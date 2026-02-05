#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, os, sys, math
import numpy as np
import soundfile as sf
from tqdm import tqdm
from scipy.signal import iirfilter, sosfiltfilt, resample_poly
import pyloudnorm as pyln

# ------------------ Utils ------------------
def db_to_lin(db): return 10.0 ** (db / 20.0)
def lin_to_db(x): return 20.0 * np.log10(np.maximum(x, 1e-12))

def ensure_stereo(x):
    if x.ndim == 1:
        return np.stack([x, x], axis=1)
    return x

# ------------------ Filters ------------------
def butter_sos(fs, fc, btype, order=2):
    ny = fs * 0.5
    wn = fc/ny if np.isscalar(fc) else np.asarray(fc)/ny
    return iirfilter(order, wn, btype=btype, ftype='butter', output='sos')

def highpass(x, fs, fc=30.0, order=2):
    sos = butter_sos(fs, fc, 'highpass', order)
    return sosfiltfilt(sos, x, axis=0)

def bandpass(x, fs, f_lo, f_hi, order=2):
    sos = butter_sos(fs, [f_lo, f_hi], 'band', order)
    return sosfiltfilt(sos, x, axis=0)

# ------------------ Denoise (spectral gate suave) ------------------


def spectral_gate(x, fs, noise_floor_db=-55.0, reduction_db=4.0, frame_len=1024, hop_len=256):
    """
    Denoise espectral robusto con STFT/ISTFT:
    - Ventana Hann length=1024, hop=256 (25%).
    - Umbral por-bin a partir del percentil 10 de magnitud y piso en dB.
    - OLA con normalización; recorte al largo original.
    """
    import numpy as np
    if x.ndim == 1:
        x = x[:, None]
    L = x.shape[0]
    C = x.shape[1]
    w = np.hanning(frame_len).astype(np.float32)

    # padding al múltiplo de hop_len
    pad = (-(L - frame_len) % hop_len) if L >= frame_len else (frame_len - L)
    xpad = np.pad(x, ((0, pad), (0,0)), mode='constant')
    N = xpad.shape[0]

    # framing
    idxs = np.arange(0, N - frame_len + 1, hop_len, dtype=int)
    nF = len(idxs)

    y = np.zeros_like(xpad, dtype=np.float32)
    norm = np.zeros(N, dtype=np.float32)

    for ch in range(C):
        # STFT
        frames = np.stack([xpad[i:i+frame_len, ch] * w for i in idxs], axis=1)  # [frame_len, nF]
        spec = np.fft.rfft(frames, axis=0)
        mag = np.abs(spec)
        phase = np.angle(spec)

        # piso por-bin a partir de percentil 10 + noise_floor_db
        floor = np.percentile(mag, 10, axis=1, keepdims=True) * (10.0 ** (noise_floor_db/20.0))
        mask = (mag >= floor).astype(np.float32) + (mag < floor).astype(np.float32) * (10.0 ** (-reduction_db/20.0))

        spec_d = (mag * mask) * np.exp(1j*phase)

        # ISTFT
        rec = np.fft.irfft(spec_d, axis=0).real  # [frame_len, nF]
        for k, i0 in enumerate(idxs):
            i1 = i0 + frame_len
            y[i0:i1, ch] += (rec[:, k] * w).astype(np.float32)
        # acumulador de normalización (por canal es el mismo w^2)
    ww = (w*w).astype(np.float32)
    for i0 in idxs:
        i1 = i0 + frame_len
        norm[i0:i1] += ww

    norm[norm < 1e-9] = 1.0
    y = y / norm[:, None]

    # recorta al largo original
    y = y[:L, :]
    return y.squeeze()

# ------------------ De-click básico ------------------
def declick_peaks(x, thresh_db=-6.0, win=3):
    if x.ndim == 1: x = x[:, None]
    y = x.copy()
    thr = db_to_lin(thresh_db)
    for ch in range(x.shape[1]):
        sig = x[:, ch]
        abs_sig = np.abs(sig)
        clicks = abs_sig > (thr * np.max(abs_sig))
        idxs = np.where(clicks)[0]
        for i in idxs:
            a = max(0, i - win)
            b = min(len(sig), i + win + 1)
            med = np.median(sig[a:b])
            y[i, ch] = med
    return y.squeeze()

# ------------------ Compresión multibanda (dynamic-EQ suave) ------------------
def multiband_compressor(x, fs,
                         bands=((20,180),(180,1200),(1200,6000),(6000,20000)),
                         thresh_db=(-30,-28,-26,-26),
                         ratio=(1.5,1.6,1.7,1.5)):
    if x.ndim == 1: x = x[:, None]
    y = np.zeros_like(x)
    for bi,(f0,f1) in enumerate(bands):
        b = bandpass(x, fs, f0, f1, order=2)
        # RMS rápido ~20 ms (por canal)
        win = max(1, int(fs*0.02))
        # energía por muestra, promediar por ventana con conv lineal
        rms = np.sqrt(np.convolve(np.mean(b**2,axis=1), np.ones(win)/win, mode='same') + 1e-12)
        rms_db = lin_to_db(rms)
        over = np.maximum(rms_db - thresh_db[bi], 0.0)
        gr_db = -over*(1.0 - 1.0/ratio[bi])
        gr_lin = db_to_lin(gr_db)
        b_comp = (b.T * gr_lin).T
        y += b_comp
    # Mezcla con señal directa 50/50 para naturalidad
    y = 0.5*y + 0.5*x
    return y.squeeze()

# ------------------ Transient shaper ------------------
def transient_shaper(x, fs, amt=0.18, hp=1500.0):
    if x.ndim == 1: x = x[:, None]
    # componente de alta frecuencia
    atk = highpass(x, fs, hp, order=1)
    env = np.abs(atk)
    env = env / (np.max(env, axis=0, keepdims=True) + 1e-9)
    gain = 1.0 + amt*env
    y = x * np.clip(gain, 0.7, 1.5)
    return y.squeeze()

# ------------------ Mid/Side procesado ------------------
def mid_side_process(stereo, fs, side_hp=150.0, widen=1.12, side_air_db=0.0):
    x = ensure_stereo(stereo)
    M = (x[:,0] + x[:,1]) * 0.5
    S = (x[:,0] - x[:,1]) * 0.5
    S = highpass(S[:,None], fs, side_hp, order=2).squeeze()
    if side_air_db != 0.0:
        # aire muy sutil 10-16 kHz
        air = bandpass(S[:,None], fs, 10000, 16000, order=1).squeeze()
        S = S + air*db_to_lin(side_air_db)
    S *= widen
    L = M + S
    R = M - S
    return np.stack([L,R], axis=1)

# ------------------ Room corto (pegamento) ------------------
def room_short(x, fs, ms=120, feedback=0.22, mix_internal=0.15):
    if x.ndim == 1: x = x[:, None]
    d = max(1, int(fs * ms/1000.0))
    y = np.copy(x)
    buf = np.zeros((d, x.shape[1]), dtype=np.float32)
    idx = 0
    for n in range(len(x)):
        wet = buf[idx]
        out = x[n] + wet*mix_internal
        y[n] = out
        buf[idx] = x[n] + wet*feedback
        idx = (idx + 1) % d
    # allpass corto para difusión
    ap_d = max(1, int(0.7*d))
    ap_g = 0.3
    ap_buf = np.zeros((ap_d, x.shape[1]), dtype=np.float32)
    idx = 0
    y2 = np.copy(y)
    for n in range(len(y)):
        ap_wet = ap_buf[idx]
        v = y[n] + (-ap_g) * ap_wet
        out = ap_wet + ap_g * v
        y2[n] = out
        ap_buf[idx] = v
        idx = (idx + 1) % ap_d
    return y2.squeeze()

# ------------------ Saturación suave ------------------
def soft_saturation(x, drive_db=3.0, blend=0.25):
    g = db_to_lin(drive_db)
    y = np.tanh(x * g)
    return (1.0 - blend)*x + blend*y

# ------------------ Loudness / Peak ------------------
def measure_lufs(x, fs):
    if x.ndim == 1: x = x[:, None]
    meter = pyln.Meter(fs)
    return meter.integrated_loudness(x.astype(np.float64))

def loudness_normalize(x, fs, target_lufs):
    loud = measure_lufs(x, fs)
    diff = target_lufs - loud
    return x * db_to_lin(diff), loud, diff

def peak_normalize_for_headroom(x, target_peak_db=-6.0):
    peak = np.max(np.abs(x)) + 1e-12
    peak_db = lin_to_db(peak)
    diff_db = target_peak_db - peak_db
    return x * db_to_lin(diff_db), peak_db, diff_db

# ------------------ Pipeline ------------------
def process_track(x, fs, args):
    # formato y canales
    x = x.astype(np.float32)
    x = ensure_stereo(x)

    # resample si hace falta
    if fs != args.sr:
        up, down = args.sr, fs
        x = np.stack([resample_poly(x[:,0], up, down),
                      resample_poly(x[:,1], up, down)], axis=1)
        fs = args.sr

    # 0) de-click y denoise
    if not args.no_declick:
        x = declick_peaks(x, thresh_db=-6.0, win=3)
    if not args.no_denoise:
        x = spectral_gate(x, fs, noise_floor_db=-55.0, reduction_db=4.0, frame_len=1024, hop_len=256)

    # 1) high-pass global 30 Hz
    x = highpass(x, fs, 30.0, order=2)

    # 2) multibanda suave (dynamic-EQ)
    if not args.no_dyn:
        x = multiband_compressor(
            x, fs,
            bands=((20,180),(180,1200),(1200,6000),(6000,20000)),
            thresh_db=(args.mb_lo_thr, args.mb_lom_thr, args.mb_mid_thr, args.mb_hi_thr),
            ratio=(1.5,1.6,1.7,1.5)
        )

    # 3) transient shaper leve
    if args.transient_amt != 0.0:
        x = transient_shaper(x, fs, amt=args.transient_amt, hp=1500.0)

    # 4) M/S: limpiar graves en side + apertura + aire opcional
    x = mid_side_process(x, fs, side_hp=150.0, widen=args.widen, side_air_db=args.side_air_db)

    # 5) room corto sutil (mezclado por fuera)
    if args.room_mix > 0.0:
        dry = x
        wet = room_short(x, fs, ms=args.room_ms, feedback=0.22, mix_internal=0.15)
        x = (1.0-args.room_mix)*dry + args.room_mix*wet

    # 6) saturación suave
    if args.sat_blend > 0.0:
        x = soft_saturation(x, drive_db=args.sat_drive_db, blend=args.sat_blend)

    # 7) loudness target y headroom
    x, lufs_before, lufs_gain = loudness_normalize(x, fs, args.lufs)
    x, peak_before_db, peak_gain_db = peak_normalize_for_headroom(x, target_peak_db=-6.0)

    return x.astype(np.float32), fs, {
        "lufs_before": lufs_before,
        "lufs_gain_db": lufs_gain,
        "peak_before_db": peak_before_db,
        "peak_gain_db": peak_gain_db
    }

def is_wav(p): return os.path.splitext(p.lower())[1] in (".wav",".wave")

def main():
    ap = argparse.ArgumentParser(description="Suno PreMaster PLUS: limpieza, M/S, transient, room, saturación, LUFS y peak (sin stems)")
    ap.add_argument("-i","--input", required=True, help="Archivo o carpeta .wav")
    ap.add_argument("-o","--output", required=True, help="Carpeta de salida")
    ap.add_argument("--sr", type=int, default=48000, help="Sample rate destino (48k recomendado)")
    ap.add_argument("--lufs", type=float, default=-20.0, help="Objetivo LUFS (pre-master)")

    # switches
    ap.add_argument("--no-denoise", action="store_true", help="Desactiva denoise espectral")
    ap.add_argument("--no-declick", action="store_true", help="Desactiva de-click")
    ap.add_argument("--no-dyn", action="store_true", help="Desactiva dynamic-EQ/multibanda")

    # multibanda thresholds
    ap.add_argument("--mb-lo-thr", type=float, default=-30.0)
    ap.add_argument("--mb-lom-thr", type=float, default=-28.0)
    ap.add_argument("--mb-mid-thr", type=float, default=-26.0)
    ap.add_argument("--mb-hi-thr", type=float, default=-26.0)

    # transients
    ap.add_argument("--transient-amt", type=float, default=0.18, help="0: off; >0 realza; <0 suaviza")

    # mid/side
    ap.add_argument("--widen", type=float, default=1.12, help="Apertura side (1.0 = sin cambio)")
    ap.add_argument("--side-air-db", type=float, default=0.0, help="Aire lateral (dB, 0-1 recomendable)")

    # room
    ap.add_argument("--room-mix", type=float, default=0.10, help="Mezcla de room (0..1)")
    ap.add_argument("--room-ms", type=float, default=120.0, help="Tamaño de sala en ms")

    # saturación
    ap.add_argument("--sat-drive-db", type=float, default=3.0, help="Drive en dB")
    ap.add_argument("--sat-blend", type=float, default=0.25, help="Mezcla 0..1")

    args = ap.parse_args()
    os.makedirs(args.output, exist_ok=True)

    # Recolectar rutas
    paths = []
    if os.path.isdir(args.input):
        for root, _, files in os.walk(args.input):
            for f in files:
                p = os.path.join(root, f)
                if is_wav(p): paths.append(p)
    else:
        if not is_wav(args.input):
            print("Entrada no es .wav", file=sys.stderr); sys.exit(1)
        paths = [args.input]

    if not paths:
        print("No se encontraron .wav en la ruta", file=sys.stderr); sys.exit(1)

    for src in tqdm(paths, desc="Procesando", unit="wav"):
        try:
            x, fs = sf.read(src, always_2d=False)
            x = x.astype(np.float32) if x.dtype.kind in "iu" else x.astype(np.float32)
            y, fs_out, _stats = process_track(x, fs, args)
            rel = os.path.relpath(src, start=args.input) if os.path.isdir(args.input) else os.path.basename(src)
            out = os.path.join(args.output, os.path.splitext(rel)[0] + "_PREPLUS.wav")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            sf.write(out, y, fs_out, subtype="PCM_24")
        except Exception as e:
            print(f"[WARN] Error con {src}: {e}", file=sys.stderr)

    print("Listo: archivos *_PREPLUS.wav")

if __name__ == "__main__":
    main()

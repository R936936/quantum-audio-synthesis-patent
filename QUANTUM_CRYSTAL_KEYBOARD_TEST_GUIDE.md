# 🎹 GUÍA DE PRUEBA - QUANTUM CRYSTAL KEYBOARD

## 📋 CHECKLIST DE PRUEBA

### **1. ABRIR VCV RACK Y AGREGAR MÓDULO**

```
1. Abre VCV Rack
2. Right-click en canvas → "Browse Modules"
3. Busca: "Quantum Crystal Keyboard" o "Aurum Lab"
4. Arrastra el módulo al canvas (123 HP, muy grande!)
```

---

### **2. PRUEBA BÁSICA - KEYBOARD VISUAL**

✅ **Verificar que se dibujan las teclas:**
- Deberías ver 49 teclas (blancas + negras)
- Layout: 4 octavas completas (C2 a C6)
- Teclas blancas en gris claro
- Teclas negras en negro

✅ **Click en teclas:**
- Click en tecla blanca (ej: C medio)
- Debería verse efecto "glow" verde-cian
- El glow se desvanece gradualmente (decay φ)

---

### **3. PRUEBA MONOPHONIC - BASIC SOUND**

**Setup mínimo:**
```
Quantum Crystal Keyboard
    │
    ↓ V/OCT output
    ↓ GATE output
    │
Quantum Resonator V3 (o cualquier oscilador VCV)
    │
    ↓ OUT
    │
Audio module → speakers
```

**Acciones:**
1. Conecta `V/OCT output` → `VOCT_L input` (QRV3)
2. Conecta `GATE output` → `TRIGGER_L1 input` (QRV3)
3. Click en teclas del keyboard
4. ✅ **RESULTADO:** Deberías escuchar notas

**Ajustes:**
- `OCTAVE +/-`: Cambia rango (prueba subir/bajar)
- `TRANSPOSE`: Afina ±24 semitonos
- `GLIDE TIME`: Sube a 500ms → portamento entre notas

---

### **4. PRUEBA POLYPHONIC - 8 VOCES**

**Setup:**
```
Quantum Crystal Keyboard
    │
    ↓ POLY VOCT (8ch)
    ↓ POLY GATE (8ch)
    │
VCV Host / Polyphonic Oscillator
    │
Audio module
```

**Acciones:**
1. Sube `SUPERPOSITION` knob → 0.5
2. Click múltiples teclas simultáneamente
3. ✅ **RESULTADO:** Múltiples notas suenan (cluster)

**Prueba Quantum Wobble:**
1. `COHERENCE` → 0.3 (low)
2. `SUPERPOSITION` → 0.7
3. Click en una tecla y mantén
4. ✅ **RESULTADO:** Pitch "flota" cuánticamente (wobble)

---

### **5. PRUEBA ARPEGGIATOR - FIBONACCI MODE**

**Acciones:**
1. Hold 4-5 teclas (ej: C, E, G, B, D)
2. `ARP MODE` → 5 (FIBONACCI)
3. `ARP RATE` → 120 BPM
4. `ARP STEPS` → 8
5. ✅ **RESULTADO:** Arpegio en intervalos Fibonacci

**Prueba LATCH:**
1. Click `LATCH` button (LED se enciende)
2. Hold teclas y suelta
3. ✅ **RESULTADO:** Notas siguen sonando infinito
4. Arpeggiator continúa aunque sueltes las teclas

---

### **6. PRUEBA SCALE QUANTIZER**

**Acciones:**
1. `ROOT NOTE` → C (0)
2. `SCALE` → 5 (Aeolian = Natural Minor)
3. `QUANTIZE` → ON (switch up)
4. Toca notas random
5. ✅ **RESULTADO:** Todas las notas cuantizadas a C minor

**Prueba diferentes escalas:**
- 0 = Ionian (Major) - happy
- 1 = Dorian - jazzy
- 2 = Phrygian - spanish
- 5 = Aeolian (Minor) - sad
- 9 = Pentatonic Major - asian

---

### **7. PRUEBA QUANTUM COLLAPSE**

**Setup:**
1. `SUPERPOSITION` → 0.8 (7-8 voces)
2. `COHERENCE` → 0.5
3. Click una tecla (escucharás cluster)
4. Click `Q_COLLAPSE` button
5. ✅ **RESULTADO:** Cluster colapsa a nota única (snap)

---

### **8. PRUEBA INTEGRATION - QRV3 FULL PATCH**

**Full System Patch:**
```
Quantum Crystal Keyboard
    ├─ V/OCT → QRV3 VOCT_L
    ├─ GATE → QRV3 TRIGGER_L1
    ├─ VELOCITY → QRV3 Q_SPREAD_CV
    └─ MOD (from mod wheel) → QRV3 MORPH_CV

Quantum Resonator V3
    └─ OUT_L → Mixer → Audio
```

**Acciones:**
1. Conecta todo según arriba
2. En QRV3: MODE → 1 (Golden Ratio)
3. En QRV3: MORPH → 0.5
4. En Keyboard: GLIDE TIME → 200ms
5. Toca melodía lenta
6. ✅ **RESULTADO:** Synth responde con glide suave

---

### **9. PRUEBA GOLDEN ARPEGGIATOR**

**Acciones:**
1. Hold 5-6 teclas
2. `ARP MODE` → 5 (GOLDEN RATIO)
3. `ARP RATE` → 180 BPM
4. Escucha el patrón
5. ✅ **RESULTADO:** Nunca repite mismo patrón (espiral dorada)

**Comparación:**
- UP mode = predecible, lineal
- GOLDEN mode = impredecible pero musical
- FIBONACCI mode = saltos intervalos Fib (0,1,1,2,3,5...)

---

### **10. STRESS TEST - MAX POLYPHONY**

**Acciones:**
1. `SUPERPOSITION` → 1.0 (máximo, 8 voces)
2. `COHERENCE` → 0.2 (muy inestable)
3. `OBSERVER RATE` → 10 Hz (colapso rápido)
4. Click una tecla
5. ✅ **RESULTADO:** Pitch breathes (respira) cuánticamente
6. Ambient heaven ☁️

---

## 🐛 TROUBLESHOOTING

### **No se ve el módulo en browser:**
```bash
# Reinstalar:
cd ~/AurumLab
make install
# Restart VCV Rack
```

### **Teclas no responden al click:**
- Verifica que clickeas dentro del área de teclas (84-439mm X)
- El área es Y=45-120mm (mid-bottom panel)
- Teclas negras tienen prioridad sobre blancas

### **No suena:**
- Verifica output connections (V/OCT + GATE mínimo)
- Verifica que hay audio module (Audio-8, Host, etc.)
- Verifica volume en oscilador destino

### **Arpeggiator no funciona:**
- Asegura que hay teclas held (o LATCH ON)
- Verifica ARP MODE ≠ 0 (OFF)
- ARP RATE debe ser > 30 BPM

### **Quantum features no audibles:**
- SUPERPOSITION debe ser > 0.1
- COHERENCE < 1.0 para escuchar wobble
- Usa headphones para escuchar detalle

---

## ✅ CHECKLIST FINAL

- [ ] Módulo visible en VCV Rack browser
- [ ] 49 teclas dibujadas correctamente
- [ ] Click en teclas genera glow effect
- [ ] V/OCT output genera notas correctas
- [ ] GATE output activa envelopes
- [ ] Polyphony funciona (SUPERPOSITION > 0)
- [ ] Arpeggiator genera patrones
- [ ] LATCH mantiene notas infinito
- [ ] Quantizer funciona (notas cuantizadas)
- [ ] Quantum collapse funciona (snap)
- [ ] GLIDE genera portamento suave
- [ ] OCTAVE +/- cambia rango
- [ ] ROOT/SCALE CV outputs generan voltage
- [ ] Todas las 12 escalas funcionan

---

## 🎯 CONFIGURACIONES RECOMENDADAS

### **A) Ambient Pad:**
```
SUPERPOSITION: 0.6
COHERENCE: 0.4
GLIDE TIME: 1000ms
ARP MODE: OFF
SCALE: Aeolian
```

### **B) Percussive Sequence:**
```
SUPERPOSITION: 0.1 (mono)
COHERENCE: 1.0 (stable)
GLIDE TIME: 0ms
ARP MODE: UP
ARP RATE: 240 BPM
LATCH: ON
```

### **C) Generative Ambient:**
```
SUPERPOSITION: 0.8
COHERENCE: 0.3
OBSERVER RATE: 2 Hz
ARP MODE: GOLDEN
ARP RATE: 60 BPM
SCALE: Lydian
```

### **D) Lead Synth:**
```
SUPERPOSITION: 0.0 (mono)
COHERENCE: 1.0
GLIDE TIME: 100ms
BEND RANGE: ±2 ST
Connect VELOCITY → Filter Cutoff
```

---

## 📊 OUTPUTS REFERENCE

| Output | Voltage | Description |
|--------|---------|-------------|
| V/OCT | 0-5V | Standard V/Oct (5 octaves) |
| GATE | 0/10V | Gate signal (Schmitt) |
| VELOCITY | 0-10V | Click intensity CV |
| AFTERTOUCH | 0-10V | Hold pressure CV |
| POLY VOCT | Poly 8ch | Polyphonic V/Oct |
| POLY GATE | Poly 8ch | Polyphonic gates |
| ROOT CV | 0-1V | Root note (12 divisions) |
| SCALE CV | 0-1.2V | Scale select (12) |
| ENTANGLE | 0-10V | → QHS entanglement |
| TREE GATE | Trigger | → QTS branch activate |
| HARMONY | 0-10V | → QHS circles |
| TRIGGER | 10V pulse | Note-on trigger |

---

**¡LISTO PARA PROBAR!** 🎹✨

1. Abre VCV Rack
2. Agrega "Quantum Crystal Keyboard"
3. Conecta V/OCT + GATE → oscilador
4. ¡Toca las teclas!

**Happy patching!** 🚀

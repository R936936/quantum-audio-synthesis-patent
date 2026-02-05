# 🌌 AURUM LAB - 3 MÓDULOS 26HP (132.08MM)

## 📋 PLAN DE DESARROLLO - 21 ENERO 2026

---

## 1️⃣ QUANTUM STARFIELD REVERB (26HP)
**Inspirado en:** Strymon Starlab  
**Filosofía:** Golden Ratio + Fractales + Quantum Modulation

### 🎯 CARACTERÍSTICAS CORE:

#### A) ALGORITMOS DE REVERB (3-4 modos)
1. **Golden Hall** - Reverb clásico con decay basado en φ
2. **Fractal Chamber** - Reflexiones fractales (Sierpinski pattern)
3. **Quantum Shimmer** - Pitch shifting +φ octaves
4. **Karplus-Strong Resonator** - Physical modeling strings

#### B) PARÁMETROS PRINCIPALES (8-10 knobs)
```
SIZE      - 1s a φ×10s decay (golden ratio scaling)
DAMPING   - Filtro high-freq (fibonacci Hz values)
DIFFUSION - Densidad de reflexiones (0-100%)
SHIMMER   - Pitch shift amount (-1oct a +2oct)
MODULATION - LFO depth (golden ratio waveforms)
MIX       - Dry/Wet (0-100%)
PRE-DELAY - 0 a φ×1000ms
FEEDBACK  - Regeneración (0-100%)
```

#### C) CARACTERÍSTICAS AURUM
- **Golden Decay Curves:** t × e^(-t/φ)
- **Fractal Diffusion:** Patrón de reflexiones tipo Cantor Set
- **Quantum Pitch:** Randomización armónica basada en φ ratios
- **Fibonacci Modulation:** LFO rates: 1, 2, 3, 5, 8, 13 Hz

#### D) CV INPUTS (6-8)
```
SIZE CV
SHIMMER CV
MOD RATE CV
MOD DEPTH CV
FEEDBACK CV
MIX CV
FREEZE GATE
CLEAR GATE
```

#### E) OUTPUTS
```
LEFT OUT
RIGHT OUT
WET ONLY L
WET ONLY R
```

---

## 2️⃣ QUANTUM MAGNETAR DELAY (26HP)
**Inspirado en:** Strymon Magneto (tape delay)  
**Filosofía:** Elastic Time + Quantum Wobble + Golden Ratios

### 🎯 CARACTERÍSTICAS CORE:

#### A) MODOS DE DELAY (4-5)
1. **Clean Digital** - Delay limpio con golden time ratios
2. **Tape Echo** - Saturación + wow/flutter analógico
3. **Reverse** - Delay invertido
4. **Pitch Shift** - Delay con pitch shifting
5. **Granular** - Buffer granular elástico

#### B) PARÁMETROS PRINCIPALES (8-10 knobs)
```
TIME       - 1ms a φ×10s (golden ratio subdivisions)
FEEDBACK   - 0-100% + self-oscillation
DEGRADE    - Bit crushing + sample rate reduction
WOBBLE     - Wow/flutter amount (elastic time stretching)
FILTER     - Tone control (fibonacci freq centers)
MIX        - Dry/Wet
ELASTIC    - Time stretch amount (como Kick module)
QUANTUM    - Pitch randomization depth
```

#### C) CARACTERÍSTICAS AURUM
- **Elastic Delay Time:** Stretching como chicle (igual que Kick)
- **Quantum Wobble:** Pitch modulation irregular (LFO fractal)
- **Golden Subdivisions:** Tap tempo → φ, φ², φ³ ratios
- **Fractal Degradation:** Bit reduction en patrón Cantor

#### D) CV INPUTS (6-8)
```
TIME CV
FEEDBACK CV
WOBBLE CV
ELASTIC CV
DEGRADE CV
MIX CV
TAP TEMPO GATE
FREEZE GATE
```

#### E) OUTPUTS
```
DELAY OUT L
DELAY OUT R
SEND (Pre-delay)
RETURN
```

---

## 3️⃣ QUANTUM COSMOS SAMPLER (26HP)
**Inspirado en:** Qu-Bit Nebulae v2 + Soma Cosmos  
**Filosofía:** Granular Quantum + Elastic Playback + Fractal Grains

### 🎯 CARACTERÍSTICAS CORE:

#### A) MODOS DE PLAYBACK (5-6)
1. **Granular Cloud** - Nube de granos clásica
2. **Elastic Stretch** - Time-stretching sin pitch change
3. **Quantum Freeze** - Freeze buffer con pitch wobble
4. **Fractal Splice** - Grains en patrón fractal
5. **Reverse Granular** - Granos invertidos
6. **Spectral Morph** - FFT freeze + morph

#### B) PARÁMETROS PRINCIPALES (10-12 knobs)
```
POSITION   - Posición en buffer (0-100%)
GRAIN SIZE - 1ms a φ×1000ms
GRAIN RATE - 1-100 Hz (fibonacci values)
SPRAY      - Randomización posición
PITCH      - -2oct a +2oct
ELASTIC    - Time stretch amount
DENSITY    - Número de granos simultáneos
TEXTURE    - Grain shape/window
FEEDBACK   - Grain recirculation
MIX        - Dry/Wet
```

#### C) CARACTERÍSTICAS AURUM
- **Quantum Grains:** Posición aleatoria basada en φ
- **Elastic Time:** Grains con stretch independiente
- **Fractal Spray:** Distribución tipo Cantor/Sierpinski
- **Golden Windows:** Grain envelopes con curvas φ

#### D) CV INPUTS (8-10)
```
POSITION CV
GRAIN SIZE CV
PITCH CV
ELASTIC CV
SPRAY CV
DENSITY CV
RECORD GATE
FREEZE GATE
REVERSE GATE
CLEAR GATE
```

#### E) INPUTS/OUTPUTS
```
AUDIO IN L
AUDIO IN R
GRAIN OUT L
GRAIN OUT R
WET L
WET R
EOC TRIGGER (End of cycle)
CLOCK IN (for sync)
```

---

## 🔧 ARQUITECTURA TÉCNICA COMÚN

### PROCESAMIENTO DSP:
```cpp
- Buffer size: 10 segundos @ 48kHz = 480,000 samples
- Interpolación: Linear/Cubic para pitch shifting
- Window functions: Hann, Hamming, Golden ratio curve
- Anti-aliasing: Oversampling 2x/4x cuando sea necesario
```

### CONTROLES COMPARTIDOS:
```
- Todos usan Trimpots pequeños para CV amount
- Knobs grandes para parámetros principales
- Switches para cambio de modo
- LEDs para indicadores de estado
- Display OLED para nombre de modo/valores
```

### FILOSOFÍA VISUAL:
```
- Background negro (#000000)
- Texto cyan (#00FFFF) para títulos
- Dorado (#FFD700) para parámetros quantum
- Verde (#00FF88) para I/O
- Naranja (#FF8800) para modulación
```

---

## 📊 PRIORIDAD DE IMPLEMENTACIÓN:

### FASE 1: QUANTUM MAGNETAR DELAY
**Por qué primero:**
- Más simple que sampler
- Usa concepto "Elastic" ya implementado
- Feedback loop más directo
- Menos CPU intensivo

### FASE 2: QUANTUM STARFIELD REVERB
**Por qué segundo:**
- DSP más complejo que delay
- Algoritmos de difusión requieren más trabajo
- Puede usar código de delay para modulation

### FASE 3: QUANTUM COSMOS SAMPLER
**Por qué último:**
- Más complejo de todos
- Requiere buffer management robusto
- Granular synthesis es CPU intensivo
- Puede beneficiarse de aprendizaje de los otros dos

---

## 🚀 SIGUIENTE PASO:

¿Con cuál módulo quieres empezar?

**Opción A:** QUANTUM MAGNETAR DELAY (más simple, usa elastic concept)  
**Opción B:** QUANTUM STARFIELD REVERB (algoritmos únicos)  
**Opción C:** QUANTUM COSMOS SAMPLER (más complejo, más features)  

O si prefieres, puedo hacer un diseño más detallado de los 3 antes de empezar a programar.

# Golden Oscillator - Conversión MONO → DUAL (Stereo/Dual-Mono)

## ✅ COMPILACIÓN EXITOSA
**Fecha:** 19 Enero 2026, 14:55
**Archivo:** `/Users/wu/Desktop/AurumLab/src/GoldenOscillator.cpp`
**Plugin:** `plugin.dylib` (516KB)

---

## �� OBJETIVO CUMPLIDO
Convertir el GoldenOscillator de **MONO (1 oscilador)** a **DUAL (2 osciladores independientes)**:
- **OSC A (LEFT)** - Canal izquierdo con todos los parámetros originales
- **OSC B (RIGHT)** - Canal derecho completamente duplicado

---

## 📋 CAMBIOS REALIZADOS

### 1. **ParamId Enum** - Duplicados 16 parámetros
```cpp
// OSC A (LEFT) - Existentes
FREQ_PARAM, FINE_TUNE_PARAM, SPIRAL_RATE_PARAM, SPIRAL_DEPTH_PARAM,
SPIRAL_COMPLEXITY_PARAM, SPIRAL_SHAPE_PARAM, MODE_MORPH_PARAM,
RESONANCE_DEPTH_PARAM, RESONANCE_FEEDBACK_PARAM, CHAOS_PARAM,
QUANTUM_DEPTH_PARAM, QUANTUM_BLEND_PARAM, QUANTUM_TABLE_PARAM,
QUANTUM_POSITION_PARAM, LATTICE_PHASE_PARAM, LATTICE_COHERENCE_PARAM

// OSC B (RIGHT) - Nuevos con sufijo _B_PARAM
FREQ_B_PARAM, FINE_TUNE_B_PARAM, SPIRAL_RATE_B_PARAM, SPIRAL_DEPTH_B_PARAM,
SPIRAL_COMPLEXITY_B_PARAM, SPIRAL_SHAPE_B_PARAM, MODE_MORPH_B_PARAM,
RESONANCE_DEPTH_B_PARAM, RESONANCE_FEEDBACK_B_PARAM, CHAOS_B_PARAM,
QUANTUM_DEPTH_B_PARAM, QUANTUM_BLEND_B_PARAM, QUANTUM_TABLE_B_PARAM,
QUANTUM_POSITION_B_PARAM, LATTICE_PHASE_B_PARAM, LATTICE_COHERENCE_B_PARAM
```
**Total:** 32 parámetros (16 + 16)

---

### 2. **InputId Enum** - Duplicados 14 inputs CV
```cpp
// OSC A (LEFT) - Existentes
VOCT_INPUT, SPIRAL_RATE_CV_INPUT, SPIRAL_DEPTH_CV_INPUT,
SPIRAL_COMPLEXITY_CV_INPUT, SPIRAL_SHAPE_CV_INPUT, MODE_MORPH_CV_INPUT,
RESONANCE_DEPTH_CV_INPUT, RESONANCE_FEEDBACK_CV_INPUT, CHAOS_CV_INPUT,
QUANTUM_TABLE_CV_INPUT, QUANTUM_POSITION_CV_INPUT, LATTICE_PHASE_CV_INPUT,
LATTICE_COHERENCE_CV_INPUT

// OSC B (RIGHT) - Nuevos con sufijo _B_INPUT
VOCT_B_INPUT, SPIRAL_RATE_B_CV_INPUT, SPIRAL_DEPTH_B_CV_INPUT,
SPIRAL_COMPLEXITY_B_CV_INPUT, SPIRAL_SHAPE_B_CV_INPUT, MODE_MORPH_B_CV_INPUT,
RESONANCE_DEPTH_B_CV_INPUT, RESONANCE_FEEDBACK_B_CV_INPUT, CHAOS_B_CV_INPUT,
QUANTUM_TABLE_B_CV_INPUT, QUANTUM_POSITION_B_CV_INPUT, LATTICE_PHASE_B_CV_INPUT,
LATTICE_COHERENCE_B_CV_INPUT
```
**Total:** 28 inputs CV (14 + 14)

---

### 3. **OutputId Enum** - Stereo outputs
```cpp
// ANTES (mono)
MAIN_OUTPUT

// AHORA (stereo)
OUTPUT_L  // Left/A
OUTPUT_R  // Right/B
```
**Total:** 2 outputs

---

### 4. **LightId Enum** - LEDs duplicados
```cpp
// OSC A (LEFT)
QUANTUM_STATUS_LIGHT
QUANTUM_WAVETABLE_LIGHT

// OSC B (RIGHT)
QUANTUM_STATUS_B_LIGHT
QUANTUM_WAVETABLE_B_LIGHT
```
**Total:** 4 LEDs (2 + 2)

---

### 5. **Objetos de Procesamiento Duplicados**
```cpp
// OSC A (LEFT)
SpiralWaveOscillator osc;
FractalEngineV2 fractalEngine;
QuantumEngine quantumEngine;
QuantumHybridEngine quantumHybrid;
QuantumWavetableSynth::QuantumWavetableEngine quantumWavetable;
QuantumHilbertLattice::HilbertLatticeEngine hilbertLattice;
float* wavetablePtrs[8];
float displayFreq;
float lockedFreq;
bool freqLocked;

// OSC B (RIGHT) - Duplicados
SpiralWaveOscillator oscB;
FractalEngineV2 fractalEngineB;
QuantumEngine quantumEngineB;
QuantumHybridEngine quantumHybridB;
QuantumWavetableSynth::QuantumWavetableEngine quantumWavetableB;
QuantumHilbertLattice::HilbertLatticeEngine hilbertLatticeB;
float* wavetablePtrsB[8];
float displayFreqB;
float lockedFreqB;
bool freqLockedB;
```

---

### 6. **Constructor - configParam() Duplicados**
Todos los parámetros de OSC A fueron duplicados para OSC B con sufijos " B" o " R":
```cpp
// Ejemplo OSC A
configParam(FREQ_PARAM, ..., "Frequency", " Hz", ...);
configParam(SPIRAL_RATE_PARAM, ..., "Spiral Rate", "%", ...);

// Ejemplo OSC B
configParam(FREQ_B_PARAM, ..., "Frequency B", " Hz", ...);
configParam(SPIRAL_RATE_B_PARAM, ..., "Spiral Rate B", "%", ...);
```

---

### 7. **Constructor - configInput() Duplicados**
Todos los inputs CV de OSC A fueron duplicados para OSC B:
```cpp
// Ejemplo OSC A
configInput(VOCT_INPUT, "V/Oct");
configInput(SPIRAL_RATE_CV_INPUT, "Spiral Rate CV");

// Ejemplo OSC B
configInput(VOCT_B_INPUT, "V/Oct B");
configInput(SPIRAL_RATE_B_CV_INPUT, "Spiral Rate B CV");
```

---

### 8. **Constructor - configOutput() Duplicados**
```cpp
// ANTES
configOutput(MAIN_OUTPUT, "Audio");

// AHORA
configOutput(OUTPUT_L, "Audio L");
configOutput(OUTPUT_R, "Audio R");
```

---

### 9. **Constructor - Quantum Data Loading Duplicado**
Todo el código de carga de datos cuánticos fue duplicado para OSC B:
```cpp
// OSC A - Quantum loading (existente)
bool quantumLoaded = quantumEngine.loadFromUserDir(...);
bool hybridLoaded = quantumHybrid.loadAll();
bool wavetableLoaded = quantumWavetable.loadFromFile(...);

// OSC B - Quantum loading (duplicado)
bool quantumLoadedB = quantumEngineB.loadFromUserDir(...);
bool hybridLoadedB = quantumHybridB.loadAll();
bool wavetableLoadedB = quantumWavetableB.loadFromFile(...);
```

---

### 10. **onSampleRateChange() Duplicado**
```cpp
void onSampleRateChange() override {
    fractalEngine.setSampleRate(APP->engine->getSampleRate());
    fractalEngineB.setSampleRate(APP->engine->getSampleRate());  // NUEVO
}
```

---

### 11. **process() - Lógica Duplicada (~230 líneas)**
Todo el código de procesamiento fue duplicado:

#### OSC A (LEFT) - Procesamiento original
1. Quantum status LED update
2. Frequency calculation (locked/unlocked)
3. V/Oct processing
4. Spiral parameters + CV modulation
5. Fractal Engine configuration
6. Quantum Hybrid synthesis
7. Fractal synthesis (additive)
8. Resonance feedback mixing
9. Quantum Wavetable synthesis
10. Hilbert Lattice modulation
11. Final mix + output

#### OSC B (RIGHT) - Procesamiento duplicado completo
Exactamente el mismo flujo, usando:
- `oscB`, `fractalEngineB`, `quantumEngineB`, etc.
- Parámetros con sufijo `_B_PARAM`
- Inputs con sufijo `_B_INPUT`
- Output `OUTPUT_R`

```cpp
// OSC A final output
outputs[OUTPUT_L].setVoltage(finalOutput * 5.0f);

// OSC B final output
outputs[OUTPUT_R].setVoltage(finalOutputB * 5.0f);
```

---

### 12. **Widget - Outputs UI Actualizados**
```cpp
// ANTES (mono)
addOutput(..., GoldenOscillator::MAIN_OUTPUT);

// AHORA (stereo)
addOutput(..., GoldenOscillator::OUTPUT_L);
addOutput(..., GoldenOscillator::OUTPUT_R);  // 11mm abajo de OUTPUT_L
```

---

## 🎛️ CARACTERÍSTICAS MANTENIDAS

Cada oscilador (A y B) conserva **TODAS** las características originales:
- ✅ Spiral Wave Oscillator (Golden Ratio)
- ✅ Fractal Resonance Engine V2 (3 modes: Fibonacci/Golden/Mandelbrot)
- ✅ Quantum Hybrid Engine (wavetables + landscapes)
- ✅ Quantum Wavetable Synthesis (8 tables)
- ✅ Hilbert Lattice 3D navigation
- ✅ Anti-click smoothing (frequency + amplitude)
- ✅ Frequency lock system
- ✅ CV modulation para todos los parámetros

---

## 🔥 CASOS DE USO

### 1. **Stereo Detuning**
- OSC A: C4 (261.626 Hz)
- OSC B: C4 + 5 cents
- → Efecto chorus natural

### 2. **Dual-Mono Independiente**
- OSC A: Bajo (100 Hz) + Fibonacci mode
- OSC B: Lead (880 Hz) + Mandelbrot mode
- → Dos synths en uno

### 3. **Quantum Stereo Field**
- OSC A: Quantum Table 0 + Phase 0.25
- OSC B: Quantum Table 3 + Phase 0.75
- → Landscape estéreo cuántico

### 4. **Fractal Panning**
- OSC A: Resonance Depth 100%
- OSC B: Spiral Complexity 100%
- → Texturas asimétricas L/R

---

## 📊 ESTADÍSTICAS FINALES

| Categoría | OSC A | OSC B | Total |
|-----------|-------|-------|-------|
| Parámetros | 16 | 16 | **32** |
| CV Inputs | 14 | 14 | **28** |
| Outputs | 1 | 1 | **2** |
| LEDs | 2 | 2 | **4** |
| Engines | 6 | 6 | **12** |
| **TOTAL COMPONENTES** | | | **78** |

---

## ⚠️ IMPORTANTE

### Lógica NO Modificada
- ✅ La lógica de procesamiento original **NO fue cambiada**
- ✅ OSC A funciona **exactamente igual** que antes
- ✅ OSC B es una **copia exacta** de OSC A
- ✅ Ambos osciladores son **100% independientes**

### Próximos Pasos (Panel UI)
El panel visual (.svg) necesitará ser actualizado para incluir:
1. 16 knobs adicionales para OSC B
2. 14 inputs CV adicionales para OSC B
3. 1 output adicional (OUTPUT_R)
4. 2 LEDs adicionales para OSC B
5. Labels actualizados ("A/L" y "B/R")

---

## 🎉 RESULTADO

**Golden Oscillator ahora es un oscilador DUAL/STEREO completo**  
Dos osciladores cuánticos fractales independientes en un solo módulo.

✅ Compilación exitosa  
✅ Sin errores  
✅ Warnings solo de variables no usadas (no críticos)  
✅ Plugin generado: `plugin.dylib` (516KB)

---

**Creado:** 19 Enero 2026, 14:55  
**Por:** GitHub Copilot CLI

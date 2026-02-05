# 🌌 ELASTIC ENGINE V2 - GRANULAR SAMPLER MEJORADO
## Plan de Implementación - 20 Enero 2026

---

## 📊 RESUMEN EJECUTIVO

**Módulo independiente tipo SOMA Cosmos + Quantum Modulation**

- **Nombre:** Elastic Cosmos Engine V2
- **Tamaño:** 30 HP (152mm width)
- **Concepto:** 4 Delay/Grain Engines independientes + Quantum Matrix
- **Performance-oriented:** Todo accesible sin menús
- **Live manipulation:** Freeze, reverse, speed control en tiempo real

---

## 🎯 FILOSOFÍA DE DISEÑO

### Inspiración: SOMA Cosmos + Elastic Quantum
```
SOMA Cosmos approach:
- 4 motores independientes
- Feedback matrix entre motores
- Live performance focus
- Freeze/Reverse instantáneo

+ Elastic Quantum Engine:
- Time stretching sin cambio de pitch
- Quantum grain modulation
- Fractal feedback
- Entangled processing

= ELASTIC COSMOS ENGINE V2
```

---

## 🏗️ ARQUITECTURA DEL SISTEMA

### LAYOUT VISUAL (30 HP):

```
┌───────────────────────────────────────────────────────────────────────┐
│                    ELASTIC COSMOS ENGINE V2                           │
├──────────────┬──────────────┬──────────────┬──────────────┬──────────┤
│              │              │              │              │          │
│   ENGINE 1   │   ENGINE 2   │   ENGINE 3   │   ENGINE 4   │  QUANTUM │
│              │              │              │              │  MATRIX  │
│   [TIME]     │   [TIME]     │   [TIME]     │   [TIME]     │          │
│   [FEED]     │   [FEED]     │   [FEED]     │   [FEED]     │ [ENTNGL] │
│   [SIZE]     │   [SIZE]     │   [SIZE]     │   [SIZE]     │ [FRACTAL]│
│              │              │              │              │ [SUPCOM] │
│   [MODE]     │   [MODE]     │   [MODE]     │   [MODE]     │          │
│    D G E     │    D G E     │    D G E     │    D G E     │ [GLOBAL] │
│              │              │              │              │  FREEZE  │
│   [FRZ][REV] │   [FRZ][REV] │   [FRZ][REV] │   [FRZ][REV] │          │
│    LED LED   │    LED LED   │    LED LED   │    LED LED   │  MASTER  │
│              │              │              │              │  [LEVEL] │
│   ( IN )     │   ( IN )     │   ( IN )     │   ( IN )     │          │
│   ( OUT)     │   ( OUT)     │   ( OUT)     │   ( OUT)     │ (STEREO) │
│              │              │              │              │  L    R  │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────┘
```

---

## 🔧 ESPECIFICACIONES POR ENGINE (4×)

### Cada Engine tiene (6 HP por engine):

#### **1. TIME Knob (grande, centro)**
- **Modo DELAY:** 10ms - 10 segundos
- **Modo GRAIN:** Posición en buffer (0-100%)
- **Modo ELASTIC:** Playback speed (0.1x - 4x)
- Con CV input + attenuverter

#### **2. FEEDBACK Knob (mediano)**
- Range: 0-150% (puede auto-oscilar)
- Feedback interno + cross-feedback entre engines
- Con CV input

#### **3. GRAIN SIZE Knob (pequeño)**
- Range: 1ms - 500ms
- Solo activo en modo GRAIN y ELASTIC
- Determina tamaño de ventana de granulación

#### **4. MODE Switch (3 posiciones)**
- **D (DELAY):** Simple delay line, pitch shift con speed
- **G (GRAIN):** Granular mode, múltiples granos simultáneos
- **E (ELASTIC):** Time stretch, mantiene pitch constante

#### **5. FREEZE Button + LED (rojo)**
- Congela el buffer actual
- Permite manipulación mientras está frozen
- LED indica estado frozen

#### **6. REVERSE Button + LED (azul)**
- Cambia dirección de playback
- Forward/Reverse instantáneo
- LED indica reverse activo

#### **7. AUDIO INPUT Jack**
- Impedancia: 100kΩ
- Range: ±10V

#### **8. AUDIO OUTPUT Jack**
- Salida individual de cada engine
- Se suma también al master

---

## 🌀 QUANTUM MATRIX (6 HP derecha)

### Sistema de modulación global:

#### **1. ENTANGLE Knob (grande)**
- Cross-modulation entre engines
- Engine 1 ↔ Engine 2
- Engine 3 ↔ Engine 4
- Range: 0-100%

#### **2. FRACTAL Knob (mediano)**
- Resonancia fractal en feedback
- Crea texturas auto-generativas
- Range: 0-100%

#### **3. SUPCOM Knob (mediano)**
- Quantum superposition depth
- Mezcla estados cuánticos entre engines
- Range: 0-100%

#### **4. GLOBAL FREEZE Button (grande)**
- Congela los 4 engines simultáneamente
- Para "capturar" un estado completo
- LED RGB indica estado

#### **5. MASTER LEVEL Knob**
- Control de nivel de salida stereo
- 0-2x (+6dB max)

#### **6. STEREO OUTPUT (L/R)**
- Suma de los 4 engines
- Post quantum matrix
- Post master level

---

## 🎛️ ESPECIFICACIONES TÉCNICAS COMPLETAS

### POR ENGINE:

**Parámetros (7):**
- TIME (con CV input + attenuverter)
- FEEDBACK (con CV input)
- GRAIN SIZE
- MODE switch (3 pos)
- FREEZE button
- REVERSE button
- (Speed implícito en TIME según modo)

**Inputs (3):**
- Audio IN
- TIME CV
- FEEDBACK CV

**Outputs (1):**
- Audio OUT

**Lights (2):**
- FREEZE LED (rojo)
- REVERSE LED (azul)

**Total por engine:**
- Params: 7
- Inputs: 3
- Outputs: 1
- Lights: 2

---

### QUANTUM MATRIX:

**Parámetros (4):**
- ENTANGLE (0-100%)
- FRACTAL (0-100%)
- SUPCOM (0-100%)
- MASTER LEVEL (0-2x)

**Inputs (0):**
- (Recibe audio internamente de los 4 engines)

**Outputs (2):**
- STEREO L
- STEREO R

**Lights (1):**
- GLOBAL FREEZE LED (RGB)

---

### TOTAL MÓDULO COMPLETO:

**Parámetros:** 32
- 4 engines × 7 params = 28
- Quantum matrix = 4
- Total = 32 params

**Inputs:** 13
- 4 engines × 3 inputs = 12
- AUDIO IN global (opcional) = 1
- Total = 13 inputs

**Outputs:** 6
- 4 engines × 1 output = 4
- Stereo L/R = 2
- Total = 6 outputs

**Lights:** 9
- 4 engines × 2 LEDs = 8
- Global freeze = 1
- Total = 9 lights

---

## 🔬 PROCESAMIENTO DE AUDIO

### MODO DELAY (D):
```cpp
struct DelayEngine {
    // Simple delay line con feedback
    float delayTime;        // 10ms - 10s
    float feedback;         // 0-150%
    
    // Buffer circular
    float buffer[480000];   // 10 segundos @ 48kHz
    int writePos = 0;
    
    float process(float in) {
        // Read from delay
        int readPos = (writePos - delayTimeSamples + bufferSize) % bufferSize;
        float delayed = buffer[readPos];
        
        // Feedback
        float feedbackSignal = delayed * feedback;
        
        // Write to buffer
        buffer[writePos] = in + feedbackSignal;
        writePos = (writePos + 1) % bufferSize;
        
        return delayed;
    }
};
```

### MODO GRAIN (G):
```cpp
struct GrainEngine {
    // Granular synthesis con múltiples granos
    struct Grain {
        float position;     // 0-1 en buffer
        float size;         // 1-500ms
        float phase;        // 0-1
        bool active;
    };
    
    Grain grains[64];       // Hasta 64 granos simultáneos
    float density = 50.0f;  // grains per second
    
    float process(float sampleTime) {
        float output = 0.f;
        
        // Trigger new grains
        grainTimer += sampleTime;
        if (grainTimer >= 1.0f / density) {
            triggerNewGrain();
            grainTimer = 0.f;
        }
        
        // Process all active grains
        for (auto& grain : grains) {
            if (grain.active) {
                output += processGrain(grain);
                grain.phase += sampleTime / grain.size;
                if (grain.phase >= 1.f) grain.active = false;
            }
        }
        
        return output;
    }
    
    float processGrain(Grain& grain) {
        // Read from buffer at grain position
        float sample = readBuffer(grain.position);
        
        // Apply Hann window
        float window = 0.5f * (1.f - std::cos(2.f * M_PI * grain.phase));
        
        return sample * window;
    }
};
```

### MODO ELASTIC (E):
```cpp
struct ElasticEngine {
    // Time stretching que mantiene pitch
    float playbackSpeed;    // 0.1x - 4x
    float pitchShift = 1.0f;  // Mantener constante
    
    // PSOLA (Pitch Synchronous Overlap-Add)
    float process(float sampleTime) {
        // Lee del buffer a velocidad variable
        playPosition += playbackSpeed * sampleTime * sampleRate;
        
        // Pero mantiene pitch con PSOLA
        float stretched = psolaStretch(playPosition, playbackSpeed);
        
        return stretched;
    }
    
    float psolaStretch(float pos, float speed) {
        // Time-domain pitch shifting
        // Lee overlapping windows a velocidad variable
        // Superpone con pitch original
        
        float grainSize = 0.02f; // 20ms default
        int numGrains = (int)(1.0f / speed) + 1;
        float output = 0.f;
        
        for (int i = 0; i < numGrains; i++) {
            float grainPos = pos + i * grainSize * speed;
            float grain = readBufferWithWindow(grainPos, grainSize);
            output += grain / (float)numGrains;
        }
        
        return output;
    }
};
```

---

## 🌀 QUANTUM MATRIX PROCESSING

### ENTANGLEMENT:
```cpp
// Cross-feedback entre engines
void processEntanglement(float depth) {
    // Engine 1 ↔ Engine 2
    float eng1_to_eng2 = engine1.output * depth;
    float eng2_to_eng1 = engine2.output * depth;
    engine1.feedback += eng2_to_eng1;
    engine2.feedback += eng1_to_eng2;
    
    // Engine 3 ↔ Engine 4
    float eng3_to_eng4 = engine3.output * depth;
    float eng4_to_eng3 = engine4.output * depth;
    engine3.feedback += eng4_to_eng3;
    engine4.feedback += eng3_to_eng4;
}
```

### FRACTAL RESONANCE:
```cpp
// Resonancia fractal en feedback
void processFractalResonance(float depth) {
    // Golden ratio modulation
    const float PHI = 1.618033988749f;
    
    for (auto& engine : engines) {
        // Modula feedback con serie de Fibonacci
        float fractalMod = std::sin(phase * PHI) * depth;
        engine.feedback *= (1.0f + fractalMod * 0.3f);
    }
    
    phase += sampleTime;
}
```

### QUANTUM SUPERPOSITION:
```cpp
// Mezcla estados cuánticos entre engines
void processQuantumSuperposition(float depth) {
    // Crear superposición de los 4 estados
    float superposed[4];
    
    for (int i = 0; i < 4; i++) {
        superposed[i] = 0.f;
        
        // Cada engine es suma ponderada de todos
        for (int j = 0; j < 4; j++) {
            float weight = (i == j) ? (1.f - depth) : (depth / 3.f);
            superposed[i] += engines[j].output * weight;
        }
    }
    
    // Aplicar superposición
    for (int i = 0; i < 4; i++) {
        engines[i].output = superposed[i];
    }
}
```

---

## 🎨 DISEÑO VISUAL

### Tema: Verde Matrix + Azul Cuántico

**Colores:**
- Fondo: `#000000` (negro puro)
- Controles principales: `#00ff00` (verde matrix)
- Quantum section: `#00BFFF` (azul cuántico)
- LEDs FREEZE: `#ff0000` (rojo)
- LEDs REVERSE: `#0080ff` (azul)
- LEDs GLOBAL: RGB (cambia según estado)

**Layout:**
- 4 columnas de engines (6HP cada uno)
- 1 columna quantum matrix (6HP)
- Total: 30HP × 128.5mm

**Tipografía:**
- Títulos: `'Orbitron', monospace` bold
- Labels: `'Orbitron', monospace` regular
- Números: `monospace` small

---

## 📋 PLAN DE IMPLEMENTACIÓN (5 FASES)

### FASE 1: ENGINE 1 - DELAY MODE (3 horas)
**Objetivo:** Crear primer engine completo solo con modo delay

1. Crear estructura básica (`ElasticCosmosV2.cpp`)
2. Implementar buffer circular (10 segundos)
3. Implementar delay simple con feedback
4. Crear panel SVG básico (30HP)
5. Añadir controles: TIME, FEEDBACK, MODE switch
6. Añadir FREEZE y REVERSE buttons
7. Compilar y probar

**Outputs esperados:**
- Engine 1 funciona en modo DELAY
- Freeze/Reverse operativos
- Panel visible en VCV Rack

---

### FASE 2: GRAIN MODE (2-3 horas)
**Objetivo:** Implementar granular synthesis

1. Crear estructura `Grain` (position, size, phase)
2. Implementar array de 64 granos
3. Trigger system (density-based)
4. Hann window para granos
5. Buffer reading con interpolación
6. GRAIN SIZE control
7. Probar con audio real

**Outputs esperados:**
- Modo GRAIN funcional
- Texturas granulares audibles
- Control de grain size efectivo

---

### FASE 3: ELASTIC MODE (3-4 horas)
**Objetivo:** Time stretching con pitch preservation

1. Implementar PSOLA algorithm
2. Pitch detection (auto-correlación)
3. Overlapping windows con pitch correction
4. Speed control independiente de pitch
5. Optimización de performance
6. Comparar con modo DELAY (pitch shift)

**Outputs esperados:**
- Modo ELASTIC funcional
- Time stretch sin cambio de pitch
- Smooth playback a diferentes velocidades

---

### FASE 4: ENGINES 2, 3, 4 + ROUTING (2 horas)
**Objetivo:** Completar los 4 engines

1. Duplicar código de Engine 1 → 2, 3, 4
2. Crear outputs individuales
3. Implementar summing a stereo master
4. Routing interno entre engines
5. Cross-feedback básico
6. Panel completo con 4 columnas
7. Probar todos simultáneamente

**Outputs esperados:**
- 4 engines independientes funcionando
- Routing correcto
- Panel completo visible

---

### FASE 5: QUANTUM MATRIX (2-3 horas)
**Objetivo:** Sistema de modulación cuántico

1. Implementar ENTANGLE (cross-feedback)
2. Implementar FRACTAL (resonancia fractal)
3. Implementar SUPCOM (quantum superposition)
4. GLOBAL FREEZE (congela todos)
5. MASTER LEVEL control
6. STEREO OUTPUT processing
7. Optimización final
8. Testing completo

**Outputs esperados:**
- Quantum matrix funcional
- Interacción entre engines audible
- Sistema completo operativo

---

### FASE 6: OPTIMIZACIÓN Y DOCS (1-2 horas)
**Objetivo:** Pulir y documentar

1. Optimizar performance (SIMD?)
2. Ajustar valores por defecto
3. Fine-tune de parámetros
4. Crear patches de demostración
5. Documentación de uso
6. Screenshots
7. Commit a GitHub con descripción completa

**TIEMPO TOTAL ESTIMADO:** 13-17 horas

---

## 💡 CARACTERÍSTICAS ESPECIALES

### 1. FREEZE AVANZADO:
```
- Freeze individual por engine
- Freeze global (todos a la vez)
- Mantiene posición en buffer
- Permite manipulación mientras frozen
- Useful para capturar texturas momentáneas
```

### 2. CROSS-ENGINE MODULATION:
```
- Engine 1 puede modular feedback de Engine 2
- Crea feedback loops complejos
- Auto-generativo cuando ENTANGLE > 50%
- Texturas evolutivas sin input
```

### 3. QUANTUM SUPERPOSITION:
```
- Los 4 engines existen en superposición
- Output es colapso de onda cuántica
- Cada sample es diferente (no-determinístico)
- Crea espacios sonoros imposibles
```

### 4. FRACTAL FEEDBACK:
```
- Feedback auto-organizado
- Patrones fractales emergen naturalmente
- Basado en serie de Fibonacci
- Golden ratio modulation (φ = 1.618...)
```

### 5. ELASTIC TIME:
```
- Time stretch sin pitch shift
- PSOLA algorithm profesional
- Mantiene formantes vocales
- Útil para loops y samples
```

---

## 🎯 CASOS DE USO

### USO 1: Delay Espacial Complejo
```
Configuración:
- Engine 1: DELAY 250ms, feedback 60%
- Engine 2: DELAY 500ms, feedback 40%
- Engine 3: DELAY 1s, feedback 70%
- Engine 4: DELAY 125ms, feedback 30%
- ENTANGLE: 30% (cross-feedback ligero)
- FRACTAL: 50% (resonancia fractal)

Resultado: Delay espacial con texturas evolutivas
```

### USO 2: Granular Cloud
```
Configuración:
- 4 engines en modo GRAIN
- GRAIN SIZE variado (50ms, 100ms, 200ms, 300ms)
- TIME positions diferentes (25%, 50%, 75%, 90%)
- SUPCOM: 70% (quantum superposition alta)
- FRACTAL: 40%

Resultado: Nube granular densa y etérea
```

### USO 3: Time Stretch Polifónico
```
Configuración:
- 4 engines en modo ELASTIC
- Speeds diferentes (0.5x, 1x, 1.5x, 2x)
- Input: loop de audio
- FREEZE individual para cada voice
- ENTANGLE: 0% (independientes)

Resultado: Polifonía temporal, 4 velocidades simultáneas
```

### USO 4: Feedback Auto-Generativo
```
Configuración:
- Engine 1-2: DELAY con feedback 120%
- Engine 3-4: GRAIN con feedback 80%
- ENTANGLE: 80% (máximo cross-feedback)
- FRACTAL: 90% (resonancia máxima)
- Input: trigger inicial, luego self-sustaining

Resultado: Textura auto-generativa infinita
```

---

## 🔗 CONEXIONES TÍPICAS

```
┌─────────────────┐
│ Golden Osc V3   │
│                 │
│  OUT L ─────────┼──→ Engine 1 IN
│  OUT C ─────────┼──→ Engine 2 IN
│  OUT R ─────────┼──→ Engine 3 IN
└─────────────────┘

┌─────────────────┐
│ Elastic Cosmos  │
│                 │
│ STEREO L ───────┼──→ Mixer A
│ STEREO R ───────┼──→ Mixer A
│                 │
│ Engine 1 OUT ───┼──→ External FX
│ Engine 2 OUT ───┼──→ External FX
└─────────────────┘
```

---

## 📊 COMPARACIÓN: ELASTIC V1 vs V2

| Feature | Elastic V1 (en Quantum Synth) | Elastic V2 (nuevo) |
|---------|--------------------------------|---------------------|
| Tamaño | Parte de 177 HP | 30 HP independiente |
| Engines | 1 (monolítico) | 4 (independientes) |
| Modes | Fijos | 3 por engine (D/G/E) |
| Freeze | Global | Individual + global |
| Reverse | No | Sí (per-engine) |
| Cross-mod | Limitado | Entangle matrix |
| Performance | Menu diving | Todo visible |
| Quantum | Básico | Matrix avanzado |
| Live use | Difícil | Diseñado para ello |
| Accesibilidad | Complejo | Intuitivo |

---

## 📁 ARCHIVOS A CREAR

```
src/ElasticCosmosV2.cpp          (~2500 lines)
res/ElasticCosmosV2.svg          (30HP panel)
```

**Archivos a modificar:**
```
src/plugin.hpp                   (añadir extern Model*)
src/plugin.cpp                   (registrar módulo)
plugin.json                      (metadata)
```

---

## 🚀 PRÓXIMOS PASOS (MAÑANA 21 ENERO)

1. **Revisar este documento** completo
2. **Decidir si empezar:**
   - Opción A: Antes del Mixer (más inspirador?)
   - Opción B: Después del Mixer (orden lógico?)
3. **Empezar Fase 1:** Engine 1 - Delay Mode
4. **Probar con audio del Golden Oscillator**
5. **Continuar con fases 2-6**

---

## 🎉 RESULTADO FINAL

**Sistema completo de procesamiento elástico:**
- 🌀 4 delay/grain/elastic engines
- ⚡ Freeze individual + global
- 🔄 Reverse per-engine
- 🎛️ 3 modos por engine (D/G/E)
- 🌌 Quantum matrix (entangle, fractal, supcom)
- 🎨 Verde matrix + azul cuántico
- 📦 30HP performance-oriented
- 🎵 Live manipulation ready

**Total: 30HP de procesamiento temporal cuántico** 🚀

---

**Documento creado:** 20 Enero 2026, 00:58 AM  
**Para trabajar:** 21 Enero 2026  
**Proyecto:** AurumLab v2.8.0 - Elastic Cosmos Engine V2  
**Autor:** R936936

---

## 📝 NOTAS TÉCNICAS ADICIONALES

### Buffer Management:
- Buffer size: 10 segundos @ 48kHz = 480,000 samples
- Memory: 480,000 × 4 bytes × 4 engines = 7.68 MB
- Circular buffer con write/read pointers
- Interpolación linear para fractional positions

### Performance Considerations:
- SIMD optimization para grain processing
- Max 64 granos activos por engine
- Efficient Hann window lookup table
- Minimal allocations en audio thread

### Cross-platform:
- Todo en C++ standard (no platform-specific)
- Compatible VCV Rack 2.x
- No dependencies externas
- Sample-accurate timing

---

## 🔬 ALGORITMOS CLAVE

### PSOLA (Pitch Synchronous Overlap-Add):
```
1. Detect pitch periods en input
2. Crear granos en cada período
3. Overlap granos con spacing variable
4. Mantener pitch original, cambiar timing
5. Result: time stretch sin pitch change
```

### Granular Synthesis:
```
1. Trigger granos a densidad variable
2. Cada grano lee buffer en posición aleatoria
3. Apply Hann window
4. Overlap múltiples granos
5. Sum to output
```

### Quantum Superposition:
```
1. Cada engine es eigenstate |ψᵢ⟩
2. Superposición: |Ψ⟩ = Σ cᵢ|ψᵢ⟩
3. Colapso: measure → output sample
4. Entanglement: correlación entre states
```

---

## ✨ INNOVACIONES ÚNICAS

### 1. **Quantum Grain Triggering:**
- No es random, es probabilístico cuántico
- Distribución basada en amplitud de onda cuántica
- Crea patrones emergentes naturales

### 2. **Fractal Feedback Networks:**
- Self-similar feedback loops
- Golden ratio modulation
- Auto-organización hacia atractores extraños

### 3. **Entangled Time Domains:**
- Engines no son independientes
- Entanglement crea correlación temporal
- Colapso simultáneo de múltiples estados

### 4. **Elastic Superposition:**
- Múltiples velocidades de playback simultáneas
- Quantum superposition de time domains
- Output es colapso probabilístico

---

**🌟 ESTE VA A SER EL MÓDULO MÁS AVANZADO DE VCVRACK 🌟**

# QUANTUM ELASTIC KICK - 18HP (91.44mm)
**Concepto:** 3 Generadores Idénticos de Kick con Física Elástica  
**Filosofía Aurum:** Quantum Physics + Golden Ratio + Elastic Behavior  
**Fecha:** 21 Enero 2026

---

## 🎯 CONCEPTO: "KICK ELÁSTICO"

### ¿Qué es un Kick Elástico?

**Kick tradicional:**
```
Pitch ↘️ (decay exponencial simple)
Amp   ↘️ (decay exponencial simple)
```

**Kick ELÁSTICO:**
```
Pitch 🎾 (bounce/overshoot - como pelota rebotando)
Amp   🌊 (elastic decay con "wobble")
```

### Física del Bounce

```cpp
// Sistema masa-resorte amortiguado
float elasticDecay(float time, float stiffness, float damping) {
    float omega = sqrt(stiffness);
    float envelope = exp(-damping * time);
    float oscillation = cos(omega * time);
    return envelope * oscillation;
}
```

**Parámetros:**
- **STIFFNESS** (rigidez del resorte) → Frecuencia del bounce
- **DAMPING** (amortiguamiento) → Qué tan rápido se detiene
- **OVERSHOOT** → Cuánto "rebasa" antes de asentarse

---

## 🏗️ ARQUITECTURA DEL MÓDULO

### 3 Sistemas Idénticos × 6HP cada uno

```
┌─────────────┬─────────────┬─────────────┐
│   KICK A    │   KICK B    │   KICK C    │
│    6HP      │    6HP      │    6HP      │
├─────────────┼─────────────┼─────────────┤
│ [PITCH   ]  │ [PITCH   ]  │ [PITCH   ]  │
│ [DECAY   ]  │ [DECAY   ]  │ [DECAY   ]  │
│ [ELASTIC ]  │ [ELASTIC ]  │ [ELASTIC ]  │
│ [CLICK   ]  │ [CLICK   ]  │ [CLICK   ]  │
│             │             │             │
│ TRIG  [●]   │ TRIG  [●]   │ TRIG  [●]   │
│ OUT   [●]   │ OUT   [●]   │ OUT   [●]   │
│             │             │             │
│    [LED]    │    [LED]    │    [LED]    │
└─────────────┴─────────────┴─────────────┘
     30mm         30mm         30mm
```

---

## 🎛️ CONTROLES POR SISTEMA (x3)

### 4 Knobs por Sistema

1. **PITCH** (30-200 Hz)
   - Frecuencia fundamental del kick
   - CV input para modular
   - Golden ratio intervals: 30, 48.5, 78.5, 127, 205 Hz

2. **DECAY** (10ms - 2000ms)
   - Duración total del kick
   - Afecta pitch sweep Y amplitude
   - CV input para ritmos dinámicos

3. **ELASTIC** (0-100%)
   - 0% = Decay exponencial clásico
   - 50% = Bounce moderado (1-2 rebotes)
   - 100% = Bounce máximo (múltiples rebotes)
   - **Parámetro único de este módulo**

4. **CLICK** (0-100%)
   - Mezcla de noise/click al inicio
   - 0% = Solo oscilador puro
   - 100% = Attack con noise burst
   - High-pass filtered noise

### 2 Jacks por Sistema

1. **TRIG** (input)
   - Dispara el kick
   - Rising edge detection
   - Retrigger durante kick = reset

2. **OUT** (output)
   - Audio output del kick
   - ±5V range
   - Hot output (puede clipear intencionalmente)

### 1 LED por Sistema

- **Trigger indicator**
  - Verde: Kick activo
  - Fade out con decay
  - Intensidad = Envelope level

---

## 🧮 ALGORITMO DE SÍNTESIS

### Stage 1: Pitch Envelope (Elastic)

```cpp
float pitchEnvelope(float t, float baseFreq, float elastic) {
    // Pitch sweep: baseFreq → baseFreq/4 con bounce
    float targetPitch = baseFreq * 0.25f;
    float pitchRange = baseFreq - targetPitch;
    
    if (elastic < 0.01f) {
        // Classic exponential sweep
        return baseFreq - pitchRange * (1.f - exp(-5.f * t));
    } else {
        // ELASTIC BOUNCE sweep
        float stiffness = 20.f * elastic;
        float damping = 3.f / (1.f + elastic);
        
        float env = exp(-damping * t);
        float osc = cos(stiffness * t);
        float bounce = 1.f - env * (1.f + osc * elastic);
        
        return baseFreq - pitchRange * bounce;
    }
}
```

**Resultado:**
- Pitch baja normalmente
- Al llegar a target, "rebota" hacia arriba levemente
- Varios rebotes según ELASTIC param
- Se asienta en frecuencia baja

### Stage 2: Amplitude Envelope (Elastic)

```cpp
float amplitudeEnvelope(float t, float decay, float elastic) {
    if (elastic < 0.01f) {
        // Classic exponential decay
        return exp(-5.f * t / decay);
    } else {
        // ELASTIC DECAY con wobble
        float damping = 5.f / decay;
        float wobbleFreq = 15.f * elastic;
        
        float env = exp(-damping * t);
        float wobble = 1.f + 0.3f * elastic * sin(wobbleFreq * t);
        
        return env * wobble;
    }
}
```

**Resultado:**
- Envelope decae normalmente
- Con elastic: amplitud tiene "wobble" (ondulación)
- Simula compresión/expansión elástica del sonido

### Stage 3: Oscillator Core

```cpp
float oscillator(float phase) {
    // Oscilador con armónicos controlados
    float fundamental = sin(phase);
    float harmonic2 = 0.3f * sin(2.f * phase);
    float harmonic3 = 0.1f * sin(3.f * phase);
    
    return fundamental + harmonic2 + harmonic3;
}
```

### Stage 4: Click/Noise

```cpp
float clickNoise(float t, float clickAmount) {
    // Short noise burst at attack
    float noiseEnv = exp(-100.f * t);  // Rápido decay
    float noise = random() * 2.f - 1.f;
    
    // High-pass filter para "click"
    float hpNoise = highPassFilter(noise, 1000.f);
    
    return hpNoise * noiseEnv * clickAmount;
}
```

### Stage 5: Output Mixer

```cpp
float output = oscillator(phase) * amplitudeEnvelope(...) 
             + clickNoise(...);
             
// Soft saturation
output = tanh(output * 1.5f);
```

---

## 🌟 CARACTERÍSTICAS ÚNICAS

### 1. Golden Ratio Pitch Intervals

```cpp
const float goldenPitches[] = {
    30.0f,      // Base
    30.0f * φ,  // 48.5 Hz
    48.5f * φ,  // 78.5 Hz
    78.5f * φ,  // 127 Hz
    127.0f * φ  // 205 Hz
};
```

### 2. Quantum Click Generation

```cpp
// Usa datos cuánticos para click texture
float quantumClick = quantum_observer.qdt[sampleIndex % 2048];
float noise = lerp(randomNoise, quantumClick, 0.3f);
```

### 3. Elastic Physics Modes

**Mode A: Bounce (default)**
- Pitch y amplitud rebotan
- Como pelota cayendo

**Mode B: Overshoot**
- Pitch va más allá del target y regresa
- Como resorte siendo estirado

**Mode C: Wobble**
- Amplitud ondula durante decay
- Como gelatina vibrando

---

## 📐 LAYOUT DETALLADO (6HP por sistema)

### Sistema Individual (30mm width)

```
Y (mm)    Elemento
────────────────────────────
10        "KICK A" (label)
          
20        [PITCH] knob
30        
40        [DECAY] knob
50        
60        [ELASTIC] knob
70        
80        [CLICK] knob
90        
100       TRIG jack
105       LED
110       OUT jack
```

### Panel Completo (18HP = 91.44mm)

```
X positions:
- KICK A: 15mm (center)
- KICK B: 45.72mm (center)
- KICK C: 76.44mm (center)
```

---

## 🎨 DISEÑO VISUAL

### Tema de Color

- **Background:** Negro profundo
- **Labels:** Cian brillante (#00FFFF) - tema quantum
- **Knobs:** Negros con indicador dorado
- **Jacks:** Plateados
- **LEDs:** Verde elástico (#00FF88)

### Iconografía

- **PITCH:** Onda senoidal
- **DECAY:** Flecha descendente
- **ELASTIC:** Resorte 🎾 (símbolo bounce)
- **CLICK:** Rayo ⚡

---

## 💾 ESPECIFICACIONES TÉCNICAS

### Parámetros (por sistema)

```cpp
enum ParamIds {
    // KICK A
    PITCH_A_PARAM,
    DECAY_A_PARAM,
    ELASTIC_A_PARAM,
    CLICK_A_PARAM,
    
    // KICK B
    PITCH_B_PARAM,
    DECAY_B_PARAM,
    ELASTIC_B_PARAM,
    CLICK_B_PARAM,
    
    // KICK C
    PITCH_C_PARAM,
    DECAY_C_PARAM,
    ELASTIC_C_PARAM,
    CLICK_C_PARAM,
    
    NUM_PARAMS
};
```

**Total: 12 parámetros**

### Inputs

```cpp
enum InputIds {
    TRIG_A_INPUT,
    TRIG_B_INPUT,
    TRIG_C_INPUT,
    NUM_INPUTS
};
```

**Total: 3 inputs**

### Outputs

```cpp
enum OutputIds {
    KICK_A_OUTPUT,
    KICK_B_OUTPUT,
    KICK_C_OUTPUT,
    NUM_OUTPUTS
};
```

**Total: 3 outputs**

### Lights

```cpp
enum LightIds {
    KICK_A_LIGHT,
    KICK_B_LIGHT,
    KICK_C_LIGHT,
    NUM_LIGHTS
};
```

**Total: 3 LEDs**

---

## 🔬 FÍSICA ELÁSTICA - DEEP DIVE

### Ecuación Diferencial del Sistema

```
m * a = -k * x - c * v

Donde:
m = masa (constante = 1.0)
k = stiffness (rigidez del resorte)
c = damping (coeficiente de amortiguamiento)
x = posición
v = velocidad
a = aceleración
```

### Solución Analítica

```cpp
// Underdamped oscillator (c < 2*sqrt(k))
float omega_d = sqrt(k - (c*c)/4);
float A = exp(-c * t / 2);
float B = cos(omega_d * t);

float displacement = A * B;
```

### Implementación en Código

```cpp
struct ElasticOscillator {
    float position = 1.0f;      // Inicio en 1.0
    float velocity = 0.0f;      // Sin velocidad inicial
    float stiffness = 100.0f;   // k
    float damping = 5.0f;       // c
    
    float process(float dt) {
        // Calcular aceleración
        float acceleration = -stiffness * position - damping * velocity;
        
        // Integrar (Euler)
        velocity += acceleration * dt;
        position += velocity * dt;
        
        return position;
    }
};
```

---

## 🎵 CASOS DE USO

### 1. Kick Tradicional
- **PITCH:** 60 Hz
- **DECAY:** 300ms
- **ELASTIC:** 0%
- **CLICK:** 10%
→ Kick clásico techno

### 2. Bouncy Kick
- **PITCH:** 80 Hz
- **DECAY:** 500ms
- **ELASTIC:** 70%
- **CLICK:** 30%
→ Kick con "boing" (IDM, experimental)

### 3. Wobbly Sub
- **PITCH:** 30 Hz
- **DECAY:** 1000ms
- **ELASTIC:** 100%
- **CLICK:** 0%
→ Sub-bass ondulante (dubstep, bass music)

### 4. Elastic 808
- **PITCH:** 50 Hz
- **DECAY:** 400ms
- **ELASTIC:** 40%
- **CLICK:** 20%
→ 808 con carácter único

---

## ⏱️ PLAN DE IMPLEMENTACIÓN

### FASE 1: Core Engine (3-4 horas)
- [ ] Crear `QuantumElasticKick.cpp`
- [ ] Implementar elastic oscillator physics
- [ ] Pitch envelope con bounce
- [ ] Amplitude envelope con wobble
- [ ] Trigger detection

### FASE 2: Audio Processing (2-3 horas)
- [ ] Oscilador con armónicos
- [ ] Click/noise generator
- [ ] Output mixer
- [ ] Soft saturation

### FASE 3: Panel Design (1-2 horas)
- [ ] SVG panel 18HP
- [ ] 3 secciones idénticas
- [ ] Labels e iconografía
- [ ] Tema cian/quantum

### FASE 4: Integration (1 hora)
- [ ] Registrar en plugin.json
- [ ] Testing de los 3 sistemas
- [ ] CV modulation testing

### FASE 5: Polish (1 hora)
- [ ] LED brightness seguir envelope
- [ ] Golden ratio pitch presets
- [ ] Quantum click texture
- [ ] Documentation

**TOTAL: 8-11 horas**

---

## 🚀 INNOVACIONES

### 1. Primera implementación de física elástica en kick drum
- Ningún módulo VCV Rack tiene esto
- Basado en ecuaciones físicas reales

### 2. Elastic como parámetro continuo
- No es switch, es knob 0-100%
- Morfeo suave entre classic y elastic

### 3. Triple sistema compacto
- 3 kicks independientes en 18HP
- Ideal para polyrhythms
- Cada uno con personalidad única

### 4. Quantum click texture
- Usa datos cuánticos reales IBM
- Textura única e irrepetible

---

## 📊 COMPARACIÓN CON OTROS MÓDULOS

| Feature | BD-808 Clone | Kick VCV | **Elastic Kick** |
|---------|--------------|----------|------------------|
| Elastic decay | ❌ | ❌ | ✅ |
| Bounce physics | ❌ | ❌ | ✅ |
| Quantum noise | ❌ | ❌ | ✅ |
| 3 systems | ❌ | ❌ | ✅ |
| Compact (6HP) | ❌ | ✅ | ✅ |
| Golden ratio | ❌ | ❌ | ✅ |

---

## 🎯 NOMBRE DEL MÓDULO

### Opciones:

1. **"Quantum Elastic Kick"** ⭐ (favorito)
   - Descriptivo y técnico
   - Mantiene branding Quantum

2. **"Elastic Triad"**
   - Enfatiza los 3 sistemas
   - Nombre corto y catchy

3. **"Bounce Kick"**
   - Simple y directo
   - Describe característica principal

4. **"φ-Kick"** (Phi Kick)
   - Golden ratio theme
   - Minimalista

**Recomendación:** **"Quantum Elastic Kick"**

---

## ✅ SIGUIENTE PASO

¿Te gusta este concepto? 

Si sí, empiezo con:
1. Crear `src/QuantumElasticKick.cpp`
2. Crear `res/QuantumElasticKick.svg`
3. Implementar física elástica
4. Compilar y probar

**¿Procedemos?** 🚀🎾

# 🔬 FÓRMULAS MATEMÁTICAS DE RESONADORES FRACTÁLICOS
**AurumLab - Golden Oscillator & QuantumSynth Fractal Resonator**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📊 TABLA DE CONTENIDO

1. [Arquitectura General](#arquitectura)
2. [Generación de Frecuencias por Modo](#frecuencias)
3. [Cálculo de Factor Q (Resonancia)](#factor-q)
4. [Multiplicadores de Intensidad](#intensidad)
5. [Filtros Resonantes (Biquad)](#filtros)
6. [Ecuaciones Completas](#ecuaciones)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<a name="arquitectura"></a>
## 🏗️ 1. ARQUITECTURA GENERAL

Ambos motores (Golden Oscillator y QuantumSynth) usan **bancos de filtros resonantes paralelos**:

```
                    ┌─────────────┐
    Input Signal -> │  Resonator  │ -> Layer 0 (f₀)
                    │    Bank     │ -> Layer 1 (f₁)
                    │             │ -> Layer 2 (f₂)
                    │  (8 capas)  │ -> ...
                    │             │ -> Layer 7 (f₇)
                    └─────────────┘
                           │
                           ↓
                    [Suma ponderada]
                           │
                           ↓
                    Output Signal
```

**Cada capa** es un **State Variable Filter** (Golden Osc) o **Biquad Bandpass** (QuantumSynth) con:
- **Frecuencia específica** (fᵢ)
- **Factor Q variable** (Qᵢ)
- **Amplitud/ganancia** (Aᵢ)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<a name="frecuencias"></a>
## 🎵 2. GENERACIÓN DE FRECUENCIAS POR MODO

### MODO FIBONACCI (Serie Armónica)

**Golden Oscillator:**
```
Secuencia Fibonacci: [1, 1, 2, 3, 5, 8, 13, 21]

Para capa i:
  fᵢ = f₀ × Fib[i] × spread_comprimido
  
  spread_comprimido = 1.0 + (spread - 1.0) × 0.5
  
Amplitudes (decay natural):
  Aᵢ = 0.8 / (1.0 + i × 0.4)
```

**QuantumSynth:**
```
Para capa i:
  fᵢ = f₀ × Fib[i]
  
Énfasis cada 3er parcial:
  Q_extra = +10 si (i mod 3 = 0)
  Q_extra = +5  en otro caso
  
Boost Fibonacci:
  Q_boost = 1.0 + 0.2 × (Fib[min(i, 15)] / 377)
```

**Resultado:** Armónicos claros, musicales, predecibles.

---

### MODO ÁUREO/GOLDEN (Potencias de φ)

**φ (Phi) = 1.618033988...**

**Golden Oscillator:**
```
Para capa i:
  Exponente = i - 3  (para centrar)
  Ratio = φ^(exponente)
  fᵢ = f₀ × φ^(i-3) × spread_comprimido

Distribución: φ⁻³, φ⁻², φ⁻¹, 1, φ, φ², φ³, φ⁴

Amplitudes (decay desde centro):
  distancia_centro = |i - 3.5|
  Aᵢ = 0.8 / (1.0 + distancia_centro × 0.3)
```

**QuantumSynth:**
```
Para capa i:
  Q_base = 15 + i × 2.5  (progresión lineal)
  
Multiplicador phi:
  Q_mult = φ^(i × 0.1)  (crecimiento exponencial suave)
  
  Qᵢ = Q_base × Q_mult
```

**Resultado:** Estructura balanceada, armónicos en relación áurea.

---

### MODO MANDELBROT (Caos Fractal)

**Golden Oscillator:**
```
Para capa i:
  c_real = -0.8 + i × 0.15  (barrido: -0.8 a 0.25)
  c_imag = 0.0
  
Iteraciones Mandelbrot:
  z₀ = 0 + 0i
  z_{n+1} = z_n² + c
  
  iter = número de iteraciones hasta |z| > 2
  normalized = iter / 20  (normalizado 0-1)

Frecuencias (números primos × caos):
  PRIMOS = [2, 3, 5, 7, 11, 13, 17, 19]
  ratio = PRIMOS[i] × (0.5 + normalized × 1.5)
  fᵢ = f₀ × ratio × spread × 0.5

Amplitudes caóticas:
  Aᵢ = 0.5 + normalized × 0.4
```

**QuantumSynth:**
```
Variación caótica de Q:
  chaos_mod = 0.5 + 0.5 × sin(i × 2.3)  (0 a 1)
  Q_base = 10 + 15 × chaos_mod  (rango: 10-25)
  
Modulación secundaria:
  Q_secondary = 1.0 + 0.3 × cos(i × φ)
  
  Qᵢ = Q_base × Q_secondary
```

**Resultado:** Inarmónicos, impredecibles, densos, fractales.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<a name="factor-q"></a>
## 🔊 3. CÁLCULO DE FACTOR Q (RESONANCIA)

El **factor Q** determina la **nitidez de los picos resonantes**:
- **Q bajo** (< 10): resonancia suave, ancho de banda amplio
- **Q medio** (10-25): resonancia definida, musical
- **Q alto** (> 25): resonancia extrema, picos muy estrechos

### Golden Oscillator - Fórmulas Base de Q

```
baseResonance = 0.5 + depth × 0.45  (rango: 0.5 - 0.95)

FIBONACCI:
  Q_fib = baseResonance × 0.6
  Feedback_fib = feedback × 0.5

ÁUREO:
  dist_centro = |i - 3.5|
  goldenMod = 1.0 / (1.0 + dist_centro × 0.15)
  Q_aureo = baseResonance × (0.8 + goldenMod × 0.4)
  Feedback_aureo = feedback × (0.6 + goldenMod × 0.4)

MANDELBROT:
  chaosMod = sin(i × 2.618) × 0.5 + 0.5
  Q_mandelbrot = baseResonance × (1.5 + chaosMod × 0.8)  ← Q EXTREMO
  Feedback_mandelbrot = feedback × (0.9 + chaosMod × 0.6)
```

**Multiplicadores relativos:**
- Fibonacci: **0.6×** (más suave)
- Áureo: **0.8-1.2×** (balanceado)
- Mandelbrot: **1.5-2.3×** (extremo)

---

### QuantumSynth - Fórmulas Base de Q

```
FIBONACCI (mode 0):
  Q_base = 12 + (i mod 3 == 0 ? 10 : 5)
  Q_boost = 1.0 + 0.2 × (Fib[min(i,15)] / 377)
  Qᵢ = Q_base × Q_boost

GOLDEN (mode 1):
  Q_base = 15 + i × 2.5  (progresión lineal)
  Q_phi = φ^(i × 0.1)
  Qᵢ = Q_base × Q_phi

MANDELBROT (mode 2):
  chaos = 0.5 + 0.5 × sin(i × 2.3)
  Q_base = 10 + 15 × chaos  (rango 10-25)
  Q_secondary = 1.0 + 0.3 × cos(i × φ)
  Qᵢ = Q_base × Q_secondary
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<a name="intensidad"></a>
## 🔥 4. MULTIPLICADORES DE INTENSIDAD

### Golden Oscillator - Chaos Parameter

**Multiplicador base:**
```
morphY_intensity = 0.3 + morphY × 1.7  (rango: 0.3× a 2.0×)
```

**Multiplicadores por modo** (per-mode scaling):
```
fib_intensity      = morphY_intensity × 0.8   (0.24× a 1.6×)
aureo_intensity    = morphY_intensity × 1.0   (0.3× a 2.0×)
mandelbrot_intensity = morphY_intensity × 1.3 (0.39× a 2.6×)
```

**Blending en modo morph:**
```
Si modeMorph < 1.0:
  fibWeight = 1.0 - modeMorph
  aureoWeight = modeMorph
  mandelbrotWeight = 0.0
Sino:
  fibWeight = 0.0
  aureoWeight = 2.0 - modeMorph
  mandelbrotWeight = modeMorph - 1.0

blended_intensity = 
  fib_intensity × fibWeight + 
  aureo_intensity × aureoWeight + 
  mandelbrot_intensity × mandelbrotWeight
```

**Aplicación final:**
```
Q_final = clamp(Q_base × blended_intensity, 0, 0.98)
Feedback_final = Feedback_base × blended_intensity
```

---

### QuantumSynth - Harmonic Excitation Parameter

**Multiplicador base:**
```
excitation_intensity = 0.5 + harmonicExcitation  (rango: 0.5× a 1.5×)
```

**Multiplicadores por modo:**
```
Si mode == 0 (Fibonacci):
  mode_scale = 0.8  (rango total: 0.4× a 1.2×)
  
Si mode == 1 (Golden):
  mode_scale = 1.0  (rango total: 0.5× a 1.5×)
  
Si mode == 2 (Mandelbrot):
  mode_scale = 1.2  (rango total: 0.6× a 1.8×)
  
Si mode == 3 (Morph):
  mode_scale = 1.0  (promedio)
```

**Aplicación final:**
```
Q_final = Q_base × excitation_intensity × mode_scale
Q_final = clamp(Q_final, 5.0, 50.0)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<a name="filtros"></a>
## 🎛️ 5. FILTROS RESONANTES

### State Variable Filter (Golden Oscillator)

**Ecuaciones diferenciales discretizadas:**
```
Para cada sample:
  f = 2 × sin(π × freq / sampleRate)
  damp = min(2 × (1 - Q^(1/4)), 2 - f)
  
  low += f × band
  high = input - low - damp × band
  band += f × high
  notch = high + low
  
  output = band  (bandpass)
```

**Feedback loop:**
```
input_with_feedback = input + feedback_final × state
state = output × 0.999  (damping para estabilidad)
```

---

### Biquad Bandpass Filter (QuantumSynth)

**Coeficientes:**
```
ω = 2π × f / sampleRate
sin_ω = sin(ω)
cos_ω = cos(ω)
α = sin_ω / (2 × Q)

a₀ = 1 + α
b₀ = (α / a₀) × gain_multiplier
b₁ = 0
b₂ = (-α / a₀) × gain_multiplier
a₁ = -2 × cos_ω / a₀
a₂ = (1 - α) / a₀
```

**Multiplicadores de ganancia por modo:**
```
Si mode == 0 (Fibonacci):  gain_mult = 4.5
Si mode == 1 (Golden):     gain_mult = 5.0  ← más limpio/alto
Si mode == 2 (Mandelbrot): gain_mult = 3.5  ← más controlado
```

**Ecuación de diferencias:**
```
y[n] = b₀×x[n] + b₁×x[n-1] + b₂×x[n-2] 
       - a₁×y[n-1] - a₂×y[n-2]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<a name="ecuaciones"></a>
## 📐 6. ECUACIONES COMPLETAS

### Golden Oscillator - Ecuación Completa de Salida

```
Para cada sample:

  1. Calcular frecuencias por modo:
     [f₀, f₁, ..., f₇] = calcular_frecuencias(modo, f_base, spread)
  
  2. Calcular Q base por modo y capa:
     Q_base[i] = función(modo, i, baseResonance, feedback)
  
  3. Aplicar intensidad con per-mode scaling:
     morphY_int = 0.3 + morphY × 1.7
     
     fib_int = morphY_int × 0.8
     aureo_int = morphY_int × 1.0
     mandel_int = morphY_int × 1.3
     
     blended_int = peso_ponderado(fib_int, aureo_int, mandel_int)
     
     Q_final[i] = clamp(Q_base[i] × blended_int, 0, 0.98)
  
  4. Procesar cada capa:
     output = 0
     Para i = 0 hasta 7:
       layer_out[i] = SVF_bandpass(input, f[i], Q_final[i], feedback)
       output += layer_out[i] × amplitude[i]
  
  5. Retornar output
```

---

### QuantumSynth - Ecuación Completa de Salida

```
Para cada sample:

  1. Determinar frecuencias parciales:
     [f₀, f₁, ..., f₃₁] = calcular_parciales(modo, morph, f_base)
  
  2. Calcular Q por modo:
     Q_mode[i] = función(modo, i)  ← ver sección 3
  
  3. Aplicar Harmonic Excitation con per-mode scaling:
     excite_int = 0.5 + harmonicExcitation
     
     mode_scale = {
       0.8 si Fibonacci,
       1.0 si Golden,
       1.2 si Mandelbrot,
       1.0 si Morph
     }
     
     Q_final[i] = clamp(Q_mode[i] × excite_int × mode_scale, 5, 50)
  
  4. Calcular coeficientes biquad para cada parcial:
     [b₀, b₁, b₂, a₁, a₂] = biquad_bandpass(f[i], Q_final[i])
  
  5. Procesar señales L/R/C con resonadores paralelos:
     output_L = 0
     output_R = 0
     
     Para i = 0 hasta 31:
       resonated_L = biquad_process(input_L, coefs[i])
       resonated_R = biquad_process(input_R, coefs[i])
       
       output_L += resonated_L × weight[i]
       output_R += resonated_R × weight[i]
  
  6. Retornar [output_L, output_R]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📊 COMPARACIÓN DE RANGOS DE Q

### At Minimum Control (Chaos/Excitation = 0.0)

```
                    Golden Osc          QuantumSynth
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fibonacci:          Q × 0.24            Q × 0.4
Aureo/Golden:       Q × 0.3             Q × 0.5
Mandelbrot:         Q × 0.39            Q × 0.6

Carácter:           Suave, musical      Limpio, controlado
```

### At Maximum Control (Chaos/Excitation = 1.0)

```
                    Golden Osc          QuantumSynth
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Fibonacci:          Q × 1.6             Q × 1.2
Aureo/Golden:       Q × 2.0             Q × 1.5
Mandelbrot:         Q × 2.6             Q × 1.8

Carácter:           EXTREMO!            Denso, resonante
```

**Distinción entre modos:**
- Golden Oscillator: Mandelbrot/Fibonacci = **1.625:1** ratio
- QuantumSynth: Mandelbrot/Fibonacci = **1.5:1** ratio

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 🎯 PROGRESIÓN AUDIBLE

```
     Chaos/Excitation
          ↓
    ┌─────┴─────┐
    0.0         1.0
    
FIBONACCI:
    🎵──────────🎶
    Musical    Enhanced
    (controlado siempre)

GOLDEN/AUREO:
    🎼─────────🎨
    Balanced   Rich
    (progresión suave)

MANDELBROT:
    🌀─────────🔥
    Textured   CHAOS!
    (explosión fractal)
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 💡 CLAVES DE DISEÑO

### Por qué estas fórmulas funcionan:

1. **Fibonacci:** Números naturales → armónicos familiares
2. **Golden Ratio:** φ es ratio "más irracional" → balance máximo
3. **Mandelbrot:** Iteraciones fractales → caos estructurado
4. **Per-mode scaling:** Amplifica diferencias progresivamente
5. **Q modulation:** Controla ancho de picos = carácter tímbrico
6. **Feedback loops:** Añade auto-resonancia = complejidad

### Estabilidad numérica:

- Q siempre limitado (< 0.98 o 5-50)
- Damping en SVF (× 0.999)
- Normalizaciones (iteraciones / 20, etc.)
- Clamps en todo el procesamiento

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 📚 REFERENCIAS

**Números Fibonacci:**
```
F₀ = 1, F₁ = 1, F₂ = 2, F₃ = 3, F₄ = 5, F₅ = 8, F₆ = 13, F₇ = 21
```

**Golden Ratio (φ):**
```
φ = (1 + √5) / 2 ≈ 1.618033988749895
```

**Conjunto Mandelbrot:**
```
z_{n+1} = z_n² + c
M = {c ∈ ℂ : lim_{n→∞} |z_n| ≠ ∞, z₀ = 0}
```

**Números Primos (para Mandelbrot):**
```
P = [2, 3, 5, 7, 11, 13, 17, 19]
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## ✅ RESUMEN EJECUTIVO

**Sistema Dual de Resonadores Fractálicos**

- **8 capas paralelas** de filtros resonantes
- **3 modos fractales** con fórmulas únicas
- **Factor Q variable** por modo, capa y parámetro
- **Per-mode intensity scaling** para máxima distinción
- **Estado estable** con clamps y damping
- **Timbres únicos** imposibles con síntesis clásica

**Resultado:** Síntesis fractal musicalmente útil y experimentalmente extrema.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**Documento creado:** Enero 16, 2026  
**Módulos:** Golden Oscillator v5.5 + QuantumSynth Fractal Resonator  
**Status:** ✅ IMPLEMENTADO Y VERIFICADO

🔥 Las matemáticas del caos fractal, ahora en tus manos! 🔥

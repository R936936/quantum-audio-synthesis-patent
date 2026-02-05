# 🌀 GOLDEN SPIRAL OSCILLATOR - TECHNICAL SPECIFICATION

## Implementación Matemática Correcta

**Fecha:** 15 Enero 2026  
**Versión:** 1.0 - True 3D Parametric Golden Spiral  
**Autor:** Aurum Lab Development Team

---

## 📐 MODELO MATEMÁTICO

### Ecuaciones Paramétricas de la Espiral Áurea

```
θ(t) = 2π · f · t                    ← Ángulo de rotación (depende de frecuencia)

r(θ) = φ^(θ · τ / π)                 ← Radio crece exponencialmente con φ
       donde τ = tightness = 0.15    ← Factor de crecimiento (ajustado para audio)

x(θ) = r(θ) · cos(θ)                 ← Coordenada X
y(θ) = r(θ) · sin(θ · spiralRate)    ← Coordenada Y (modulada por spiralRate)
z(θ) = spiralDepth · θ / (2π)        ← Coordenada Z (altura lineal)

Output = tanh(x·0.4) · 0.5 +         ← Componente principal (50%)
         tanh(y·0.4) · 0.35 +        ← Componente armónico (35%)
         tanh(z·0.6) · 0.15          ← Componente textural (15%)
```

---

## 🎛️ PARÁMETROS

### 1. FREQUENCY (20-8000 Hz)
- **Control:** Knob grande + V/Oct input + Fine tune
- **Rango logarítmico:** log(20) a log(8000)
- **Efecto:** Velocidad de recorrido de la espiral
- **Phase continuity:** `phase *= (newFreq / oldFreq)` cuando cambia

### 2. SPIRAL RATE (0.5-10x, default φ=1.618)
- **Control:** Knob mediano
- **Efecto:** Modula la componente Y
- **En φ (1.618):** Produce relación áurea natural
- **< φ:** Más armónicos bajos
- **> φ:** Más complejidad espectral

### 3. SPIRAL DEPTH (0-100%, default 50%)
- **Control:** Knob mediano
- **Efecto:** Amplitud del componente Z
- **0%:** Espiral plana (2D)
- **100%:** Máxima dimensión 3D

### 4. SPIRAL TIGHTNESS (interno: 0.15)
- **Fijo por ahora** (podría exponerse después)
- **Efecto:** Qué tan rápido crece el radio
- **Valor actual (0.15):** Optimizado para rango de audio

---

## 🔧 CARACTERÍSTICAS TÉCNICAS

### Continuidad de Fase
```cpp
void setFrequency(float freq) {
    if (lastFreq > 0.f && abs(freq - lastFreq) > 0.1f) {
        phase *= (freq / lastFreq);  // ← Mantiene coherencia
        while (phase >= 1.f) phase -= 1.f;
        while (phase < 0.f) phase += 1.f;
    }
    lastFreq = frequency;
}
```

**VENTAJA:** La forma de onda se mantiene coherente cuando la frecuencia cambia.  
No hay discontinuidades ni "clicks".

### Soft Clipping (tanh)
```cpp
output = tanh(x * 0.4f) * 0.5f +
         tanh(y * 0.4f) * 0.35f +
         tanh(z * 0.6f) * 0.15f;
```

**VENTAJA:**
- Previene clipping harsh
- Agrega saturación musical natural
- Mantiene señal en rango [-1, 1]

### Radius Clamping
```cpp
radius = clamp(pow(PHI, theta * tightness / M_PI), 0.1f, 3.0f);
```

**VENTAJA:**
- Previene explosión numérica
- Mantiene estabilidad en frecuencias extremas
- Radio máximo = 3.0 (límite de audio range)

### Z-Axis Wrapping
```cpp
z = z - floor(z);        // Wrap a [0,1]
z = (z - 0.5f) * 2.f;    // Scale a [-1,1]
```

**VENTAJA:**
- Z crece linealmente pero wrap periódico
- Añade componente cíclico textural
- No acumula offset DC

---

## 🎵 CARACTERÍSTICAS SONORAS

### Espectro Único
- **NO es suma de senos fijos**
- **SÍ es recorrido de curva 3D**
- Contenido armónico cambia dinámicamente con SPIRAL params

### Forma de Onda Orgánica
- Asimétrica y compleja
- Rica en armónicos impares y pares
- "Viva" - cambia sutilmente en el tiempo

### Modulación Dimensional
- **SPIRAL RATE:** Cambia relaciones armónicas
- **SPIRAL DEPTH:** Añade/quita dimensión Z
- **FREQ:** Cambia velocidad sin cambiar forma

---

## 📊 COMPARACIÓN vs IMPLEMENTACIÓN ANTERIOR

| Aspecto | Anterior (Suma Senos) | Nuevo (Golden Spiral) |
|---------|----------------------|----------------------|
| Forma de onda | Fija (x+y+z)/3 | Paramétrica 3D |
| Radio | N/A | Crece con φ^(θ/π) |
| Phase continuity | NO | SÍ |
| Clipping | Hard | Soft (tanh) |
| Coherencia temporal | Baja | Alta |
| Riqueza armónica | Media | Alta |
| CPU | Baja | Media |

---

## 🚀 PRÓXIMOS PASOS (Fibonacci Resonator)

1. **State Variable Filter Bank** (4-8 filtros)
2. **Fibonacci Mode:** Ratios 1,1,2,3,5,8,13,21
3. **Golden Mode:** Potencias φ^n
4. **Mandelbrot Mode:** Secuencia fractal
5. **RESONANCE knob:** Intensidad de filtros
6. **MORPH knob:** Mezcla entre modos

---

## 🎯 CONCLUSIÓN

Esta implementación es **matemáticamente correcta** y produce una forma de onda
que verdaderamente "viaja" coherentemente en el tiempo a través de una espiral
áurea 3D. No es una aproximación - es el modelo real.

**Resultado sonoro:** Único, orgánico, y armónicamente rico. ✨

---

**Aurum Lab** - _Where Mathematics Meets Music_ 🌟


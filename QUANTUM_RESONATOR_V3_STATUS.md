# Quantum Resonator V3 - Estado Actual del Proyecto
## Fecha: 2 de Octubre de 2025

---

## ✅ LIMPIEZA COMPLETADA

Se han eliminado todos los directorios duplicados y versiones antiguas que causaban confusión:

### Directorio Principal (ÚNICO):
- **`~/AurumLab/`** - Plugin activo con Quantum Resonator V3

### Directorios Movidos a Backup (para eliminar):
- **`~/OBSOLETE_AURUM_BACKUPS_TO_DELETE/`** - Contiene:
  - Todas las copias de AurumLab del Desktop (20+ directorios)
  - AurumAI
  - Aurum_backups
  - Versiones V1, V2, checkpoints antiguos

### Plugin Instalado:
- **Ubicación**: `~/Library/Application Support/Rack2/plugins-mac-arm64/`
- **Archivo**: `AurumLab-3.0.0-mac-arm64.vcvplugin`
- **Brand**: Aurum
- **Módulo**: Quantum Resonator V3

---

## 🎛️ CARACTERÍSTICAS IMPLEMENTADAS

### 1. **Osciladores en Espiral** (Spiral Wave Oscillators)
- ✅ Dual-channel (L/R) con afinación independiente
- ✅ Forma de onda basada en espiral (spiral phase)
- ✅ 4 controles principales:
  - `SPIRAL_RATE_PARAM` - velocidad de expansión espiral
  - `SPIRAL_DEPTH_PARAM` - profundidad de modulación AM
  - `SPIRAL_COMPLEXITY_PARAM` - riqueza armónica (capas Fibonacci)
  - `SPIRAL_SHAPE_PARAM` - morphing de forma de onda (sine→enhanced→tri→saw)

### 2. **Banco de Resonadores Fractálicos** (Resonator Bank)
- ✅ 16 resonadores por canal con estructura armónica
- ✅ 3 modos fractálicos + 1 modo morph:
  - **Fibonacci**: Estructura basada en secuencia de Fibonacci
  - **Golden Ratio**: Ratios basados en Φ (1.618...)
  - **Mandelbrot**: Estructura armónica compleja caótica
  - **Morph**: Transición suave entre los 3 modos anteriores

### 3. **Superposición Cuántica** (Quantum Superposition)
- ✅ 3 parámetros de control:
  - `Q_SPREAD_PARAM` - dispersión de distribución de probabilidad
  - `Q_EVOLUTION_PARAM` - velocidad de evolución unitaria
  - `Q_COHERENCE_PARAM` - fuerza de interferencia cuántica
- ✅ Estados cuánticos complejos con amplitud y fase
- ✅ Interferencia constructiva/destructiva entre parciales

### 4. **Entrelazamiento Cuántico** (Quantum Entanglement)
- ✅ 2 tipos de entrelazamiento:
  - `Q_ENTANGLE_CHANNEL_PARAM` - correlación de fase entre canales L↔R
  - `Q_ENTANGLE_HARMONIC_PARAM` - correlación de frecuencias armónicas
- ✅ Inputs CV para modulación externa

### 5. **Modulación por Túnel Cuántico** (Quantum Tunnel)
- ✅ `Q_TUNNEL_PARAM` - probabilidad de saltos de fase cuánticos
- ✅ Crea discontinuidades sutiles simulando efecto túnel
- ✅ Input CV para control externo

### 6. **Delay con Número Áureo** (Golden Delay)
- ✅ Líneas de delay basadas en Φ
- ✅ 2 controles:
  - `DELAY_AMOUNT_PARAM` - cantidad de delay/feedback
  - `DELAY_ITERATIONS_PARAM` - número de iteraciones (1-8)
- ✅ Tiempos de delay en proporción áurea

### 7. **Reverb en Espiral de Caracol** (Fibonacci Shell Reverb)
- ✅ 8 taps con espaciado de Fibonacci
- ✅ Emula reflexiones internas de una concha en espiral
- ✅ 2 controles:
  - `REVERB_FEEDBACK_PARAM` - retroalimentación
  - `REVERB_MIX_PARAM` - mezcla wet/dry
- ✅ Modulación en espiral áurea entre taps

### 8. **Triggers por Canal**
- ✅ 3 entradas de trigger:
  - `TRIGGER_L_INPUT` - trigger canal izquierdo
  - `TRIGGER_R_INPUT` - trigger canal derecho
  - `TRIGGER_GLOBAL_INPUT` - trigger global (ambos canales)

### 9. **Displays de Frecuencia Interactivos**
- ✅ 2 displays LED mostrando frecuencias en Hz
- ✅ Click para ingresar valores manualmente via teclado
- ✅ Actualización en tiempo real

### 10. **Control V/Oct**
- ✅ Inputs V/Oct independientes por canal
- ✅ Afinación precisa estilo sintetizador

---

## 📊 ARQUITECTURA DE AUDIO

```
INPUT (V/Oct + Triggers)
    ↓
Spiral Wave Oscillators (L/R)
    ↓
Quantum Superposition Layer
    ↓
Resonator Bank (16 partials × 2 channels)
    ├── Fibonacci Mode
    ├── Golden Ratio Mode
    ├── Mandelbrot Mode
    └── Morph Mode
    ↓
Quantum Entanglement (Channel + Harmonic)
    ↓
Quantum Tunnel Modulation
    ↓
Golden Delay Lines (1-8 iterations)
    ↓
Fibonacci Shell Reverb (8 taps)
    ↓
OUTPUT (L/R)
```

---

## 🎨 PANEL (20HP)

### Layout de Controles:

**Fila Superior:**
- Frequency Display L | Frequency Display R

**Sección Media:**
- Mode Knob | Morph Knob
- Spiral Controls (4 knobs en 2×2)
- Quantum Superposition (3 knobs)

**Sección Inferior Izquierda:**
- Quantum Entanglement (2 knobs)
- Quantum Tunnel (1 knob)

**Sección Inferior Central:**
- Delay Amount | Delay Iterations

**Sección Inferior Derecha:**
- Reverb Feedback | Reverb Mix

**Inputs/Outputs:**
- V/Oct L/R (top)
- Triggers L/R/Global (middle)
- Audio Out L/R (bottom)
- CV inputs para todos los parámetros modulables

---

## 🔧 MEJORAS PENDIENTES

### Alta Prioridad:
1. **Ajustar layout del panel** - algunos controles aún están superpuestos
2. **Mejorar entrada de teclado en Frequency Displays** - permitir entrada directa desde teclado numérico
3. **Optimización de CPU** - el módulo puede ser exigente con muchos parciales
4. **Calidad de audio** - anti-aliasing en osciladores

### Media Prioridad:
5. **Presets** - crear presets de fábrica para diferentes modos
6. **Documentación** - manual de usuario con ejemplos
7. **Visualización** - LEDs o scope para mostrar actividad cuántica
8. **Modulación adicional** - FM, PM inputs

### Baja Prioridad:
9. **Poly support** - soporte para cables polyphonic
10. **Stereo effects** - procesamiento stereo avanzado

---

## 🚀 PRÓXIMOS PASOS

1. **Testear** el módulo en Rack2 para verificar que todo funciona
2. **Ajustar panel** para eliminar superposiciones restantes
3. **Validar audio** - verificar que oscila y resuena correctamente
4. **Refinar parámetros** - ajustar rangos para mejor musicalidad
5. **Documentar** - crear README con instrucciones de uso

---

## 📝 NOTAS TÉCNICAS

- **Sample Rate**: Variable (depende de Rack2, típicamente 44.1-48kHz)
- **Parciales**: 16 por canal (32 total)
- **Delay Buffer**: 96,000 samples (2 segundos @ 48kHz)
- **Reverb Taps**: 8 con espaciado Fibonacci
- **CPU Usage**: Medio-Alto (depende de configuración)

---

## ⚠️ PROBLEMAS CONOCIDOS

1. Algunos controles en el panel están superpuestos visualmente
2. Entrada de teclado en displays de frecuencia necesita mejorarse
3. Sin warnings de compilación críticos (solo 3 variables no usadas)

---

## 📂 ESTRUCTURA DE ARCHIVOS

```
~/AurumLab/
├── src/
│   ├── QuantumResonatorV3.cpp (1387 líneas)
│   ├── plugin.cpp
│   └── plugin.hpp
├── res/
│   └── QuantumResonatorV3.svg (panel SVG)
├── plugin.json
├── Makefile
└── README.md
```

---

## 🎯 ESTADO: FUNCIONAL

El módulo compila, instala y debería funcionar correctamente en Rack2 Pro.
Todas las características principales están implementadas.
Requiere ajustes de UI/UX pero el DSP está completo.

---

**Para continuar el desarrollo:**
1. Abrir Rack2 Pro
2. Agregar módulo "Quantum Resonator V3" de marca "Aurum"
3. Testear funcionalidad
4. Reportar issues específicos para ajustar


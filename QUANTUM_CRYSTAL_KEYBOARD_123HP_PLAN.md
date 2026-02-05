# QUANTUM CRYSTAL KEYBOARD - 123 HP (624.84mm)

**Fecha:** 21 Enero 2026  
**Propósito:** Teclado de performance con pads que complementa Quantum Tree Sequencer y Quantum Harmonic Sequencer

---

## 🎯 CONCEPTO

**QUANTUM CRYSTAL KEYBOARD**
- 123 HP de espacio total (624.84mm ancho × 128.5mm alto)
- Layout de pads tipo Push/Launchpad optimizado para VCV Rack
- Integración perfecta con ambos secuenciadores
- Quantum features únicos
- Performance-oriented design

---

## 🎹 ARQUITECTURA PROPUESTA

### LAYOUT HORIZONTAL (624.84mm)

```
┌─────────────┬──────────────────────────────────────┬─────────────┐
│   CONTROL   │         PAD MATRIX 8×8              │   QUANTUM   │
│   SECTION   │         (64 PADS)                   │   SECTION   │
│   (150mm)   │         (325mm)                     │   (150mm)   │
│             │                                      │             │
│  Velocity   │  ┌──┬──┬──┬──┬──┬──┬──┬──┐         │  IBM Qubit  │
│  Octave     │  │  │  │  │  │  │  │  │  │ ROW 8  │  Processing │
│  Scale      │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │             │
│  Mode       │  │  │  │  │  │  │  │  │  │ ROW 7  │  Entangle   │
│  Quantize   │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │  Decohere   │
│             │  │  │  │  │  │  │  │  │  │ ROW 6  │  Superpos   │
│  QTS Link   │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │             │
│  QHS Link   │  │  │  │  │  │  │  │  │  │ ROW 5  │  Gate Outs  │
│             │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │  CV Outs    │
│  Seq Ctrl   │  │  │  │  │  │  │  │  │  │ ROW 4  │  Triggers   │
│  Pattern    │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │             │
│             │  │  │  │  │  │  │  │  │  │ ROW 3  │  Velocity   │
│  Display    │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │  Aftertouch │
│  (OLED)     │  │  │  │  │  │  │  │  │  │ ROW 2  │  Expression │
│             │  ├──┼──┼──┼──┼──┼──┼──┼──┤         │             │
│             │  │  │  │  │  │  │  │  │  │ ROW 1  │  8 Macros   │
│             │  └──┴──┴──┴──┴──┴──┴──┴──┘         │             │
│             │    C  D  E  F  G  A  B  C'         │             │
└─────────────┴──────────────────────────────────────┴─────────────┘
   24 HP           65 HP (ish)                         30 HP
```

---

## ✨ CARACTERÍSTICAS PRINCIPALES

### 1. PAD MATRIX 8×8 (64 PADS)

**Layout Musical:**
- Filas = Octavas (8 octavas: C-2 a C6)
- Columnas = Notas (C, D, E, F, G, A, B, C)
- Pads iluminados por RGB LED
- Velocity sensitive (0-127)
- Aftertouch per-pad

**Tamaño de Pads:**
- 64 pads en 325mm × 95mm
- Cada pad: ~38mm × 10mm
- Spacing: 2mm entre pads
- Click activo al presionar

### 2. CONTROL SECTION (Izquierda - 150mm)

**Knobs y Switches:**
```
┌─────────────────┐
│  VELOCITY       │ ← Trimpot (0-200%)
│  [====]         │
├─────────────────┤
│  OCTAVE         │ ← Trimpot (-4 a +4)
│  [====]         │
├─────────────────┤
│  SCALE SELECT   │ ← Switch 12 pos
│  [◇]            │    (Major, Minor, Dorian...)
├─────────────────┤
│  QUANTIZE       │ ← Toggle ON/OFF
│  [○]            │
├─────────────────┤
│  QTS LINK       │ ← LED Button
│  [●]            │    (Sync con Tree Seq)
├─────────────────┤
│  QHS LINK       │ ← LED Button  
│  [●]            │    (Sync con Harm Seq)
├─────────────────┤
│  PATTERN BANK   │ ← 8 LED buttons
│  [●][●][●][●]  │    (Save/recall)
│  [●][●][●][●]  │
├─────────────────┤
│  OLED DISPLAY   │ ← 40×20mm
│  ┌───────────┐  │    4 páginas info
│  │ C Major   │  │
│  │ Octave +2 │  │
│  └───────────┘  │
└─────────────────┘
```

**CV Inputs (abajo):**
- VELOCITY CV (modula velocity)
- OCTAVE CV (transpose)
- SCALE CV (cambia escala)
- QUANTIZE GATE (activa cuantización)

### 3. QUANTUM SECTION (Derecha - 150mm)

**Quantum Processing:**
```
┌──────────────────┐
│  IBM QUBITS      │
│  ▓▓▓▓▓▓▓▓ (8)   │ ← Visual de qubits
├──────────────────┤
│  ENTANGLE        │ ← Knob + CV
│  [====]  [IN]    │   (Pads correlacionados)
├──────────────────┤
│  DECOHERENCE     │ ← Knob + CV
│  [====]  [IN]    │   (Humanización)
├──────────────────┤
│  SUPERPOSITION   │ ← Knob + CV
│  [====]  [IN]    │   (Multi-nota simultánea)
├──────────────────┤
│  OUTPUTS (8ch)   │
│  ┌──┬──┬──┬──┐  │
│  │V/│GT│AF│EX│  │ ← 1-4
│  ├──┼──┼──┼──┤  │
│  │V/│GT│AF│EX│  │ ← 5-8
│  └──┴──┴──┴──┘  │
├──────────────────┤
│  MACRO (8)       │
│  [1][2][3][4]    │ ← Knobs
│  [5][6][7][8]    │   Programables
└──────────────────┘
```

**8 Canales de Salida:**
- Cada canal tiene 4 outputs:
  - **V/OCT** - CV tono
  - **GATE** - Gate trigger
  - **AFTR** - Aftertouch CV
  - **EXPR** - Expression CV

Total: 32 outputs en Quantum Section

---

## 🔌 INTEGRACIÓN CON SECUENCIADORES

### QUANTUM TREE SEQUENCER ⟷ KEYBOARD

**Modo QTS LINK activo:**
- Keyboard envía notas → QTS recibe y secuencia
- QTS envía pattern clock → Keyboard sincroniza LEDs
- Keyboard ROOT/SCALE → QTS QUANTIZE input
- QTS puede "grabar" lo que tocas en pads

### QUANTUM HARMONIC SEQUENCER ⟷ KEYBOARD

**Modo QHS LINK activo:**
- Keyboard ROOT/SCALE → QHS recibe info armónica
- QHS envía acordes → Keyboard ilumina pads correspondientes
- Círculos armónicos NDLR reflejados en pad colors
- Keyboard puede "tocar" sobre progresión de QHS

---

## 🎨 VISUALIZACIÓN DE PADS

### RGB LED States:

| Color       | Significado                        |
|-------------|------------------------------------|
| Azul        | Nota en escala actual              |
| Rojo        | Nota fuera de escala               |
| Verde       | Nota activa (pressed)              |
| Amarillo    | Nota en acorde actual (QHS link)   |
| Cyan        | Root note de escala                |
| Magenta     | Nota "entangled" (quantum)         |
| Blanco      | Superposición múltiple             |

### Animaciones:
- Pulse en tempo con QTS/QHS
- Fade out gradual al soltar
- Shimmer en quantum superposition

---

## 💻 ESPECIFICACIONES TÉCNICAS

### Audio Processing:
- Sample rate: 44.1 kHz (VCV Rack)
- Latency: <1ms (trigger directo)
- Polyphony: 64 voces simultáneas
- Velocity curve: Exponencial ajustable

### MIDI Integration:
- MIDI input opcional (USB/CV)
- MIDI output de 64 pads
- MPE support (per-pad pitch bend)

### Memory:
- 8 pattern banks × 64 pads
- Pattern storage: note + velocity + aftertouch
- Total: 512 eventos guardados

### Quantum Features:
- IBM Quantum jobs: 3 adicionales
  1. Entanglement (correlación de pads)
  2. Decoherence (humanización timing)
  3. Superposition (chord generation)

---

## 📐 DIMENSIONES EXACTAS

### Panel Total:
- Ancho: 624.84mm (123 HP)
- Alto: 128.5mm (3U Eurorack)

### Secciones:
- Control: 150mm (29.6 HP)
- Pad Matrix: 325mm (64 HP)
- Quantum: 150mm (29.6 HP)

### Pad Matrix Detail:
- 8 columnas × 38mm = 304mm
- 8 rows × 10mm = 80mm
- Spacing: 2mm horizontal, 1mm vertical
- Total area: 325mm × 95mm
- Posición Y: 16.75mm desde top

---

## 🏗️ PLAN DE IMPLEMENTACIÓN

### ✅ FASE 1: Estructura Base (COMPLETADO - 21 Ene 2026)
- [x] Crear `QuantumCrystalKeyboard.cpp` (~600 líneas base)
- [x] Panel SVG 624.84mm × 128.5mm
- [x] Layout de 3 secciones (Control/Pads/Quantum)
- [x] 64 pad buttons (8×8 grid) con RGB LEDs
- [x] Registro en plugin.json/cpp/hpp
- [x] Compilación e instalación exitosa

**Resultado:** Módulo visible en VCV Rack browser, estructura funcional, listo para Fase 2.

---

### FASE 2: Pad Matrix Logic (4-5 horas) - PRÓXIMO
- [ ] Crear `QuantumCrystalKeyboard.cpp`
- [ ] Panel SVG 624.84mm × 128.5mm
- [ ] Layout de 3 secciones
- [ ] 64 pad buttons (8×8 grid)
- [ ] Registro en plugin.json/cpp/hpp

### FASE 2: Pad Matrix Logic (4-5 horas)
- [ ] Clase `QuantumPad` (state, LED, velocity)
- [ ] Grid manager 8×8
- [ ] Note mapping (C-2 a C6)
- [ ] Velocity processing (0-127)
- [ ] LED RGB control
- [ ] Click feedback

### FASE 3: Control Section (3-4 horas)
- [ ] 10 knobs/switches control
- [ ] OLED display 40×20mm (4 páginas)
- [ ] Scale selection (12 escalas)
- [ ] Octave transpose (-4 a +4)
- [ ] Quantize toggle
- [ ] Pattern bank LEDs (8)
- [ ] 4 CV inputs

### FASE 4: Quantum Section (4-5 horas)
- [ ] IBM Qubit visualization (8 qubits)
- [ ] Entanglement algorithm (pad correlation)
- [ ] Decoherence (timing humanization)
- [ ] Superposition (chord generator)
- [ ] 32 outputs (8 canales × 4 tipos)
- [ ] 8 macro knobs programables

### FASE 5: Integración Secuenciadores (3-4 horas)
- [ ] QTS LINK protocol
- [ ] QHS LINK protocol
- [ ] ROOT/SCALE CV output (format QTS)
- [ ] Pattern sync con QTS clock
- [ ] Chord receive de QHS
- [ ] LED sync con secuenciadores

### FASE 6: Pattern Memory (2-3 horas)
- [ ] Pattern storage (64 pads × 8 banks)
- [ ] Save/recall functionality
- [ ] LED indicators de pattern activo
- [ ] Merge patterns mode

### FASE 7: Quantum Jobs IBM (2-3 horas)
- [ ] Generar 3 circuitos cuánticos nuevos
- [ ] Entanglement circuit (8 qubits)
- [ ] Decoherence measurement
- [ ] Superposition states
- [ ] Integrar .qdt files

### FASE 8: Testing & Polish (2-3 horas)
- [ ] Test todos los pads
- [ ] Verificar velocity response
- [ ] Test integración QTS/QHS
- [ ] Ajustar LED brightness
- [ ] Documentación final

**TIEMPO TOTAL ESTIMADO:** 23-31 horas

---

## 🎮 CASOS DE USO

### Caso 1: Performance en Vivo
```
1. Seleccionar escala (C Minor)
2. Activar QUANTIZE
3. Tocar pads libremente → todo en escala
4. DECOHERENCE → humanización automática
5. Velocity dinámica → expresión natural
```

### Caso 2: Jam con QTS
```
1. Activar QTS LINK
2. QTS genera pattern → Keyboard sincroniza
3. Tocar pads → QTS graba y secuencia
4. QTS envía ROOT → Keyboard actualiza escala
5. Loop perfecto entre ambos
```

### Caso 3: Harmonía con QHS
```
1. Activar QHS LINK
2. QHS genera progresión armónica
3. Keyboard ilumina notas del acorde actual
4. Tocar pads iluminados → armonía perfecta
5. QHS cambia acorde → LEDs actualizan
```

### Caso 4: Quantum Experimentation
```
1. ENTANGLE alto → pads correlacionados
2. Presionar pad C → pads E y G también suenan
3. SUPERPOSITION → genera acordes aleatorios
4. DECOHERENCE → timing orgánico
5. Resultados impredecibles únicos
```

---

## 📊 COMPARACIÓN CON HARDWARE

| Feature                  | Hardware (Push/Launchpad) | Quantum Crystal | Ventaja |
|--------------------------|---------------------------|-----------------|---------|
| Pads                     | 64 (8×8)                  | 64 (8×8)        | ✓       |
| RGB LEDs                 | Sí                        | Sí              | ✓       |
| Velocity                 | Sí                        | Sí + CV mod     | ✓✓      |
| Aftertouch               | Limitado                  | Per-pad + CV    | ✓✓      |
| Quantum Processing       | No                        | IBM real        | ✓✓✓     |
| Secuencer Integration    | DAW only                  | QTS + QHS       | ✓✓✓     |
| CV/Gate Outputs          | No                        | 32 outputs      | ✓✓✓     |
| Pattern Memory           | 8 banks                   | 8 banks         | ✓       |
| Display                  | Basic                     | OLED 4-page     | ✓✓      |
| Modularity               | Standalone                | Eurorack 123HP  | ✓✓      |

---

## 🎯 PRÓXIMOS PASOS

### AHORA MISMO:
1. ¿Apruebas el diseño 8×8 con 3 secciones?
2. ¿Algún cambio en layout o features?
3. ¿Empezamos con Fase 1?

### ALTERNATIVAS:
- 4×4 pads más grandes (16 total)
- 16×4 layout (64 pads horizontales)
- Agregar ribbon controller
- XY pad para expression

---

## 📝 NOTAS TÉCNICAS

### Archivos a Crear:
```
src/QuantumCrystalKeyboard.cpp  (~2000 líneas)
res/QuantumCrystalKeyboard.svg  (624.84×128.5mm)
quantum-datasets/keyboard_*.qdt (3 nuevos)
```

### Dependencias:
- Rack SDK 2.x
- IBM Quantum jobs (3 adicionales)
- QuantumDataLoader.hpp (ya existe)

### Integración:
- plugin.json (metadata)
- plugin.cpp (registry)
- plugin.hpp (declaration)

---

**STATUS:** ✅ Listo para implementar

**WAITING FOR:** Tu aprobación del diseño

---

*Quantum Crystal Keyboard - "The first 64-pad quantum controller with real IBM qubit processing and seamless VCV Rack sequencer integration"* 🎹⚛️

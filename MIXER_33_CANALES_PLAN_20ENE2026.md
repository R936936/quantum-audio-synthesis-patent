# 🎚️ MIXER 33 CANALES - SISTEMA MODULAR
## Plan de Implementación - 20 Enero 2026

---

## 📊 RESUMEN EJECUTIVO

**Sistema modular de 4 módulos independientes:**
- **Mixer A (15HP)**: Canales 1-11 + Bus output
- **Mixer B (15HP)**: Canales 12-22 + Bus output  
- **Mixer C (15HP)**: Canales 23-33 + Bus output
- **Master (15HP)**: Control master + Sends/Returns + Outputs

**Total:** 60HP (cada módulo independiente, expansible)

---

## 🎯 DECISIÓN: OPCIÓN B - SISTEMA MODULAR

### ✅ VENTAJAS:
- 33 canales completos como especificaste
- Cada módulo es manejable (15HP)
- Features completas por canal
- Expansible (puedes usar 1, 2, 3 o 4 módulos)
- Más fácil de diseñar y probar
- Más versátil para diferentes setups

### 📐 LAYOUT DE CADA MIXER (A, B, C):

```
┌─────────────────────────────────────────┐
│  MIXER A - CANALES 1-11 (15HP)         │
├─────────────────────────────────────────┤
│                                         │
│  COL 1      COL 2      COL 3     MASTER│
│  (1-4)      (5-8)      (9-11)    BUS   │
│                                         │
│  [VOL]      [VOL]      [VOL]      🔊   │
│  [PAN]      [PAN]      [PAN]     [BUS] │
│  [SND]      [SND]      [SND]     OUT → │
│  ( IN )     ( IN )     ( IN )          │
│  (CV )      (CV )      (CV )           │
│  [LED]      [LED]      [LED]           │
│                                         │
│    ×4         ×4         ×3       LINK │
│ canales   canales   canales      LED   │
│                                         │
│  15 HP = 76mm width                    │
│  128.5mm height                         │
└─────────────────────────────────────────┘
```

### 📐 LAYOUT DEL MASTER:

```
┌─────────────────────────────────────────┐
│  MIXER MASTER (15HP)                    │
├─────────────────────────────────────────┤
│                                         │
│  ┌─── BUS INPUTS ───┐                  │
│  │ IN A  IN B  IN C │                  │
│  │  ○     ○     ○   │                  │
│  └──────────────────┘                  │
│                                         │
│  ┌─── FX SENDS/RETURNS ───┐            │
│  │ SEND 1        RETURN 1 │            │
│  │ [SND1]  OUT →  ○ IN   │            │
│  │ [RTN1]         ○ L    │            │
│  │                ○ R    │            │
│  │                        │            │
│  │ SEND 2        RETURN 2 │            │
│  │ [SND2]  OUT →  ○ IN   │            │
│  │ [RTN2]         ○ L    │            │
│  │                ○ R    │            │
│  └────────────────────────┘            │
│                                         │
│  ┌─── MASTER FADERS ───┐               │
│  │   [MASTER L]        │               │
│  │   [MASTER R]        │               │
│  └─────────────────────┘               │
│                                         │
│  ┌─── OUTPUTS ───┐                     │
│  │ STEREO OUT    │                     │
│  │  ○ L   ○ R    │                     │
│  │               │                     │
│  │ HEADPHONES    │                     │
│  │  ○ L   ○ R    │                     │
│  │ [PHONES VOL]  │                     │
│  │               │                     │
│  │ USB (35 outs) │                     │
│  │  ○ ○ ○ ○ ...  │ (mix + 33 direct) │
│  │  [USB LED]    │                     │
│  └───────────────┘                     │
│                                         │
│  15 HP = 76mm width                    │
└─────────────────────────────────────────┘
```

---

## 🔧 ESPECIFICACIONES TÉCNICAS

### MIXER A, B, C (CADA UNO):

#### Por Canal (11 canales por módulo):
- **1× Volume Knob** (0-1, logarítmico)
  - Rango: -∞ a 0 dB
  - Con CV input + attenuverter (-5V a +5V)
  
- **1× Pan Knob** (-1 a +1, centro detent)
  - Pan law: -3dB (profesional)
  - L = 100% cuando pan = -1
  - R = 100% cuando pan = +1
  - Center = 70.7% ambos lados
  
- **1× Send Amount Knob** (0-1)
  - Pre-fader send (para monitors)
  - Envía a bus de sends global
  
- **1× Audio Input Jack**
  - Impedancia: 100kΩ (high-Z)
  - Rango: ±10V
  
- **1× CV Input Jack** (control de volumen)
  - 0-10V modula volumen 0-100%
  - -5 a +5V con attenuverter
  
- **1× Signal LED** (verde)
  - Ilumina cuando señal > -20dB
  - Brightness proporcional a nivel

#### Output del módulo:
- **1× Bus Output L** (suma pre-master)
- **1× Bus Output R** (suma pre-master)
- Conectar estos a Master module

#### Total por módulo MIXER:
- **Params:** 33 (11× vol, 11× pan, 11× send)
- **Inputs:** 33 (11× audio, 11× CV, 11× attenuverter)
- **Outputs:** 2 (bus L, bus R)
- **Lights:** 11 (LEDs de señal)

---

### MASTER MODULE:

#### Bus Inputs:
- **3× Bus Input L** (de Mixer A, B, C)
- **3× Bus Input R** (de Mixer A, B, C)
- Suma interna automática

#### FX Sends (2):
- **Send 1 Knob** (nivel global)
- **Send 1 Output** (mono, post-sum)
- **Return 1 L Input**
- **Return 1 R Input**
- **Return 1 Level Knob**

- **Send 2 Knob** (nivel global)
- **Send 2 Output** (mono, post-sum)
- **Return 2 L Input**
- **Return 2 R Input**
- **Return 2 Level Knob**

#### Master Section:
- **Master L Fader** (0-2, +6dB max)
- **Master R Fader** (0-2, +6dB max)
- **Stereo Output L**
- **Stereo Output R**

#### Headphones:
- **Headphone L Output** (copia de master)
- **Headphone R Output** (copia de master)
- **Headphone Volume Knob** (0-2)
- Ganancia adicional: +6dB para headphones

#### USB Output (ES-9 style):
- **35 outputs virtuales:**
  - Outputs 1-2: Master mix L/R (post-fader)
  - Outputs 3-35: Direct outs canales 1-33 (pre-master)
- **USB Connection LED** (azul)
- En VCV Rack: implementar con 35 output jacks

#### Total MASTER module:
- **Params:** 7 (2× send level, 2× return level, 2× master fader, 1× phones vol)
- **Inputs:** 10 (3× bus L, 3× bus R, 2× return L, 2× return R)
- **Outputs:** 41 (2× stereo, 2× phones, 2× sends, 35× USB)
- **Lights:** 1 (USB LED)

---

## 📦 ARCHIVOS A CREAR

### MIXER A:
```
src/MixerA_11ch.cpp          (~800 lines)
res/MixerA_11ch.svg          (15HP panel)
```

### MIXER B:
```
src/MixerB_11ch.cpp          (~800 lines, copia de A)
res/MixerB_11ch.svg          (15HP panel)
```

### MIXER C:
```
src/MixerC_11ch.cpp          (~800 lines, copia de A)
res/MixerC_11ch.svg          (15HP panel)
```

### MASTER:
```
src/MixerMaster.cpp          (~600 lines)
res/MixerMaster.svg          (15HP panel)
```

### Archivos modificados:
```
src/plugin.hpp               (añadir 4 extern Model*)
src/plugin.cpp               (registrar 4 módulos)
plugin.json                  (metadata de 4 módulos)
```

---

## 🎨 DISEÑO VISUAL

### Tema: Verde Matrix (consistente con Quantum Tree)
- Fondo: `#000000` (negro puro)
- Controles: Verde matrix `#00ff00`
- LEDs: Verde `#00ff00`
- Texto: Verde matrix
- Sin círculos decorativos (minimalista)

### Tipografía:
- Títulos: `'Orbitron', monospace` bold
- Labels: `'Orbitron', monospace` regular
- Números: `monospace` small

---

## ⚙️ PROCESAMIENTO DE AUDIO

### Pan Law (-3dB):
```cpp
float panL = (pan <= 0.f) ? 1.f : std::cos(pan * M_PI / 4.f);
float panR = (pan >= 0.f) ? 1.f : std::cos(-pan * M_PI / 4.f);
```

### Volume (logarítmico):
```cpp
float volumeDb = params[VOL].getValue(); // 0-1
float volumeLin = std::pow(10.f, volumeDb * 2.f - 2.f); // -40dB a 0dB
```

### CV Modulation:
```cpp
float cvVoltage = inputs[CV].getVoltage(); // -5 a +5V
float atten = params[CV_ATTEN].getValue(); // -1 a +1
float modulation = cvVoltage * atten * 0.1f; // escala a 0-1
float finalVolume = clamp(volumeLin + modulation, 0.f, 1.f);
```

### Send (pre-fader):
```cpp
float sendAmount = params[SEND].getValue(); // 0-1
float sendSignal = inputSignal * sendAmount; // antes de volume/pan
sendBusL += sendSignal * panL;
sendBusR += sendSignal * panR;
```

### Bus Summing:
```cpp
// En cada channel:
busL += processedSignal * panL * volume;
busR += processedSignal * panR * volume;

// En master:
masterL = busA_L + busB_L + busC_L + return1_L + return2_L;
masterR = busA_R + busB_R + busC_R + return1_R + return2_R;
```

---

## 🔄 CONEXIONES ENTRE MÓDULOS

```
┌─────────────┐
│  MIXER A    │
│  (Ch 1-11)  │
│             │
│  BUS L OUT ─┼──┐
│  BUS R OUT ─┼──┤
└─────────────┘  │
                 │
┌─────────────┐  │
│  MIXER B    │  │    ┌─────────────┐
│  (Ch 12-22) │  │    │   MASTER    │
│             │  ├───→│  BUS A IN   │
│  BUS L OUT ─┼──┤    │  BUS B IN   │
│  BUS R OUT ─┼──┼───→│  BUS C IN   │
└─────────────┘  │    │             │
                 │    │  SEND 1 ────┼──→ To FX
┌─────────────┐  │    │  SEND 2 ────┼──→ To FX
│  MIXER C    │  │    │             │
│  (Ch 23-33) │  │    │  RET 1 IN ←─┼─── From FX
│             │  │    │  RET 2 IN ←─┼─── From FX
│  BUS L OUT ─┼──┘    │             │
│  BUS R OUT ─┼───────│  STEREO OUT │
└─────────────┘       │  PHONES OUT │
                      │  USB OUTS   │
                      └─────────────┘
```

---

## 📋 PLAN DE IMPLEMENTACIÓN (6 FASES)

### FASE 1: MIXER A (Canal 1-11)
**Tiempo estimado:** 2-3 horas

1. Crear estructura básica (`MixerA_11ch.cpp`)
2. Definir params/inputs/outputs/lights (11 canales)
3. Crear panel SVG 15HP con layout 3×4 grid
4. Implementar procesamiento:
   - Volume con CV modulation
   - Pan con -3dB law
   - Send amount (pre-fader)
   - Bus summing L/R
5. Compilar y verificar en VCV Rack
6. Ajustar posiciones visuales

### FASE 2: MIXER B y C (copias)
**Tiempo estimado:** 30 minutos

1. Copiar `MixerA_11ch.cpp` → `MixerB_11ch.cpp` y `MixerC_11ch.cpp`
2. Cambiar nombres de struct y labels
3. Copiar y modificar SVG panels
4. Registrar en plugin.hpp y plugin.cpp
5. Compilar y verificar

### FASE 3: MASTER MODULE
**Tiempo estimado:** 2-3 horas

1. Crear `MixerMaster.cpp`
2. Implementar:
   - 3 bus inputs summing
   - 2 sends con control global
   - 2 returns stereo
   - Master faders L/R
   - Headphone amp (+6dB)
3. Crear panel SVG 15HP
4. Compilar y verificar

### FASE 4: CONEXIONES Y TESTING
**Tiempo estimado:** 1-2 horas

1. Conectar Mixer A → Master
2. Conectar Mixer B → Master
3. Conectar Mixer C → Master
4. Probar con Golden Oscillator outputs
5. Verificar summing correcto
6. Verificar pan law
7. Verificar sends/returns

### FASE 5: USB OUTPUTS (35 canales)
**Tiempo estimado:** 1 hora

1. Añadir 35 outputs en Master module
2. Output 1-2: Master mix post-fader
3. Outputs 3-35: Direct outs pre-master de cada canal
4. Implementar routing interno
5. Probar grabación multi-track

### FASE 6: OPTIMIZACIÓN Y DOCUMENTACIÓN
**Tiempo estimado:** 1 hora

1. Ajustar posiciones de controles
2. Optimizar performance (simd?)
3. Crear documentación de uso
4. Commit a GitHub
5. Screenshots y demo patch

**TIEMPO TOTAL ESTIMADO:** 7-10 horas

---

## 💡 CARACTERÍSTICAS ESPECIALES

### CV Modulation:
- Cada canal tiene CV input con attenuverter
- Modula el volume en tiempo real
- Perfecto para sidechaining, ducking, automation

### Pre-fader Sends:
- Sends se toman ANTES del fader de volumen
- Ideal para monitores de músicos
- No afecta el nivel de send cuando ajustas el fader

### Pan Law -3dB:
- Center = -3dB en cada lado (70.7% cada uno)
- Potencia acústica constante
- Standard profesional de mezcla

### Direct Outs (USB):
- Cada canal tiene direct out pre-master
- Permite grabación multitrack en DAW
- 33 tracks individuales + 2 master mix = 35 outputs

### Headphone Amp:
- +6dB de ganancia adicional
- Suficiente para headphones de alta impedancia
- Control de volumen independiente

---

## 🎯 CASOS DE USO

### Setup 1: Sistema completo (4 módulos)
```
Sources → Mixer A, B, C → Master → Stereo Out + USB Recording
         (33 channels)
```

### Setup 2: Sistema básico (2 módulos)
```
Sources → Mixer A → Master → Stereo Out
         (11 channels, expansible)
```

### Setup 3: Multi-bus (sin master)
```
Sources → Mixer A → External Mixer
        → Mixer B → External Mixer
        → Mixer C → External Mixer
(3 sub-grupos independientes)
```

### Setup 4: Con FX externos
```
Master SEND 1 → Reverb → Master RETURN 1
Master SEND 2 → Delay → Master RETURN 2
```

---

## 📊 RESUMEN DE COMPONENTES

### Por módulo MIXER (A, B, C):
- **11 canales** completos
- **3 knobs** por canal (vol, pan, send)
- **2 inputs** por canal (audio, CV)
- **1 LED** por canal
- **2 outputs** de bus (L, R)
- **Tamaño:** 15HP × 128.5mm

### Módulo MASTER:
- **6 inputs** (3× bus L, 3× bus R)
- **7 knobs** (sends, returns, master, phones)
- **41 outputs** (stereo, phones, sends, USB×35)
- **1 LED** (USB status)
- **Tamaño:** 15HP × 128.5mm

### Total sistema completo:
- **33 canales** de entrada
- **99 knobs** (33×3)
- **66 inputs** (33× audio, 33× CV)
- **45 outputs** (2 stereo + 2 phones + 2 sends + 35 USB + 4 returns)
- **33 LEDs** de señal + 1 USB LED
- **Tamaño:** 60HP (4 módulos × 15HP)

---

## 🚀 PRÓXIMOS PASOS (MAÑANA 21 ENERO)

1. **Revisar este documento** y confirmar especificaciones
2. **Decidir orden de implementación:**
   - Opción A: Empezar con Mixer A completo
   - Opción B: Empezar con Master completo
   - Recomendación: Empezar con Mixer A (más simple)
3. **Crear Mixer A (Fase 1)**
4. **Probar con audio real**
5. **Continuar con fases 2-6**

---

## 📝 NOTAS IMPORTANTES

### Ventajas del diseño modular:
✅ Cada módulo es independiente
✅ Puedes usar 1, 2, 3 o 4 módulos según necesites
✅ Más fácil de mantener y debuggear
✅ Permite diferentes configuraciones
✅ 15HP por módulo es tamaño razonable

### Compatibilidad:
✅ Conecta con Golden Oscillator (3 osciladores)
✅ Conecta con Quantum Tree Sequencer
✅ Conecta con cualquier módulo de VCV Rack
✅ Compatible con VCV Recorder para USB recording

### Expansibilidad futura:
- Agregar EQ por canal (otro módulo)
- Agregar compresión por canal (otro módulo)
- Agregar más sends (modificar Master)
- Agregar automation recording (otro módulo)

---

## 🎉 RESULTADO FINAL

**Sistema profesional de mezcla modular:**
- ⚡ 33 canales completos
- 🎛️ CV modulation en cada canal
- 🔊 Master section profesional
- 🎧 Salida de audífonos dedicada
- 💾 USB output multi-track (35 canales)
- 🎨 Tema verde matrix minimalista
- 📦 4 módulos de 15HP cada uno
- 🔗 Sistema expansible y modular

**Total: 60HP de puro poder de mezcla profesional** 🚀

---

**Documento creado:** 20 Enero 2026, 00:52 AM  
**Para trabajar:** 21 Enero 2026  
**Proyecto:** AurumLab v2.8.0 - Mixer System  
**Autor:** R936936

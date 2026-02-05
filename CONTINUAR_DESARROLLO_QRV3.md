# Quantum Resonator V3 - Guía para Continuar el Desarrollo

---

## 🎯 ESTADO ACTUAL

✅ **Proyecto limpio y consolidado**
- Solo existe UN directorio: `~/AurumLab/`
- Todas las versiones antiguas movidas a: `~/OBSOLETE_AURUM_BACKUPS_TO_DELETE/`
- Plugin compilado e instalado en Rack2

✅ **Módulo funcional**
- Quantum Resonator V3 está compilado
- Instalado en: `~/Library/Application Support/Rack2/plugins-mac-arm64/`
- Brand: **Aurum**
- Versión: **3.0.0**

---

## 📋 VERIFICACIÓN INMEDIATA

### 1. Verificar que el módulo aparece en Rack2
```bash
# Rack2 Pro debería estar abierto ahora
# Busca "Aurum" en el navegador de módulos
# Deberías ver: "Quantum Resonator V3"
```

### 2. Testear funcionalidad básica
- [ ] El módulo aparece en el navegador
- [ ] Se puede agregar al rack
- [ ] Los displays de frecuencia muestran valores
- [ ] Los controles responden
- [ ] Genera audio cuando se conecta a un output
- [ ] Los triggers funcionan
- [ ] V/Oct funciona correctamente

---

## 🔧 PRÓXIMAS MEJORAS

### MEJORA #1: Ajustar Layout del Panel (URGENTE)

**Problema**: Algunos controles están superpuestos visualmente

**Archivo a editar**: `~/AurumLab/src/QuantumResonatorV3.cpp`

**Sección a modificar**: `QuantumResonatorV3Widget` (línea ~1208)

**Qué ajustar**:
- Posición Y de controles en la fila inferior
- Espaciado entre inputs/outputs
- Eliminar displays rectangulares que no tienen función

**Comando para editar**:
```bash
cd ~/AurumLab
code src/QuantumResonatorV3.cpp
# o
nano src/QuantumResonatorV3.cpp
```

**Después de editar, recompilar**:
```bash
cd ~/AurumLab
make && make install
```

---

### MEJORA #2: Entrada de Teclado en Frequency Displays

**Objetivo**: Permitir entrada directa de Hz desde teclado numérico

**Archivo**: `~/AurumLab/src/QuantumResonatorV3.cpp`

**Función actual**: `FrequencyDisplay` (línea ~1140)

**Qué mejorar**:
- Captura de eventos de teclado
- Validación de entrada numérica
- Conversión de Hz a parámetro de frecuencia

**Status actual**: 
- Click en display abre menú de texto
- Permite entrada manual
- Necesita refinamiento

---

### MEJORA #3: Triggers Funcionando Correctamente

**Verificar**:
- Triggers deben afectar al oscilador, no al delay
- Cada trigger debe reiniciar la fase del canal correspondiente
- Trigger global debe afectar ambos canales

**Archivo**: `~/AurumLab/src/QuantumResonatorV3.cpp`

**Función**: `process()` del módulo (línea ~900+)

**Buscar**:
```cpp
if (triggerL.process(inputs[TRIGGER_L_INPUT].getVoltage())) {
    oscL.resetPhase();
}
```

---

### MEJORA #4: Calidad de Audio

**Objetivos**:
1. Anti-aliasing en osciladores
2. Oversampling opcional
3. Suavizado de parámetros (para evitar clicks)

**Técnicas a implementar**:
- PolyBLEP para reducir aliasing
- Interpolación en cambios de parámetros
- Filtros anti-aliasing en delays

---

### MEJORA #5: Optimización de CPU

**Estrategias**:
1. Reducir número de parciales en modos simples
2. Lazy evaluation de resonadores silenciosos
3. Usar SIMD cuando sea posible
4. Cache de valores trigonométricos

**Medición actual**:
```bash
# En Rack2, activar Performance Meter
# CPU% se muestra en la esquina
```

---

## 🎨 AJUSTES DE PANEL DETALLADOS

### Coordenadas Sugeridas (en mm, panel de 20HP = 101.6mm ancho)

```cpp
// FREQUENCY DISPLAYS (top)
float displayY = 20.0f;
addChild(createDisplay<FrequencyDisplay>(mm2px(Vec(8.0, displayY)), ...));  // Left
addChild(createDisplay<FrequencyDisplay>(mm2px(Vec(60.0, displayY)), ...)); // Right

// MODE & MORPH (upper middle)
float modeY = 35.0f;
addParam(createParam<...>(mm2px(Vec(15.0, modeY)), ...MODE_PARAM));
addParam(createParam<...>(mm2px(Vec(70.0, modeY)), ...MORPH_PARAM));

// SPIRAL CONTROLS (4 knobs in 2x2, middle section)
float spiralY1 = 50.0f;
float spiralY2 = 65.0f;
float spiralX1 = 10.0f;
float spiralX2 = 45.0f;
// Row 1
addParam(createParam<...>(mm2px(Vec(spiralX1, spiralY1)), ...SPIRAL_RATE_PARAM));
addParam(createParam<...>(mm2px(Vec(spiralX2, spiralY1)), ...SPIRAL_DEPTH_PARAM));
// Row 2
addParam(createParam<...>(mm2px(Vec(spiralX1, spiralY2)), ...SPIRAL_COMPLEXITY_PARAM));
addParam(createParam<...>(mm2px(Vec(spiralX2, spiralY2)), ...SPIRAL_SHAPE_PARAM));

// QUANTUM SUPERPOSITION (3 knobs, middle)
float qSupY = 82.0f;
float qSupX1 = 8.0f;
float qSupX2 = 35.0f;
float qSupX3 = 62.0f;
addParam(createParam<...>(mm2px(Vec(qSupX1, qSupY)), ...Q_SPREAD_PARAM));
addParam(createParam<...>(mm2px(Vec(qSupX2, qSupY)), ...Q_EVOLUTION_PARAM));
addParam(createParam<...>(mm2px(Vec(qSupX3, qSupY)), ...Q_COHERENCE_PARAM));

// QUANTUM ENTANGLEMENT (2 knobs, lower left)
float qEntY = 97.0f;
float qEntX1 = 8.0f;
float qEntX2 = 28.0f;
addParam(createParam<...>(mm2px(Vec(qEntX1, qEntY)), ...Q_ENTANGLE_CHANNEL_PARAM));
addParam(createParam<...>(mm2px(Vec(qEntX2, qEntY)), ...Q_ENTANGLE_HARMONIC_PARAM));

// QUANTUM TUNNEL (1 knob, lower left)
float qTunY = 97.0f;
float qTunX = 48.0f;
addParam(createParam<...>(mm2px(Vec(qTunX, qTunY)), ...Q_TUNNEL_PARAM));

// DELAY CONTROLS (2 knobs, lower center)
float delayY = 97.0f;
float delayX1 = 65.0f;
float delayX2 = 82.0f;
addParam(createParam<...>(mm2px(Vec(delayX1, delayY)), ...DELAY_AMOUNT_PARAM));
addParam(createParam<...>(mm2px(Vec(delayX2, delayY)), ...DELAY_ITERATIONS_PARAM));

// REVERB CONTROLS (2 knobs, lower right)
float reverbY = 112.0f;
float reverbX1 = 65.0f;
float reverbX2 = 82.0f;
addParam(createParam<...>(mm2px(Vec(reverbX1, reverbY)), ...REVERB_FEEDBACK_PARAM));
addParam(createParam<...>(mm2px(Vec(reverbX2, reverbY)), ...REVERB_MIX_PARAM));

// INPUTS (left side, evenly spaced)
float inputX = 5.0f;
addInput(createInput<...>(mm2px(Vec(inputX, 40.0)), ...VOCT_L_INPUT));
addInput(createInput<...>(mm2px(Vec(inputX, 52.0)), ...VOCT_R_INPUT));
addInput(createInput<...>(mm2px(Vec(inputX, 64.0)), ...TRIGGER_L_INPUT));
addInput(createInput<...>(mm2px(Vec(inputX, 76.0)), ...TRIGGER_R_INPUT));
addInput(createInput<...>(mm2px(Vec(inputX, 88.0)), ...TRIGGER_GLOBAL_INPUT));

// OUTPUTS (right side, bottom)
float outputX = 90.0f;
addOutput(createOutput<...>(mm2px(Vec(outputX, 108.0)), ...OUT_L_OUTPUT));
addOutput(createOutput<...>(mm2px(Vec(outputX, 120.0)), ...OUT_R_OUTPUT));
```

---

## 🗑️ ELIMINAR BACKUPS OBSOLETOS

**Cuando estés listo** (después de verificar que todo funciona):

```bash
cd ~
./delete_old_backups.sh
# Confirma con 'SI' cuando te lo pida
```

**Esto eliminará**:
- `~/OBSOLETE_AURUM_BACKUPS_TO_DELETE/` (~2GB+ de espacio)
- Todas las versiones antiguas
- Checkpoints obsoletos

**⚠️ ADVERTENCIA**: No se puede deshacer

---

## 🚀 WORKFLOW DE DESARROLLO

### 1. Editar código
```bash
cd ~/AurumLab
code src/QuantumResonatorV3.cpp
# o tu editor preferido
```

### 2. Compilar
```bash
cd ~/AurumLab
make -j4
```

### 3. Instalar
```bash
make install
```

### 4. Testear en Rack2
```bash
# Cerrar Rack2 si está abierto
killall "Rack 2 Pro"

# Abrir de nuevo
open -a "Rack 2 Pro"
```

### 5. Verificar logs (si hay problemas)
```bash
tail -f ~/Library/Application\ Support/Rack2/log.txt
```

---

## 📚 RECURSOS

### Documentación de Rack2 SDK
- https://vcvrack.com/manual/
- https://vcvrack.com/docs-v2/

### Rack2 Plugin Development
- `~/SDK/Rack-SDK/include/` - Headers de la API
- Ejemplos en plugins oficiales de VCV

### DSP References
- Fibonacci resonators: secuencia 1,1,2,3,5,8,13,21...
- Golden Ratio (Φ): 1.618033988749895
- Mandelbrot: Z(n+1) = Z(n)² + C

---

## 🐛 DEBUGGING

### Ver output de compilación
```bash
cd ~/AurumLab
make 2>&1 | tee compile.log
```

### Ver advertencias
```bash
cd ~/AurumLab
make 2>&1 | grep warning
```

### Limpiar y recompilar desde cero
```bash
cd ~/AurumLab
make clean
make -j4
make install
```

### Ver tamaño del plugin
```bash
ls -lh ~/AurumLab/plugin.dylib
du -sh ~/Library/Application\ Support/Rack2/plugins-mac-arm64/AurumLab*
```

---

## ✅ CHECKLIST DE VERIFICACIÓN

Antes de considerar el módulo "completo", verificar:

- [ ] Compila sin errores
- [ ] Aparece en Rack2
- [ ] Osciladores generan audio
- [ ] Resonadores suenan correctamente
- [ ] Modos fractálicos suenan diferentes
- [ ] Modo morph transiciona suavemente
- [ ] Triggers funcionan por canal
- [ ] Delay áureo es audible
- [ ] Reverb de caracol funciona
- [ ] Entrelazamiento cuántico es perceptible
- [ ] Túnel cuántico crea efectos audibles
- [ ] Displays muestran Hz correctamente
- [ ] V/Oct responde apropiadamente
- [ ] CV inputs modulan parámetros
- [ ] No hay artifacts de audio (clicks, pops)
- [ ] CPU usage es razonable (<20% con 1 instancia)
- [ ] Panel UI es claro y usable
- [ ] No hay controles superpuestos

---

## 📞 SIGUIENTE SESIÓN

**Reportar**:
1. ¿El módulo aparece en Rack2?
2. ¿Genera audio?
3. ¿Qué controles están superpuestos?
4. ¿Algún bug o comportamiento extraño?
5. ¿Qué característica quieres mejorar primero?

**Para pantallazos**:
- Tomar captura del módulo en Rack2
- Marcar áreas problemáticas
- Describir comportamiento esperado vs actual

---

**¡El proyecto está limpio y listo para continuar!** 🎉

Solo existe UNA versión: **Quantum Resonator V3** en `~/AurumLab/`

No más confusión de directorios. 
No más mezcla de versiones.
Un solo plugin. Un solo módulo. Fácil de desarrollar.


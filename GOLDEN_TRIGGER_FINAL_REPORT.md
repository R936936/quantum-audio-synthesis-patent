# 🎛️ GOLDEN TRIGGER - REPORTE FINAL
## Módulo de Triggers con Ratio Áureo (φ = 1.618...)

**Fecha:** 15 de Enero 2026
**Versión:** v2.7.0
**Estado:** ✅ COMPLETADO

---

## 📋 ESPECIFICACIONES TÉCNICAS

### **Dimensiones:**
- **Tamaño:** 18 HP
- **Panel:** 345.6 × 485.67 px

### **Arquitectura:**
- **3 Canales independientes** (CH1, CH2, CH3)
- Cada canal genera **9 triggers** (3 triggers × 3 copias A/B/C)
- **27 outputs totales** de triggers
- **27 LEDs rítmicos** (parpadean con triggers activos)

---

## 🎛️ CONTROLES POR CANAL

### **Inputs:**
- **1 Clock Input** (arriba del canal)
  - CH1: +3mm derecha
  - CH2: Centro
  - CH3: -3mm izquierda

- **3 CV Inputs** (modulación de offsets)
  - CV1, CV2, CV3 para cada trigger

### **Knobs:**
- **3 Offset Knobs** (timing de cada trigger)
  - Rango: 0.0 - 1.0 (0% - 100% del periodo de clock)
  - Cada knob controla cuándo dispara su trigger

### **Outputs:**
- **9 Trigger Outputs** por canal (matriz 3×3)
  - Trigger 1: T1A, T1B, T1C (3 copias)
  - Trigger 2: T2A, T2B, T2C (3 copias)
  - Trigger 3: T3A, T3B, T3C (3 copias)

### **LEDs:**
- **9 LEDs por canal** (amarillos)
  - Parpadean cuando el trigger correspondiente está activo
  - Duración del parpadeo = duración del pulso

---

## ⚙️ CONTROL GLOBAL: φ WIDTH

### **Ubicación:** 
Parte inferior del panel, centrado bajo CH2

### **Componentes:**
1. **Botón LED Verde** (izquierda)
   - ON (💚): Pulse width control activo
   - OFF (⚫): Bypass - pulsos ultra-cortos (1ms)

2. **Knob Trimpot Tiny** (derecha)
   - Rango: 0.1ms - 100ms
   - Default: 10ms

---

## 🎵 FUNCIONAMIENTO

### **Con φ WIDTH Activado (Botón Verde):**

El knob controla la **duración base** de los pulsos, aplicada con escala áurea:

```
Trigger 1: Base × φ⁰ = Base × 1.0   (100%)
Trigger 2: Base × φ⁻¹ = Base × 0.618 (61.8%)
Trigger 3: Base × φ⁻² = Base × 0.382 (38.2%)
```

**Ejemplo:** Si φ WIDTH = 10ms
- Trigger 1: 10.0ms
- Trigger 2: 6.18ms
- Trigger 3: 3.82ms

### **Con φ WIDTH Desactivado (Botón Apagado):**

- Todos los pulsos: **1ms fijo** (ultra-cortos)
- Solo el **timing** (offsets) importa
- Comportamiento similar a gates muy breves

---

## 🎼 EJEMPLO DE USO

### **Clock Euclidean + Golden Ratios:**

```
Clock (120 BPM) → CH1 CLK

CH1 Knobs:
  Offset 1: 0.0   → Trigger en beat 1 (10ms)
  Offset 2: 0.618 → Trigger en φ (6.18ms)
  Offset 3: 0.382 → Trigger en φ² (3.82ms)

Resultado:
  3 triggers con timing áureo
  Cada uno con duración áurea
  9 outputs para routing flexible
```

---

## 🔧 POSICIONES FINALES (mm)

### **Clock Inputs (Y=16):**
- CH1: X = 15.24 + 3.0 = **18.24mm**
- CH2: X = 45.72 = **45.72mm** 
- CH3: X = 100.20 - 3.0 = **97.20mm**

### **CV Inputs (Y=25):**
Organizados en columnas A/B/C con offsets graduales

### **Knobs (Y=41):**
Organizados en columnas A/B/C con offsets graduales

### **Outputs (Y=59-83):**
- 3 filas × 3 columnas = 9 outputs
- Espaciado vertical: 12mm entre filas

### **LEDs (Y=95-107):**
- 3 filas × 3 columnas = 9 LEDs
- Espaciado vertical: 6mm entre filas

### **φ WIDTH Control (Y=116):**
- Botón: X = 49.72mm (8mm left of knob)
- Knob: X = 57.72mm

---

## 📊 ESTADÍSTICAS

### **Código:**
- Archivo: `GoldenTrigger.cpp`
- Líneas: ~260
- Parámetros: 11 (9 offsets + 1 width + 1 button)
- Inputs: 13 (9 CV + 3 CLK + 1 RESET)
- Outputs: 30 (27 triggers + 3 gates sin usar)
- LEDs: 28 (27 triggers + 1 button)

### **Constantes Áureas:**
```cpp
PHI = 1.618033988749895f      // φ (documentación)
INV_PHI = 0.618033988749895f  // 1/φ (usado en cálculos)
```

---

## ✅ CARACTERÍSTICAS COMPLETADAS

- [x] 3 canales independientes horizontales
- [x] 9 triggers por canal (3×3 matriz)
- [x] 27 LEDs rítmicos (parpadean con actividad)
- [x] Control global φ WIDTH con escala áurea
- [x] Botón enable/disable para pulse width
- [x] Clock inputs ajustados espaciadamente
- [x] CV modulation para todos los offsets
- [x] Panel minimalista 18HP
- [x] Timing con ratio áureo
- [x] Duraciones con ratio áureo

---

## 🎯 PRÓXIMOS MÓDULOS PLANEADOS

1. **Golden Gates** (companion module)
   - 3 canales de gates con duraciones φ
   - Similar al Golden Trigger pero para gates sostenidos

2. **Matrix Mult 9×3** (ya existe en código)
   - Multiplicador de señales

---

## 📝 NOTAS DE DESARROLLO

### **Iteraciones de Layout:**
- 20+ ajustes de spacing fino
- Optimización visual de columnas
- Balance horizontal entre canales

### **Cambios de Comportamiento:**
- LEDs: De estático (knob position) → rítmico (trigger activity)
- Pulse width: De obligatorio → opcional (con botón)
- Default width: De 1ms → 10ms (más visible)

---

## 🚀 INSTRUCCIONES DE USO

### **Para Añadir el Módulo NUEVO:**

1. ⚠️ **IMPORTANTE:** Borra cualquier instancia vieja del patch
2. Abre el **Module Browser** en VCV Rack
3. Busca: **"Golden Trigger"** o **"Aurum Lab"**
4. Añade el módulo **fresco** al rack
5. El nuevo módulo tendrá:
   - ✅ Knob φ WIDTH tiny (Trimpot) abajo
   - ✅ Botón LED verde al lado del knob
   - ✅ Sin CV input WIDTH
   - ✅ LEDs rítmicos funcionando
   - ✅ Clock inputs espaciados

### **Para Usar:**

1. **Conecta un clock** a CH1/CH2/CH3 CLK
2. **Activa el botón verde** (φ WIDTH enable)
3. **Ajusta el knob φ WIDTH** para duración visible (~10-50ms)
4. **Mueve los offset knobs** para timing diferente
5. **Observa los LEDs** parpadear rítmicamente
6. **Conecta los outputs** a tu patch

---

## 🎨 ESTÉTICA

- **Fondo:** Negro (#1a1a1a)
- **Título:** Dorado (#FFD700) "GOLDEN TRIGGER"
- **Labels:** Gris (#888, #666)
- **Dividers:** Líneas verticales grises entre canales
- **Minimalista:** Solo texto esencial

---

## 🏆 LOGROS

✅ Módulo completamente funcional
✅ Timing basado en ratio áureo (φ)
✅ Duraciones basadas en ratio áureo (φ)
✅ LEDs rítmicos intuitivos
✅ Control bypass para pulse width
✅ Layout balanceado y espaciado
✅ 27 outputs para máxima flexibilidad

---

**Plugin instalado en:** `~/Library/Application Support/Rack2/plugins-mac-arm64/`  
**Archivo:** `AurumLab-2.7.0-mac-arm64.vcvplugin`  
**Última compilación:** 15 Enero 2026, 11:24 AM

---

## 🔄 PARA PRÓXIMA SESIÓN

Si necesitas modificar el módulo, los archivos están en:
- **Código:** `~/Desktop/AurumLab/src/modules/GoldenTrigger.cpp`
- **Panel:** `~/Desktop/AurumLab/res/GoldenTrigger.svg`

Compilar: `cd ~/Desktop/AurumLab && make clean && make -j4 && make dist`

---

**¡Golden Trigger completado! 🎉**

# 🔍 DIAGNÓSTICO: Osciladores Pulsando en lugar de Sostenidos

## ❌ PROBLEMA REPORTADO

Los osciladores oscilan "pulsando" en lugar de ser una oscilación sostenida continua mientras NO interactúan triggers.

**Comportamiento actual:**
- Oscilación tipo "gate/trigger" (pulsos)

**Comportamiento esperado:**
- Oscilación sostenida continua (como oscilador normal)

---

## 🔍 ANÁLISIS DEL CÓDIGO

### Líneas relevantes:

**Línea 2443:** `float spiralL = oscL.process(args.sampleTime) * oscAmount;`
**Línea 2500:** `float spiralR = oscR.process(args.sampleTime) * oscAmount;`
**Línea 2631:** `float spiralCenter = oscCenter.process(args.sampleTime) * oscAmount;`

✅ Los osciladores se procesan **SIEMPRE** (cada sample)

---

### Modulación de amplitud:

**Líneas 2807-2809:**
```cpp
float ampModL = 0.85f + 0.15f * quantumEnergyL;
float ampModC = 0.85f + 0.15f * quantumEnergyC;
float ampModR = 0.85f + 0.15f * quantumEnergyR;
```

**Líneas 2812-2814:** (⚠️ SOSPECHOSO)
```cpp
ampModL *= ampPulseModL;
ampModC *= ampPulseModCenter;
ampModR *= ampPulseModR;
```

**Líneas 2816-2818:**
```cpp
outputs[OUT_L_OUTPUT].setVoltage(outL * 5.f * outputGain * ampModL);
outputs[OUT_R_OUTPUT].setVoltage(outR * 5.f * outputGain * ampModR);
outputs[OUT_CENTER_OUTPUT].setVoltage(outCenter * 5.f * outputGain * ampModC);
```

---

## 🎯 TEORÍA DEL PROBLEMA

Las líneas 2812-2814 multiplican la salida por `ampPulseModL/R/Center`.

### QuantumAmplitudePulse behavior:

```cpp
struct QuantumAmplitudePulse {
    float amount = 0.f;  // ← Inicia en 0
    
    float process() {
        if (amount < minAmount) {
            amount = 0.f;
            return 1.f;  // ← Devuelve 1.0 cuando NO hay pulse
        }
        float output = 1.f + amount;  // ← Cuando hay pulse, devuelve 1 + boost
        amount *= decay;
        return output;
    }
};
```

✅ El struct parece correcto: devuelve 1.0 por defecto.

---

## 🤔 POSIBLES CAUSAS

### Causa 1: Inicialización incorrecta

Si `ampPulseL.amount` NO se inicializa correctamente, podría estar en un estado indefinido.

**Solución:** Verificar inicialización en constructor.

---

### Causa 2: `quantumEnergyL/R/C` empieza en 0

Si `quantumEnergyL` es 0 al inicio:
- `ampModL = 0.85f + 0.15f * 0 = 0.85f` ✅ Debería haber sonido

---

### Causa 3: `oscAmount` está en 0

Si el parámetro `OSC_AMOUNT_PARAM` está en 0 por defecto:
- Línea 2443: `spiralL = oscL.process(...) * 0` = 0 ❌

**Verificar línea 1937:**
```cpp
configParam(OSC_AMOUNT_PARAM, 0.f, 1.f, 0.8f, "Oscillator Amount", "%", 0.f, 100.f);
```

✅ Default es 0.8, no 0.

---

### Causa 4: `outputGain` está en 0

Verificar valor de `outputGain`.

---

### Causa 5: Problema con el mixer

Si el audio pasa por un mixer que requiere triggers para abrir gates.

---

## 💡 HIPÓTESIS MÁS PROBABLE

**El problema NO está en el código de oscilación, sino en:**

1. **Panel UI:** Algún control visual que da la impresión de pulsos
2. **VCV Rack Scope:** Mostrando solo triggers
3. **Conexiones:** Los triggers están conectados a algo que no debería

---

## 🔧 SOLUCIÓN SUGERIDA

### Test 1: Verificar oscAmount

Poner el knob `OSC_AMOUNT` al máximo y probar.

### Test 2: Verificar outputs directos

Conectar `OUT_L`, `OUT_R`, `OUT_CENTER` directamente a VCV Audio.

No usar MIXER outputs primero.

### Test 3: Verificar triggers

Desconectar TODOS los triggers y probar.

### Test 4: Verificar parámetros quantum

Si `Q_COHERENCE`, `Q_SPREAD`, etc. están en 0, el sonido puede ser muy débil.

---

## 📊 ACCIÓN INMEDIATA

**Necesito que me digas:**

1. ¿Qué outputs estás usando? (OUT_L/R/CENTER o MIXER_OUT?)
2. ¿Tienes algo conectado a los triggers?
3. ¿El knob OSC_AMOUNT está arriba?
4. ¿Los knobs de frecuencia están en un rango audible (100-5000 Hz)?
5. ¿Estás viendo el scope de VCV Rack o escuchando audio?

---

**Con esta info podré darte la solución exacta.** 🎯

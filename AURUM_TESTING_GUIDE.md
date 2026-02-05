# 🎹 GUÍA DE TESTING - QuantumSynth Fractal Resonator v4.84

## ✅ ESTADO ACTUAL
- **Plugin:** AurumLab ✅ VISIBLE en VCV Rack
- **Módulo:** QuantumSynth Fractal Resonator
- **Versión:** v4.84
- **Compilación:** ✅ Exitosa (431 KB)

---

## 🎯 PRUEBAS RÁPIDAS (5-10 minutos)

### 1️⃣ PRUEBA BÁSICA DE AUDIO (2 min)

**Setup:**
1. Abre VCV Rack Pro
2. Right-click → Aurum → QuantumSynth Fractal Resonator
3. Añade un módulo de Audio Output (Audio-8 o similar)
4. Conecta **OUT_L** → Audio Output Left

**Prueba:**
- [ ] Ajusta **OSC AMOUNT** (gira el knob)
- [ ] ¿Escuchas una señal de audio? (drone/zumbido)
- [ ] Conecta **OUT_C** → Audio Output Right
- [ ] ¿También hay señal?
- [ ] Conecta **OUT_R** → Audio Output
- [ ] ¿Señal en los 3 outputs?

**Resultado esperado:** ✅ Señal de audio audible en los 3 outputs


### 2️⃣ PRUEBA DE AFINACIÓN V/OCT (2 min)

**Setup:**
1. Añade un módulo MIDI-CV (MIDI → CV)
2. Conecta tu teclado MIDI
3. Conecta **MIDI-CV V/OCT** → **QuantumSynth V/OCT input**

**Prueba:**
- [ ] Toca nota C4 (Do central)
- [ ] ¿Suena aproximadamente 261.63 Hz?
- [ ] Toca C5 (una octava arriba)
- [ ] ¿Suena el doble de frecuencia?
- [ ] Toca C3 (una octava abajo)
- [ ] ¿Suena la mitad de frecuencia?

**Resultado esperado:** ✅ V/Oct tracking correcto (cada octava = 2x frecuencia)


### 3️⃣ PRUEBA DE PARÁMETROS CUÁNTICOS (3 min)

**Q-SPREAD (Dispersión Cuántica):**
- [ ] Gira **Q-SPREAD** de 0% a 100%
- [ ] ¿El sonido se vuelve más "disperso" o "ancho"?

**Q-COHERENCE (Coherencia):**
- [ ] Gira **Q-COHERENCE** de 0% a 100%
- [ ] ¿El sonido se vuelve más "enfocado" o cambia?

**Q-EVOLUTION (Evolución):**
- [ ] Gira **Q-EVOLUTION** de 0% a 100%
- [ ] ¿El timbre evoluciona/cambia con el tiempo?

**Q-DECOHERENCE:**
- [ ] Ajusta **Q-DECOHERENCE**
- [ ] ¿Afecta la "estabilidad" del sonido?

**Q-TUNNEL:**
- [ ] Ajusta **Q-TUNNEL**
- [ ] ¿Afecta el carácter del sonido?

**Resultado esperado:** ✅ Cada parámetro modula el sonido de forma audible


### 4️⃣ PRUEBA DE MODOS FRACTALES (2 min)

**Setup:**
- Mantén el audio conectado
- Toca una nota sostenida

**Prueba cada modo:**
- [ ] **Fibonacci:** Selector → Fibonacci
  - ¿Sonido con proporciones áureas?
  
- [ ] **Golden Ratio:** Selector → Golden Ratio
  - ¿Carácter diferente al anterior?
  
- [ ] **Mandelbrot:** Selector → Mandelbrot
  - ¿Sonido más complejo/fractal?
  
- [ ] **Morphing:** Selector → Morphing
  - ¿El sonido evoluciona/cambia?

**Resultado esperado:** ✅ Cada modo produce un carácter tímbrico diferente


### 5️⃣ PRUEBA DE DISPLAYS (1 min)

**Verifica que los displays muestren:**
- [ ] Frecuencia del oscilador L (aprox Hz)
- [ ] Frecuencia del oscilador C (aprox Hz)
- [ ] Frecuencia del oscilador R (aprox Hz)
- [ ] Los valores cambian al tocar notas diferentes

**Resultado esperado:** ✅ Displays actualizados y con valores razonables

---

## 📊 CHECKLIST COMPLETO

### SISTEMA DE OSCILACIÓN
- [ ] OUT_L genera señal ✅
- [ ] OUT_C genera señal ✅
- [ ] OUT_R genera señal ✅
- [ ] OSC AMOUNT modula volumen ✅
- [ ] V/Oct tracking correcto ✅

### RESONADOR FRACTAL
- [ ] Fibonacci mode funciona ✅
- [ ] Golden Ratio mode funciona ✅
- [ ] Mandelbrot mode funciona ✅
- [ ] Morphing mode funciona ✅

### PARÁMETROS CUÁNTICOS
- [ ] Q-SPREAD modula (0-100%) ✅
- [ ] Q-EVOLUTION modula (0-100%) ✅
- [ ] Q-COHERENCE modula (0-100%) ✅
- [ ] Q-DECOHERENCE modula ✅
- [ ] Q-TUNNEL modula ✅

### OUTPUTS
- [ ] OUT_L tiene señal ✅
- [ ] OUT_C tiene señal ✅
- [ ] OUT_R tiene señal ✅
- [ ] MIXER tiene señal ✅

### DISPLAYS
- [ ] Display L muestra frecuencia ✅
- [ ] Display C muestra frecuencia ✅
- [ ] Display R muestra frecuencia ✅

---

## 🐛 TROUBLESHOOTING

### ❌ No hay señal de audio
**Posibles causas:**
1. OSC AMOUNT está en 0 → Sube el knob
2. Osciladores apagados → Verifica switches
3. Cable no conectado → Revisa conexiones

### ❌ Afinación incorrecta
**Posibles causas:**
1. V/Oct no conectado → Conecta MIDI-CV
2. Frecuencia base incorrecta → Revisar código
3. Escala no calibrada → Ajustar tracking

### ❌ Parámetros no modulan
**Posibles causas:**
1. Rango muy sutil → Aumentar sensitivity
2. Parámetro no conectado en DSP → Revisar código
3. Valores fuera de rango → Verificar params

### ❌ Displays no actualizan
**Posibles causas:**
1. Update rate muy bajo → Aumentar frecuencia
2. Variables no conectadas → Revisar código
3. Formato incorrecto → Ajustar displays

---

## 💡 PRUEBA CREATIVA (BONUS)

**Patch Recomendado:**
```
MIDI-CV → QuantumSynth V/OCT
LFO → Q-SPREAD CV
LFO → Q-COHERENCE CV
ENV → Q-EVOLUTION CV
OUT_L → Reverb → Audio
OUT_C → Delay → Audio
OUT_R → Filter → Audio
```

**Resultado:** Paisaje sonoro cuántico evolutivo 🌌

---

## 📋 REPORTE DE RESULTADOS

**Copia y pega este template:**

```
🎹 REPORTE DE TESTING - QuantumSynth v4.84

✅ Funciona perfectamente:
- 

⚠️ Funciona pero con issues:
- 

❌ No funciona:
- 

💡 Sugerencias:
- 

🎵 Impresión general:
[Tu feedback aquí]
```

---

## 🎯 PRÓXIMOS PASOS SEGÚN RESULTADOS

### Si TODO FUNCIONA ✅
→ ¡A celebrar! 🎉
→ Crear patches creativos
→ Documentar sonidos únicos
→ Preparar para release

### Si HAY ISSUES MENORES ⚠️
→ Identificar qué falla
→ Ajustar parámetros
→ Re-compilar
→ Re-testear

### Si HAY ISSUES MAYORES ❌
→ Reporte detallado
→ Debug específico
→ Fix código
→ Nueva compilación

---

**¿Listo para testear? 🚀🎵**

Abre VCV Rack y sigue esta guía paso a paso.
¡Reporta tus resultados cuando termines! 🎹✨

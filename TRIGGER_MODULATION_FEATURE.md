╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║      🎯 TRIGGER MODULATION - NUEVA FEATURE GOLDEN OSCILLATOR V2      ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

📅 Implementado: 17 Enero 2026
🎛️ Módulo: Golden Oscillator V2
✨ Feature: Sample & Hold por Trigger

═══════════════════════════════════════════════════════════════════════

🎯 CONCEPTO:

Ahora TODOS los parámetros (excepto 1V/Oct y Fine Tune) pueden ser 
controlados por TRIGGERS además de CV continuo.

Al recibir un trigger:
  1. Sample el valor actual (knob + CV)
  2. Hold ese valor hasta el próximo trigger
  3. Ignora cambios en knob/CV mientras está en modo trigger

═══════════════════════════════════════════════════════════════════════

🎛️ PARÁMETROS CON TRIGGER INPUT:

✅ Spiral Rate
✅ Spiral Depth
✅ Spiral Complexity
✅ Spiral Shape
✅ Mode Morph
✅ Resonance Depth
✅ Resonance Feedback
✅ Chaos

═══════════════════════════════════════════════════════════════════════

🔌 COMPORTAMIENTO:

┌──────────────────────────────────────────────────────────────────────┐
│ SIN TRIGGER CONECTADO:                                               │
│   → CV modulation continua (comportamiento normal)                   │
│   → Knob + CV suman en tiempo real                                   │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│ CON TRIGGER CONECTADO:                                               │
│   → Valor se congela hasta próximo trigger                           │
│   → Sample: knob + CV en el momento del trigger                      │
│   → Hold: mantiene valor aunque muevas knob/CV                       │
└──────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════

🎵 CASOS DE USO:

1. CAMBIOS RÍTMICOS CUANTIZADOS
   ┌────────────────────────────────────────────────────────────────┐
   │ Trigger: Clock (4/4)                                           │
   │ Parámetro: Mode Morph                                          │
   │                                                                │
   │ Beat 1: Fibonacci (sampled en trigger)                         │
   │ Beat 2: Golden Ratio (sampled en trigger)                      │
   │ Beat 3: Mandelbrot (sampled en trigger)                        │
   │ Beat 4: Back to Fibonacci                                      │
   │                                                                │
   │ Resultado: Evolución tímbrica sincronizada con beat            │
   └────────────────────────────────────────────────────────────────┘

2. EUCLIDEAN MODULATION
   ┌────────────────────────────────────────────────────────────────┐
   │ Trigger: Euclidean pattern [x . x . x . . .]                   │
   │ Parámetro: Spiral Depth                                        │
   │ CV: Random voltage                                             │
   │                                                                │
   │ En cada trigger: nuevo valor random de AM                      │
   │ Entre triggers: valor se mantiene                              │
   │                                                                │
   │ Resultado: Pulsación rítmica con valores aleatorios            │
   └────────────────────────────────────────────────────────────────┘

3. STEP SEQUENCING DE TIMBRE
   ┌────────────────────────────────────────────────────────────────┐
   │ Trigger: Step sequencer gate                                   │
   │ Parámetros: Chaos + Resonance Depth                            │
   │ CV: Sequence voltages                                          │
   │                                                                │
   │ Step 1: Chaos=0.2, Depth=0.3                                   │
   │ Step 2: Chaos=0.5, Depth=0.7                                   │
   │ Step 3: Chaos=1.0, Depth=1.0                                   │
   │ Step 4: Chaos=0.1, Depth=0.1                                   │
   │                                                                │
   │ Resultado: Secuencia tímbrica precisa                          │
   └────────────────────────────────────────────────────────────────┘

4. RANDOM MUTATIONS
   ┌────────────────────────────────────────────────────────────────┐
   │ Trigger: Random triggers (Turing Machine)                      │
   │ Parámetros: ALL (8 parámetros)                                 │
   │ CV: 8 random voltages                                          │
   │                                                                │
   │ Cada trigger = nueva "mutación" completa del sonido            │
   │ Mantiene coherencia entre triggers                             │
   │                                                                │
   │ Resultado: Evolución generativa controlada                     │
   └────────────────────────────────────────────────────────────────┘

5. SWING/GROOVE MODULATION
   ┌────────────────────────────────────────────────────────────────┐
   │ Trigger: Swing clock (alternating timing)                      │
   │ Parámetro: Spiral Rate                                         │
   │ CV: Alternating voltages (0.2V / 0.8V)                         │
   │                                                                │
   │ On-beat: Slow AM                                               │
   │ Off-beat: Fast AM                                              │
   │                                                                │
   │ Resultado: Groove orgánico en la pulsación                     │
   └────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════

🔧 IMPLEMENTACIÓN TÉCNICA:

Cada parámetro tiene:
  - SchmittTrigger: Detecta rising edge (threshold 0.1V)
  - Sampled value: Almacena último valor sampledado
  - Conditional logic: if (trigger connected) → use sampled, else → normal

Ventajas:
  ✅ Zero latency (detection en process())
  ✅ Per-parameter control (mezcla trigger + CV normal)
  ✅ Backwards compatible (si no conectas trigger, funciona normal)
  ✅ Combinable con CV (knob + CV se samplea juntos)

═══════════════════════════════════════════════════════════════════════

🎹 PATCHING EXAMPLES:

BÁSICO: Random timbral steps
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Clock → Chaos Trigger                                              │
│  Random → Chaos CV                                                  │
│                                                                     │
│  Resultado: Chaos cambia aleatoriamente en cada beat                │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

INTERMEDIO: Morphing secuenciado
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Sequencer Gate → Mode Morph Trigger                                │
│  Sequencer CV (0V, 0.5V, 1V) → Mode Morph CV                        │
│                                                                     │
│  Resultado: Sequence de Fibonacci → Golden → Mandelbrot             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

AVANZADO: Generative patch completo
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Master Clock → [Divider] → Triggers a 8 parámetros                 │
│  8× Random sources → CVs de cada parámetro                          │
│  Probability gates → Control qué triggers pasan                     │
│                                                                     │
│  Resultado: Sistema generativo con mutaciones controladas           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════

⚡ VENTAJAS vs CV CONTINUO:

TRIGGER S&H:
  ✅ Cambios cuantizados en tiempo
  ✅ Valores estables entre cambios
  ✅ Perfecto para secuencias/patterns
  ✅ Reproducible (mismo trigger = mismo resultado)

CV CONTINUO:
  ✅ Modulación suave
  ✅ LFO/envelope shaping
  ✅ Transiciones graduales
  ✅ Control expresivo en tiempo real

COMBINACIÓN:
  🔥 Usa ambos: trigger para timing, CV para modulación adicional
  🔥 Ejemplo: Trigger step sequence + CV slow LFO = evolución lenta
              dentro de steps rítmicos

═══════════════════════════════════════════════════════════════════════

📝 NOTAS DE IMPLEMENTACIÓN:

• NOTA: Panel NO modificado aún - triggers NO visibles
• Para usar: patch directamente en código o espera panel update
• Todos los inputs están funcionales en el backend
• Next step: Añadir jacks al panel SVG

INPUTS TOTALES AHORA:
  - 1× V/Oct
  - 8× CV continuo
  - 8× Trigger (sample & hold)
  = 17 inputs totales (vs 9 anteriores)

═══════════════════════════════════════════════════════════════════════

🚀 ESTADO:

✅ Código implementado
✅ Compilado sin errores
⏳ Panel SVG (pendiente - triggers no visibles aún)
⏳ Testing en VCV Rack

═══════════════════════════════════════════════════════════════════════

💡 FILOSOFÍA DE DISEÑO:

"El oscilador ahora no solo responde a voltaje continuo, sino también
 a eventos discretos en el tiempo. Esto abre un nuevo paradigma de
 modulación rítmica donde el timbre evoluciona sincronizado con el beat,
 combinando lo mejor de síntesis continua y síntesis granular."

═══════════════════════════════════════════════════════════════════════

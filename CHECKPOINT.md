Checkpoint – Engine V2 Quantum-Fractal

Fecha: 2025-09-05

Estado
- Núcleo V2 activado por defecto: osciladores L/R → síntesis fractálica continua → banco modal V2 → capa cuántica → post.
- Modos fractálicos: Fibonacci, Áurico (Golden), Mandelbrot y Morph entre ellos.
- Cuántico integrado:
  - Superposición (Q_SUPER): mezcla equal‑power que afecta f y g del espectro (y endurece la forma de la espiral).
  - Entrelazamiento (Q_ENT): mezcla equal‑power de osciladores L/R y ensanchamiento suave de pesos de modo.
  - Colapso: TRIG_X1 o drift alto; rampa logística hacia el modo alterno más afín (sin pulsos).
- Anti‑pulsos: spacing mínimo entre parciales, normalización por canal, suavizado de g_i, offset de fase fractal suavizado, AGC lento.
- Controles nuevos: Spiral Shape, Spiral PM, Q Mode (selector 0=Superposición,1=Entrelazamiento,2=Colapso).
- Debug: TRIG_X2 vuelca /tmp/aurum_v2_dump.json con fi/gi por parcial para corroborar fórmulas.

Próximo
- Afinar pesos por modo (σ Fibo, ventana φ, patrón Mandel) contra espectros esperados.
- Selector de alterno por afinidad completa (ponderada por energía) y granular fractal opcional.


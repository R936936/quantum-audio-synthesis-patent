# GOLDEN TRIGGER V2 - MEJORAS FRACTALES Y TAP TEMPO

## 🎯 OBJETIVOS

1. **TAP TEMPO Button** - Sincronización tipo DJ
   - Botón para tap manual
   - Detecta BPM promedio de 2-4 taps
   - Genera clock interno a ese BPM
   - LED indicador de tempo

2. **FRACTAL RHYTHM Generator**
   - Switch/Button para 4 modos fractales:
     * Sierpinski Triangle - Patrón subdivisión triangular
     * Koch Curve - Patrón subdivisión 4 partes
     * Cantor Set - Patrón subdivisión binaria con silencios
     * Dragon Curve - Patrón alternante izq/derecha
   - Genera patrones rítmicos matemáticamente coherentes
   - Usa offsets existentes para timing

3. **Mantener funcionalidad actual**
   - 3 canales independientes
   - 9 outputs por canal (3x3 grid)
   - 3 offsets por canal
   - Pulse width global

## 🔧 IMPLEMENTACIÓN

### TAP TEMPO
```cpp
- Botón TAP (momentary)
- Almacena últimos 4 tap times
- Calcula BPM promedio
- Output SYNC clock a ese BPM
- LED pulsa al tempo
```

### FRACTAL MODES
```cpp
- Switch de 4 posiciones (o rotativo)
- Cada modo genera patrón único:
  
  SIERPINSKI (nivel 3):
  - 27 triggers en patrón triangular
  - Usa offsets: 0, 1/3, 2/3
  
  KOCH (nivel 2):
  - 16 triggers en patrón de 4 subdivisiones
  - Usa offsets: 0, 1/4, 1/2, 3/4
  
  CANTOR (nivel 3):
  - 8 triggers con silencios (1/3 medio removido)
  - Usa offsets: 0, 1/9, 2/9, 6/9, 7/9, 8/9
  
  DRAGON (nivel 3):
  - 8 triggers en patrón L-R alternante
  - Usa offsets: 0, 1/8, 3/8, 5/8, 7/8
```

### LAYOUT
```
CH1           CH2           CH3
[CLOCK]      [CLOCK]      [CLOCK]
[3x3 OUT]    [3x3 OUT]    [3x3 OUT]
[OFFSET1-3]  [OFFSET1-3]  [OFFSET1-3]
[LEDs]       [LEDs]       [LEDs]

GLOBAL:
[TAP TEMPO] button + LED
[FRACTAL MODE] switch (4 pos)
[PULSE WIDTH] knob
[SYNC OUT] output
```

## 📊 PARÁMETROS NUEVOS

- TAP_BUTTON (momentary)
- FRACTAL_MODE (0-3: Sierpinski, Koch, Cantor, Dragon)
- SYNC_OUTPUT (clock sincronizado)
- TAP_LED (indicador tempo)

## 🎵 FILOSOFÍA

Los fractales generan ritmos **matemáticamente perfectos**:
- Auto-similares a diferentes escalas
- Subdivisiones coherentes
- Patrones complejos de triggers simples
- Offsets golden ratio + fractales = ritmos únicos

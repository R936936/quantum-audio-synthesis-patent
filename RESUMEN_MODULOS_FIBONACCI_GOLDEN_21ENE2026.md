# 🎯 MÓDULOS ACTUALIZADOS - 21 ENERO 2026

## ✅ FIBONACCI CLOCK - BOTÓN SYNC

### Funcionalidad:
**Botón SYNC** (centro inferior del módulo) - Sincroniza los 3 canales

**¿Qué hace?**
- Resetea las 3 fases (`phase[0]`, `phase[1]`, `phase[2]`) a 0
- Los 3 clocks disparan al mismo tiempo
- **EMPATA/SINCRONIZA** los BPMs para que toquen juntos

**Uso típico:**
1. Configura BPMs diferentes en CH1, CH2, CH3
2. Dejas correr... se desincroniza
3. **Presionas SYNC** → ¡Todos vuelven a disparar juntos!
4. Efecto "DJ" - emparejar beats

**Ubicación:**
- Centro bottom del panel triangular
- Botón LED verde

---

## ✅ GOLDEN TRIGGER - MODOS FRACTALES

### Funcionalidad:
**Knob FRACTAL MODE** por cada canal (debajo de los 3 offset knobs)

**5 Modos** (gira el knob 0-4):

### 0 - NORMAL
```
Comportamiento actual
3 grupos de 3 triggers
Offsets: Golden ratio (0, 1/φ, 1-1/φ)
```

### 1 - SIERPINSKI TRIANGLE
```
Patrón: Subdivisión triangular (nivel 2)
9 triggers en:
  0, 1/9, 2/9, 3/9, 4/9, 5/9, 6/9, 7/9, 8/9
Ritmo: Uniforme pero denso
Efecto: Fills rítmicos complejos
```

### 2 - KOCH CURVE
```
Patrón: 4 subdivisiones con gaps
9 triggers en:
  0, 1/16, 2/16, 4/16, 5/16, 6/16, 8/16, 10/16, 12/16
Ritmo: Irregular con silencios
Efecto: Syncopation matemática
```

### 3 - CANTOR SET
```
Patrón: Tercio medio removido
9 triggers en:
  0, 1/27, 2/27, [SILENCE], [SILENCE], [SILENCE], 18/27, 19/27, 20/27
Ritmo: 3 triggers - pausa - 3 triggers
Efecto: Gaps fractales (triggers 4-6 mudos)
```

### 4 - DRAGON CURVE
```
Patrón: Alternancia L-R asimétrica
9 triggers en:
  0, 1/8, 3/8, 4/8, 5/8, 7/8, 2/8, 6/8, 0
Ritmo: Irregular alternante
Efecto: Ritmos complejos no repetitivos
```

---

## 🎵 CÓMO USAR:

### FIBONACCI CLOCK:
1. Configura BPMs diferentes (ej: 8, 55, 144)
2. Conecta outputs a secuenciadores/drums
3. Cuando se desincroniza, **presiona SYNC**
4. Todos los clocks tocan juntos otra vez

### GOLDEN TRIGGER:
1. Conecta clock al CH1 input
2. Gira el knob **FRACTAL MODE** (debajo de offset knobs)
   - 0 = Normal
   - 1 = Sierpinski (denso)
   - 2 = Koch (sparse)
   - 3 = Cantor (con gaps)
   - 4 = Dragon (asimétrico)
3. Los 9 outputs generan patrón fractal
4. Usa outputs para triggers de drums/envelopes

---

## 📊 COMPARACIÓN MODOS:

| Mode | Triggers | Spacing | Carácter |
|------|----------|---------|----------|
| **Normal** | 9 | Golden ratio | Orgánico |
| **Sierpinski** | 9 | Uniforme 1/9 | Denso |
| **Koch** | 9 | Gaps irregulares | Syncopado |
| **Cantor** | 6 (3 mudos) | Tercio silencio | Con pausas |
| **Dragon** | 9 | Asimétrico | Complejo |

---

## 🔧 PENDIENTE PARA SIGUIENTE SESIÓN:

### Quantum Elastic Kick:
- ⚠️ Click del clock todavía se filtra
- Posible solución: DC blocker en input
- O revisar Schmitt trigger threshold
- Dejar para después

### Golden Trigger:
- ✅ Fractal modes implementados
- Próximo: Labels en SVG para modos
- Próximo: Visualización LED patrón

### Fibonacci Clock:
- ✅ SYNC button funcionando
- Próximo: Input de clock externo para sync
- Próximo: BPM readout más grande

---

## 🚀 COMMITS:

```bash
git add src/FibonacciClock.cpp
git commit -m "FibonacciClock: Add SYNC button to match all 3 channels"

git add src/GoldenTrigger.cpp
git commit -m "GoldenTrigger: Add fractal modes (Sierpinski, Koch, Cantor, Dragon)"
```

# Technical Specifications - Quantic Resonator V2 Improvements
## Engineering Documentation

---

## 🔬 Multi-Layer Spiral Oscillator

### Architecture
```cpp
struct SpiralWaveOscillator {
    float phase;              // Main carrier phase [0, 1)
    float spiralPhase;        // Base spiral phase [0, 1)
    float layerPhases[3];     // Three interacting spiral layers
    float frequency;          // Carrier frequency (Hz)
    
    // Control parameters
    float spiralRate;         // Spiral rotation speed [0.001, 0.1]
    float spiralDepth;        // AM modulation depth [0, 1]
    float spiralComplexity;   // Harmonic richness [0, 1]
    float spiralShape;        // Waveform morph [0, 1]
};
```

### Phase Update Equations
```
phase += f × Δt
layer[0] += spiralRate × Δt × 1.0
layer[1] += spiralRate × Δt × φ
layer[2] += spiralRate × Δt × φ²

where φ = 1.618033988749895 (golden ratio)
```

### Radius Calculation (Multi-Layer)
```
r₁ = 0.5 + 0.5 × sin(2π × layer[0])
r₂ = 0.5 + 0.5 × sin(2π × layer[1])
r₃ = 0.5 + 0.5 × sin(2π × layer[2])

combined = (r₁ + r₂×c×0.5 + r₃×c×0.25) / (1 + c×0.75)

where c = spiralComplexity ∈ [0, 1]
```

### Phase Modulation
```
PM = PM₁ + PM₂ + PM₃

PM₁ = 0.3 × sin(2π × layer[0] × φ)
PM₂ = 0.15 × c × sin(2π × layer[1] × φ⁻¹)
PM₃ = 0.075 × c × sin(2π × layer[2])
```

### Waveform Morphing Function
```
shape ∈ [0.00, 0.25): sine
shape ∈ [0.25, 0.50): lerp(sine, enhanced_sine)
shape ∈ [0.50, 0.75): lerp(enhanced_sine, triangle)
shape ∈ [0.75, 1.00]: lerp(triangle, saw)

where:
enhanced_sine = sine + 0.3×sin(4πφ) + 0.2×sin(6πφ)
triangle = 4|φ - floor(φ + 0.5)| - 1
saw = 2(φ - floor(φ + 0.5))
```

### Fibonacci Harmonic Enhancement
```
if complexity > 0.1:
    harmonic = 0.1×c×sin(2πφ×2)      // F(2)
             + 0.06×c×sin(2πφ×3)     // F(3)
             + 0.04×c×sin(2πφ×5)     // F(4)
```

### Final Output
```
output = (baseWave + harmonics) × amplitude × 3.0
output = tanh(output × 0.8) × 1.25  // Soft saturation
```

---

## 🎭 Circular Morphing System

### Window Functions
```
θ = morph × 2π

W_fib(θ) = cos²(θ)
W_gold(θ) = cos²(θ - 2π/3)
W_mandel(θ) = cos²(θ - 4π/3)

// Normalize
sum = W_fib + W_gold + W_mandel
W_fib /= sum
W_gold /= sum
W_mandel /= sum
```

### Blending Formula
```
param_morphed = param_fib × W_fib(θ)
              + param_gold × W_gold(θ)
              + param_mandel × W_mandel(θ)
```

### Applied To:
1. **Partial Frequencies**: `f_k(baseFreq, k, morph)`
2. **Fractal Weights**: `w_k(k, morph)`
3. **Q Values**: `Q_k(k, morph)`

### Mathematical Properties
- **Continuity**: C∞ (infinitely differentiable)
- **Periodicity**: θ + 2π = θ
- **Symmetry**: 120° rotational symmetry
- **Coverage**: Σ W_i(θ) = 1 ∀θ

---

## 🔊 Resonator Bank Calibrations

### Mode-Specific Q Values

#### Fibonacci Mode
```cpp
Q_base = 12.0
Q_bonus = (partial % 3 == 0) ? 10.0 : 5.0
fib_factor = FIBONACCI[min(partial, 15)] / 377.0
Q_fib = (Q_base + Q_bonus) × (1 + 0.2 × fib_factor)

Range: [12, 27]
Character: Emphasizes Fibonacci-indexed partials
```

#### Golden Ratio Mode
```cpp
Q_base = 15.0
Q_linear = partial × 2.5
Q_exp = φ^(partial × 0.1)
Q_golden = (Q_base + Q_linear) × Q_exp

Range: [15, 35]
Character: Smooth exponential growth, cleanest sound
```

#### Mandelbrot Mode
```cpp
chaos = 0.5 + 0.5 × sin(partial × 2.3)
Q_base = 10.0 + 15.0 × chaos
Q_mod = 1.0 + 0.3 × cos(partial × φ)
Q_mandel = Q_base × Q_mod

Range: [10, 25]
Character: Chaotic variation, complex spectrum
```

#### Morph Mode
```cpp
Q_fib = /* as above */
Q_golden = /* as above */
Q_mandel = /* as above */

θ = morph × 2π
Q_morph = circular_blend(Q_fib, Q_golden, Q_mandel, θ)
```

### Gain Multipliers
```cpp
Fibonacci:   4.5×
Golden:      5.0×  (cleanest → loudest)
Mandelbrot:  3.5×  (controlled chaos)
```

---

## 📐 Fractal Weight Functions

### Fibonacci Weights
```cpp
if partial < 15:
    fib_value = FIBONACCI[partial]
    weight = 1 / √(1 + fib_value × 0.1)
else:
    weight = 1 / (1 + (partial - 14) × 1.5)
```

### Golden Ratio Weights
```cpp
weight = (φ⁻¹)^(partial × 0.6)
       = 0.618^(partial × 0.6)
```

### Mandelbrot Weights
```cpp
base_decay = 1 / (1 + partial × 0.5)
chaos = 0.5 + 0.5 × sin(partial × e)
chaos *= 0.5 + 0.5 × cos(partial × φ × 1.3)
weight = base_decay × (0.7 + 0.3 × chaos)
```

---

## 🌊 Partial Frequency Formulas

### Fibonacci Mode
```cpp
if partial == 0:
    return baseFreq

if partial < 14:
    // Accumulated Fibonacci ratios
    accumulated = 1.0
    for k in 1..partial:
        accumulated *= F(k+1) / F(k)
    
    // Compress growth
    accumulated = accumulated^0.4
    return baseFreq × accumulated
else:
    // Continue with phi series
    return baseFreq × φ^((partial - 13) × 0.5) × 7.0
```

### Golden Ratio Mode
```cpp
exponent = partial × 0.333
return baseFreq × φ^exponent
```

### Mandelbrot Mode
```cpp
harmonic = baseFreq × (partial + 1)  // Base harmonic

// Map to Mandelbrot set
angle = partial × φ × 2π
radius = 0.3 + 0.4 × (partial / NUM_PARTIALS)

cx = -0.5 + radius × cos(angle)
cy = radius × sin(angle)

// Iterate Mandelbrot
zx = zy = 0
for iter in 0..29:
    if zx² + zy² > 4:
        escape_time = iter
        break
    zx_new = zx² - zy² + cx
    zy = 2×zx×zy + cy
    zx = zx_new

// Map escape time to detuning
chaos = escape_time / 30.0
detuning = 1.0 + (chaos - 0.5) × 0.15  // ±7.5%

return harmonic × detuning
```

---

## 🎛️ Parameter Specifications

### Spiral Controls

| Parameter | Range | Default | Unit | Description |
|-----------|-------|---------|------|-------------|
| Spiral Rate | 0.001 - 0.1 | 0.01 | - | Spiral rotation speed |
| Spiral Depth | 0.0 - 1.0 | 0.5 | % | AM modulation depth |
| **Spiral Complexity** | **0.0 - 1.0** | **0.5** | **%** | **Harmonic richness** |
| **Spiral Shape** | **0.0 - 1.0** | **0.0** | **%** | **Waveform morph** |

### Quantum Controls

| Parameter | Range | Default | Unit | Description |
|-----------|-------|---------|------|-------------|
| Q-Spread | 0.0 - 1.0 | 0.5 | % | Distribution width |
| Q-Evolution | 0.0 - 1.0 | 0.3 | % | Evolution rate |
| Q-Coherence | 0.0 - 1.0 | 0.7 | % | Interference strength |

### Effects Controls

| Parameter | Range | Default | Unit | Description |
|-----------|-------|---------|------|-------------|
| Delay Amount | 0.0 - 1.0 | 0.3 | % | Feedback amount |
| Delay Iterations | 1 - 8 | 3 | - | Number of taps |
| Reverb Feedback | 0.0 - 1.0 | 0.5 | % | Reverb decay |
| Reverb Mix | 0.0 - 1.0 | 0.3 | % | Wet/dry mix |

---

## 📊 Performance Characteristics

### Computational Complexity
```
Per sample:
- Oscillator: O(1) + O(complexity)
- Resonator: O(NUM_PARTIALS) = O(8)
- Delay: O(MAX_ITERATIONS) ≤ O(8)
- Reverb: O(NUM_TAPS) = O(8)

Total: O(32) operations per sample
```

### Memory Usage
```
Oscillator:     ~60 bytes
Resonator Bank: ~400 bytes
Delay Lines:    2 × 8 × 384KB = 6MB
Reverb:         2 × 8 × 384KB = 6MB

Total per instance: ~12 MB
```

### Latency
```
Processing: < 1 sample (real-time)
Delay: User-controlled (50-200ms typical)
Reverb: 2-200ms (Fibonacci-spaced)
```

---

## 🔢 Mathematical Constants

```cpp
PHI = 1.618033988749895      // Golden ratio
INV_PHI = 0.618033988749895  // 1/φ
E = 2.71828182845905         // Euler's number

FIBONACCI = {
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
    89, 144, 233, 377, 610, 987
}
```

---

## ✅ Validation Criteria

### Audio Quality
- [ ] No audible clicks or pops
- [ ] No DC offset
- [ ] No aliasing artifacts
- [ ] Stable at all parameter settings

### Morphing
- [ ] Smooth transitions (no jumps)
- [ ] Continuous timbral evolution
- [ ] Cyclic behavior (0 = 1)

### Complexity
- [ ] 0.0: Clean, simple tone
- [ ] 0.5: Rich, complex timbre
- [ ] 1.0: Dense, full spectrum

### Shape
- [ ] 0.0: Pure sine character
- [ ] 0.5: Balanced brightness
- [ ] 1.0: Aggressive saw character

---

## 🔧 Troubleshooting

### Issue: Distortion at high complexity
**Solution**: Reduce OSC_AMOUNT or enable soft saturation

### Issue: Morphing sounds discontinuous
**Solution**: Verify circular window normalization

### Issue: Weak output
**Solution**: Check mode-specific gain multipliers

### Issue: Excessive CPU usage
**Solution**: Reduce Q values or disable reverb

---

*Technical Specification Document*
*Quantum Fractal Resonator V2*
*Version: 2.0.3 Enhanced*
*Date: October 2, 2025*

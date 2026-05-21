---
sticker: emoji//1f300
tags:
  - concept
  - chaos
  - prng
---
# Concept 03 — Chaotic Maps

> What a chaotic map is, why iterating it produces a random-looking sequence, and how that sequence becomes an encryption key stream.

---

## One-line definition

**A chaotic map is a math function you keep applying to a state. The output sequence looks random, but it's fully deterministic — if you know the starting state, you get the same sequence every time. This determinism + apparent randomness is what makes it usable as an encryption key stream.**

---

## What "chaos" actually means

In math, **chaos** has three precise properties:

1. **Deterministic.** No randomness in the function itself. Given the same inputs, you always get the same outputs.
2. **Sensitive to initial conditions.** Change the starting state by an arbitrarily small amount (say, 10⁻¹⁵) and after enough iterations, the trajectory diverges completely.
3. **Aperiodic.** The sequence never settles into a repeating cycle (or if it does, the cycle is astronomically long).

Together these properties mean: chaos *looks* random because tiny initial differences blow up unpredictably, but it *isn't* random — anyone with the exact starting state can reproduce the sequence.

This is exactly what encryption needs: a sender and receiver who share the key can both compute the same "random" sequence, but an attacker without the key cannot predict it.

---

## The simplest example: the logistic map

To get the idea before jumping to the paper's 3D map, here's the simplest chaotic system — the **logistic map**:

$$
x_{n+1} = r \cdot x_n \cdot (1 - x_n)
$$

Pick `r = 3.9` and `x₀ = 0.5`. Iterate:

| n | xₙ |
|---|---|
| 0 | 0.5000 |
| 1 | 0.9750 |
| 2 | 0.0951 |
| 3 | 0.3358 |
| 4 | 0.8696 |
| 5 | 0.4423 |
| 6 | 0.9618 |
| 7 | 0.1432 |
| ... | ... |

Looks random. But change `x₀` from `0.5` to `0.500000000000001` (perturbation of 10⁻¹⁵) and after 50 iterations the two sequences are completely different.

That perturbation sensitivity is the **encryption gold**: the key is the starting value, and even an attacker who guesses the right *function* and the right *parameter `r`* can't get the right sequence without the right `x₀`.

---

## The paper's 3D chaotic map

The paper uses a **3-variable** discrete chaotic map. It takes a state vector `(x, y, z)` and 6 parameters `(a, b, c, d, e, f)` and produces a new state `(x', y', z')`.

The paper labels this **Equation 1** but the exact form is in the original PDF figure, not the text we have. What we know:

- It has **9 secret quantities** total: parameters `a, b, c, d, e, f` and initial state `x₀, y₀, z₀`.
- The paper uses fixed values: `(a, b, c, d, e, f) = (0.3, 0.94, 0.9, 1.6, -1.8, -1.8)` and `(x₀, y₀, z₀) = (0.1, 0.1, 0.1)`.
- Iterating produces three coupled sequences: `X = (x₀, x₁, x₂, ...)`, `Y = (y₀, y₁, y₂, ...)`, `Z = (z₀, z₁, z₂, ...)`.

For the talk you don't need to write the equation. Just say it's a 3D discrete chaotic map with 6 parameters and 3 initial values, total of 9 secret quantities.

---

## Why 3D instead of 1D?

A 1D map (like the logistic map) gives you one chaotic sequence. The paper needs three sequences (one for each cube coordinate `i, j, k`). Options:

| Option | Pros | Cons |
|---|---|---|
| Run 1D map three times with different seeds | Simple | Three independent sequences — no coupling, weaker security |
| Use a 3D map → get 3 coupled sequences at once | Coupled sequences are harder to predict; bigger key space | Slightly more complex |

The paper picks the 3D approach for the coupling benefit and the larger key space.

---

## From chaos to "pseudo-random number generator (PRNG)"

The chaotic map outputs are real numbers between 0 and 1 (approximately). To use them for encryption, you need:

1. **Integer values** in a specific range (e.g., 0-255 for pixel-level XOR; 0 to cube-dimension for position indices).
2. **Statistical randomness** (passes NIST tests).

The paper does two post-processing steps:

### Step 1: Burn-in (warm-up)

Iterate the map **1.25 × 10⁵ times** before using any values. This pushes the trajectory deep onto the chaotic attractor, away from any transient or biased initial behavior. The first ~1000 iterations of any chaotic map can have weak statistics; burning in fixes this.

### Step 2: Quantize

Take the real-valued output `xₙ` and convert to integer:

$$
\text{int\_value} = \text{floor}\!\left(|x_n - L| \cdot 10^k\right) \bmod M
$$

Where:
- `|·|` takes absolute value (ensures positive).
- `floor` rounds down.
- `· 10ᵏ` shifts decimals to the integer part (the paper picks `k` based on how much precision is needed).
- `mod M` keeps the integer in the range `[0, M-1]` (`M = 256` for pixel-level diffusion, `M = cube_dim` for position offsets).

This produces an integer sequence that **passes all 15 NIST randomness tests** (paper Table 1).

---

## The NIST randomness tests (Table 1 in paper)

NIST publishes a **statistical test suite** for randomness. It has 15 tests, each checking a different aspect of how random a sequence "looks":

| Test | What it checks |
|---|---|
| Frequency | Are 0s and 1s balanced? |
| Block Frequency | Within sub-blocks, are 0s and 1s balanced? |
| Cumulative Sums | Does the running sum stay near zero? |
| Runs | Are there too many or too few long runs of the same bit? |
| Longest Run | Length of the longest run of 1s |
| Rank | Linear algebra rank of matrices built from the sequence |
| FFT | Frequency analysis for hidden periodicities |
| Non-Overlapping Template | Do specific bit patterns appear at the expected frequency? |
| Overlapping Template | Same as above, allowing overlap |
| Universal | Compression-based test |
| Approximate Entropy | Entropy compared to random sequences |
| Random Excursions | Random walk properties |
| Random Excursions Variant | Detailed random walk analysis |
| Serial | Are all pairs/triples of bits equally likely? |
| Linear Complexity | How long is the shortest LFSR generating this sequence? |

**Pass criteria:** p-value ≥ 0.01 and pass rate > 96%.

**The paper's result: all 15 pass.** That's the proof the chaotic stream is statistically indistinguishable from true random data.

---

## Lyapunov exponent — the chaos detector

The paper mentions **Lyapunov exponents (LEs)** in Section 2.1.2. Here's what they are:

The Lyapunov exponent measures **how fast nearby trajectories diverge**. If `λ > 0`, two trajectories that start arbitrarily close to each other separate exponentially — that's the formal definition of chaos.

- **`λ > 0`** → chaotic
- **`λ = 0`** → periodic / stable
- **`λ < 0`** → trajectories converge (not chaotic)

The paper checks `λ` for their 3D map across parameter ranges and confirms `λ > 0` for the chosen settings. The **bifurcation diagram** in Fig. 2 visualizes this.

You don't need to compute Lyapunov exponents for the talk. Just be ready for: *"How do you know it's actually chaotic?"* → *"They computed the Lyapunov exponent and confirmed it's positive, which is the formal definition of chaotic behavior."*

---

## Why this beats a regular PRNG

You might ask: why not just use Python's `random.randint()` or AES-CTR as the key stream? Three reasons:

1. **Key sensitivity is finer-grained.** Chaos lets you have keys with precision 10⁻¹⁵, so the key space is enormous.
2. **No pre-computed tables.** AES needs S-boxes; chaos is just iterating a closed-form equation, which is easy to implement on small embedded devices.
3. **Research value.** This is what the paper studies. Chaos-based cryptography is a recognized academic field.

For production security AES-CTR is better in most ways. But chaos-based crypto is a valid research alternative that has its own niches (multi-image, compression-coupled, etc.).

---

## What to remember for the talk

1. A chaotic map = deterministic function that produces random-looking sequences when iterated.
2. The paper uses a **3D discrete chaotic map** with 9 secret quantities (6 params + 3 initial values).
3. **Burn-in phase:** iterate 1.25×10⁵ times before using values, to wash out initial transients.
4. **Quantization:** `floor(|xₙ - L| · 10ᵏ) mod M` turns real-valued chaos into integers.
5. The chaotic stream passes **all 15 NIST randomness tests**.
6. **Sensitivity to initial conditions** is what makes the starting state a usable encryption key — perturbation of 10⁻¹⁵ destroys decryption.

---

## If asked: "Show me the equation"

> *"The form of Equation 1 is in the paper's figure — it's a 3-variable discrete map with 6 parameters. The exact body isn't in the verbatim text we transcribed, but it's an iterated function from (x, y, z) to a new (x', y', z') with parameters a through f. The paper sets those to (0.3, 0.94, 0.9, 1.6, −1.8, −1.8) starting at (0.1, 0.1, 0.1), and the phase diagrams in Figure 1 confirm the trajectory is chaotic for those values."*

---
sticker: emoji//1f4d0
tags:
  - concept
  - notation
  - reference
---
# Concept 08 — Notation Cheat Sheet

> Every symbol that appears in the paper, what it means, and the kind of value it holds. Use this while reading the verbatim paper or any equation walkthrough.

---

## Image / cube dimensions

| Symbol | Meaning | Type |
|---|---|---|
| `N` | Number of input images | Integer (e.g., 12) |
| `n` | Image index (n = 1, 2, ..., N) | Integer |
| `h_n` | Height of image `n` (original) | Integer (e.g., 256 or 512) |
| `w_n` | Width of image `n` (original) | Integer |
| `h'_n, w'_n` | Height/width of image `n` after DWT compression (half of original) | Integer |
| `h_max, w_max` | Max height and width across all input images | Integer |
| `M_h` | Cube height = `h_max / 2` | Integer |
| `M_w` | Cube width = `w_max / 2` | Integer |
| `z` | Cube depth = `ceil(P / (M_h · M_w))` | Integer |
| `P` | Total pixel count in cube | Integer |

---

## Channel and pixel indexing

| Symbol | Meaning | Type |
|---|---|---|
| `R, G, B` | Red, Green, Blue color channels | Sub-images |
| `(i, j, k)` | Pixel position in the cube: row, column, depth | Tuple of integers |
| `i` | Row index, `0 ≤ i < M_h` | Integer |
| `j` | Column index, `0 ≤ j < M_w` | Integer |
| `k` | Depth index, `0 ≤ k < z` | Integer |

---

## DWT sub-bands

| Symbol | Meaning | Size |
|---|---|---|
| `LL` | Low-Low approximation (kept) | Half height × half width |
| `LH` | Low-High (horizontal detail, discarded) | Half × half |
| `HL` | High-Low (vertical detail, discarded) | Half × half |
| `HH` | High-High (diagonal detail, discarded) | Half × half |

---

## Cubes (3D arrays)

| Symbol | Meaning |
|---|---|
| `C` | Plaintext cube (stacked LL sub-bands) |
| `C'` | Confusion cube (positions scrambled) |
| `V` | 1D vector flattened from `C'` |
| `V'` | 1D vector after diffusion |
| `D` | Cipher cube (final encrypted output) |
| `F` | Decrypted cube (after inverse diffusion + inverse confusion) |

---

## Chaotic map parameters

| Symbol | Meaning | Paper's value |
|---|---|---|
| `a` | Chaotic map parameter | `0.3` |
| `b` | Chaotic map parameter | `0.94` |
| `c` | Chaotic map parameter | `0.9` |
| `d` | Chaotic map parameter | `1.6` |
| `e` | Chaotic map parameter | `−1.8` |
| `f` | Chaotic map parameter | `−1.8` |
| `x₀` | Initial state x | `0.1` |
| `y₀` | Initial state y | `0.1` |
| `z₀` | Initial state z | `0.1` |

These 9 quantities together form the **secret key** (along with plaintext-derived parameters).

---

## Chaotic sequences

| Symbol | Meaning | Used in |
|---|---|---|
| `X, Y, Z` | First set of chaotic sequences (from one map iteration) | Confusion step (positions) |
| `X2, Y2, Z2` | Second set of chaotic sequences (from another iteration) | Diffusion step (values) |
| `S1, T1, U1` | Integer offset sequences derived from `X, Y, Z` | Confusion swap targets |

Length of each sequence: `M_h × M_w × z` (one value per cube pixel).

---

## Quantization operations

| Symbol | Meaning |
|---|---|
| `abs(x)` | Absolute value of `x` |
| `floor(x)` | Round `x` down to nearest integer |
| `mod` | Remainder after division (e.g., `7 mod 3 = 1`) |
| `ceil(x)` | Round `x` up to nearest integer |
| `sum` | Sum of pixel values |
| `bitxor` or `XOR` or `⊕` | Bitwise exclusive OR |

---

## Plaintext-derived key components

| Symbol | Meaning |
|---|---|
| `L` | A constant used in quantization (paper sets `L = 0`) |
| `sum(C)` | Sum of all pixel values in plaintext cube `C` |
| Other Eq. (7) parameters | Six values computed from the cube to make the key plaintext-aware |

These are mixed into the chaotic map's state so that two different plaintexts produce two different key streams — even with the same chaotic parameters. This blocks chosen-plaintext attacks.

---

## Security metrics

| Symbol | Meaning | Ideal value |
|---|---|---|
| `PSNR` | Peak Signal-to-Noise Ratio (dB) | > 30 (Paper: 32.06) |
| `NPCR` | Number of Pixel Change Rate (%) | 99.6094 (Paper: 99.6533) |
| `UACI` | Unified Average Changing Intensity (%) | 33.4635 (Paper: 33.4887) |
| `IE` or `H(X)` | Information entropy (bits) | 8 (Paper: 7.9994) |
| `SE` | Spectral entropy (chaos complexity measure) | Close to 1 |
| `LE` or `λ` | Lyapunov exponent | > 0 (chaotic) |

---

## Equations referenced in the paper

| Eq. | What it defines | Section |
|---|---|---|
| (1) | 3D discrete chaotic map (form in figure) | 2.1 |
| (2) | Burn-in / fractional-part preprocessing | 3.1 |
| (3) | Quantization to integer sequence | 3.1 |
| (4) | DWT decomposition into LL, LH, HL, HH | 4.1.1 |
| (5) | Cube formation by stacking LL sub-bands | 4.1.1 |
| (6) | Cube depth computation (`z`) | 4.1.1 |
| (7) | Six plaintext-derived key parameters | 4.1.2 |
| (8) | Chaotic sequences X, Y, Z for confusion | 4.1.2 |
| (9) | Quantization of X, Y, Z → S1, T1, U1 | 4.1.2 |
| (10) | Nine confusion swap cases | 4.1.2 |
| (11) | Chaotic sequences X2, Y2, Z2 for diffusion | 4.1.3 |
| (12) | First-pixel diffusion (with seed) | 4.1.3 |
| (13) | General diffusion (with chaining) | 4.1.3 |
| (14) | First-pixel inverse diffusion | 4.2 |
| (15) | General inverse diffusion | 4.2 |
| (16) | PSNR formula | 5 |
| (17) | NPCR formula | 6.1.2 / 6.2.1 |
| (18) | UACI formula | 6.2.1 |

The equation **bodies** are mostly inside figures in the original PDF, so the verbatim text we have lists them as references. For the talk you don't need the bodies — just be able to describe what each equation does.

---

## Figures referenced in the paper

| Fig. | What it shows | Section |
|---|---|---|
| 1 | Phase diagram of the 3D chaotic map for 3 values of f | 2.1.1 |
| 2 | Bifurcation diagrams + Lyapunov exponents | 2.1.2 |
| 3 | Spectral entropy across parameter space | 2.1.3 |
| 4 | **Encryption pipeline flow chart** (the main one) | 4.1 |
| 5 | DWT compression and recovery process | 4.1.1 |
| 6 | Decryption pipeline flow chart | 4.2 |
| 7 | **Before / cipher / decrypted images** (great for slides) | 5 |
| 8 | PSNR values per channel per image (bar chart) | 5 |
| 9 | Failed decryption with x₀ perturbation 10⁻¹⁵ | 6.1.2 |
| 10 | NPCR test results | 6.1.2 |
| 11 | All-black and all-white test results | 6.2.2 |
| 12-13 | Plaintext vs cipher histograms (R, G, B) | 6.3.1 |
| 14 | Correlation in H, V, D directions | 6.3.2 |
| 15 | Sheared cube reconstruction | 6.4 |
| 16 | Noise attack reconstruction | 6.5 |

If you want to show a figure on a slide, the strongest visual choices are **Figure 4** (the encryption flow chart) and **Figure 7** (the before/cipher/decrypted images side by side).

---

## Test images used

The paper uses the **USC-SIPI image database** (a standard research benchmark). File names like `4.1.01.tiff` come from this database:

- `4.1.0X.tiff` images are 256 × 256 (small)
- `4.2.0X.tiff` images are 512 × 512 (medium)

Common pictures in this set: lena, mandrill, peppers, sailboat. The paper tests on 12 of them across both sizes.

---

## Units

| Unit | What it measures |
|---|---|
| **dB (decibels)** | PSNR (reconstruction quality). Logarithmic. |
| **%** | NPCR, UACI, pass rates |
| **bits** | Information entropy |
| **MB/s** | Encryption / decryption throughput |
| **s (seconds)** | Time cost |

---

## Quick conversion: bit-level vs byte-level

A pixel value of 180 in decimal is:
- Binary: `10110100`
- Hex: `0xB4`

When the paper says "XOR pixel with keystream value," both sides are 8-bit values. XOR is done bit-by-bit.

---

## TL;DR — the most-used symbols

If you remember only these, you can follow most of the paper:

- `C` = plaintext cube
- `C'` = after confusion
- `D` = after diffusion (final cipher)
- `(x₀, y₀, z₀)` = chaotic map starting state (key)
- `(a, b, c, d, e, f)` = chaotic map parameters (key)
- `X, Y, Z` = chaotic sequences for confusion
- `S1, T1, U1` = position offsets (derived from X, Y, Z)
- `X2, Y2, Z2` = chaotic sequences for diffusion XOR
- `LL` = the DWT sub-band the paper keeps

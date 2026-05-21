---
sticker: emoji//1f522
tags:
  - paper
  - equations
  - walkthrough
---
# Equations Walkthrough — Plain English

> Every numbered equation in the paper, what it does, and how to talk about it. The actual equation bodies (the math symbols) live inside figures in the original PDF — the verbatim text we have just lists them by number. This file translates each into plain English so you can defend any equation question.

---

## Equation (1) — The 3D chaotic map

**Section 2.1, defines:** The chaotic map's iteration rule.

**What it does:** Takes a current state `(x, y, z)` and 6 parameters `(a, b, c, d, e, f)`, produces a new state `(x', y', z')`. The exact algebraic form is in Figure 1, not the text.

**Why it exists:** This is the *engine* that produces all the pseudo-random sequences used for encryption. Iterating it forever produces an infinite, deterministic, random-looking trajectory.

**How to talk about it:** *"Equation 1 is the chaotic map — a 3-variable iterated function with six tunable parameters. Plug in (x, y, z), you get a new (x, y, z). The paper sets the parameters to (0.3, 0.94, 0.9, 1.6, −1.8, −1.8) starting at (0.1, 0.1, 0.1) — those values are chosen because phase diagrams and Lyapunov exponents confirm the resulting trajectory is chaotic."*

**If asked for the body:** Admit you don't have it. *"The exact form is in Figure 1 of the paper. We know it's a 3-variable map with 6 parameters, but the symbolic body lives in the figure rather than the prose."*

---

## Equation (2) — Burn-in preprocessing

**Section 3.1 Step 2, defines:** How to take the fractional part of the iterated chaotic values.

**What it does:** After iterating the map 1.25×10⁵ times, take each output `xₙ` and compute `|xₙ - L|`, where `L = 0`. This strips off any integer part, leaving a value in `[0, 1)`.

**Why it exists:** The chaotic map's raw output may have small biases or transient behavior. Taking absolute values and fractional parts normalizes the output to a clean `[0, 1)` range that's easier to quantize.

**How to talk about it:** *"Equation 2 is just preprocessing — take the absolute value of the chaotic output and use the fractional part. It's a normalization step to land in [0, 1)."*

---

## Equation (3) — Quantize to integers

**Section 3.1 Step 3, defines:** Conversion from real-valued chaos to integer key stream.

**What it does:** Multiplies the fractional value by a power of 10 (to shift decimals into the integer part), then takes mod 256 (to land in the byte range 0-255). Outputs an integer sequence ready for XOR with pixels.

**Why it exists:** Pixel values are integers 0-255. The XOR needs both sides to be integers. This is the bridge.

**How to talk about it:** *"Equation 3 quantizes the real-valued chaotic output into integers — floor of absolute value times ten-to-the-k, modulo a target size. That gives integer sequences that can XOR directly with 8-bit pixel values."*

---

## Equation (4) — DWT decomposition

**Section 4.1.1 Step 2, defines:** How each color channel splits into LL, LH, HL, HH.

**What it does:** Standard wavelet decomposition: low-pass filter rows then columns to get LL; combine low and high filters in the other 3 ways for LH, HL, HH. Each output is half the size in both dimensions.

**Why it exists:** This is *the* compression step. The paper keeps only LL, throws away LH, HL, HH → 1/4 the size.

**How to talk about it:** *"Equation 4 is the wavelet decomposition. Each channel — R, G, or B — gets split into four sub-bands. LL is the smoothed half-size approximation; the other three hold horizontal, vertical, and diagonal edges. The paper keeps only LL."*

---

## Equation (5) — Stack cube

**Section 4.1.1 Step 3, defines:** Merging all LL sub-bands into one 3D cube.

**What it does:** Concatenates all the per-channel LL sub-bands along the depth axis. Result: a 3D cube of dimensions `M_h × M_w × N` (where `N` is the total layer count).

**Why it exists:** Lets the encryption treat *all images simultaneously* as one object instead of processing per image.

**How to talk about it:** *"Equation 5 stacks the LL sub-bands into a 3D cube. Cube width is half the widest input's width; cube height is half the tallest input's height; cube depth fits the total layer count. That cube is what gets encrypted."*

---

## Equation (6) — Compute cube depth `z`

**Section 4.1.1 Step 4, defines:** How tall the cube needs to be.

**What it does:** Computes `z = ceil(P / (M_h × M_w))`. In words: take the total pixel count `P`, divide by the cube cross-section, round up to get the depth.

**Why it exists:** Ensures the cube is exactly big enough to hold all pixels. Any leftover space gets zero-padded.

**How to talk about it:** *"Equation 6 computes the cube's depth — it's the ceiling of total pixel count divided by the cube cross-section. Zero padding fills any leftover space."*

---

## Equation (7) — Six plaintext-derived parameters

**Section 4.1.2 Step 2, defines:** How to compute extra key components from the plaintext itself.

**What it does:** Computes six values from the cube `C`. The most important is `sum(C)` (the sum of all pixel values), plus five others derived from cube dimensions and content.

**Why it exists:** Making the key depend on the plaintext means *two different plaintexts produce two different key streams*. This blocks **chosen-plaintext attacks**: an attacker can't precompute a useful key by analyzing the chaotic parameters alone — they'd need to also predict the plaintext sum.

**How to talk about it:** *"Equation 7 derives six extra key components from the plaintext itself — things like the cube's pixel sum. These get mixed into the chaotic map's state, so two different inputs produce two different key streams. That's what makes the scheme plaintext-aware."*

---

## Equation (8) — Confusion sequences X, Y, Z

**Section 4.1.2 Step 3, defines:** Generate the chaotic sequences for confusion.

**What it does:** Iterate the chaotic map (now seeded with both the original parameters AND the Equation-7 plaintext-derived values) `M_h × M_w × z` times. Collect the x, y, z outputs into three sequences `X`, `Y`, `Z`.

**Why it exists:** Need a unique random-looking offset for each pixel's swap target — one per cube pixel.

**How to talk about it:** *"Equation 8 generates three chaotic sequences X, Y, Z by iterating the map once per cube pixel. Each value will become a position offset for the confusion step."*

---

## Equation (9) — Quantize X, Y, Z → S1, T1, U1

**Section 4.1.2 Step 3, defines:** Convert the real-valued X, Y, Z to integer offsets.

**What it does:** For each `Xₙ` (similarly Y, Z), compute `floor(|Xₙ| · 10ᵏ) mod (cube dimension)`. Output: three integer sequences `S1`, `T1`, `U1`, each value in the valid coordinate range.

**Why it exists:** Pixel positions are integers. Need integer offsets to do swaps.

**How to talk about it:** *"Equation 9 quantizes X, Y, Z into integer offset sequences S1, T1, U1. Each value is a valid coordinate inside the cube. These are the actual swap targets."*

---

## Equation (10) — The 9 confusion swap cases

**Section 4.1.2 Step 4, defines:** For each pixel `(i, j, k)`, where does it move?

**What it does:** Compares `(i, j, k)` against `(S1(k), T1(k), U1(k))`. Each coordinate has 3 outcomes (>, <, =), giving 9 combinations. Each combination specifies the swap target:
- All three `>`: swap with `(i + S1(k), j + T1(k), k + U1(k))`.
- All three `<`: swap with `(|i - S1(k)|, |j - T1(k)|, |k - U1(k)|)`.
- All three `=`: stay in place.
- The other 6: mixtures (e.g., `i > S1`, `j < T1`, `k = U1` → swap each axis according to its own rule).

**Why it exists:** Without the 9-case structure, swap targets could land outside the cube. The 9 cases ensure every swap is well-defined.

**How to talk about it:** *"Equation 10 is the rule for moving pixels. For each pixel, compare its (i, j, k) coordinates to the chaotic offsets. Bigger → swap with i plus offset. Smaller → swap with absolute value of i minus offset. Equal → stay. Three coordinates times three outcomes per coordinate = 9 cases. You don't need to memorize all 9 — the principle is simple."*

---

## Equation (11) — Diffusion sequences X2, Y2, Z2

**Section 4.1.3 Step 1, defines:** Generate fresh chaotic sequences for diffusion.

**What it does:** Iterate the chaotic map again (different starting point — typically the state at the end of confusion) `M_h × M_w × z` times. Collect into `X2`, `Y2`, `Z2`. Quantize the same way as Equation 9, but to range 0-255 (byte values).

**Why it exists:** Need a separate keystream for diffusion. If confusion and diffusion used the same stream, attackers could exploit the redundancy.

**How to talk about it:** *"Equation 11 generates the diffusion keystream — three sequences X2, Y2, Z2, quantized to byte range. Separate from the confusion keystream so the two stages don't share randomness."*

---

## Equation (12) — First-pixel diffusion (with seed)

**Section 4.1.3 Step 2, defines:** How to encrypt the very first pixel.

**What it does:** `V'(0) = V(0) XOR seed`, where `seed` is a value derived from the chaotic sequence. This bootstraps the chain.

**Why it exists:** The general diffusion rule (Equation 13) uses the previous output `V'(n-1)`. For the first pixel there is no previous output, so a seed plays that role.

**How to talk about it:** *"Equation 12 handles the first pixel — XOR it with a seed from the chaotic sequence. This bootstraps the chaining that follows."*

---

## Equation (13) — General diffusion (with chaining)

**Section 4.1.3 Step 3, defines:** Encryption rule for all subsequent pixels.

**What it does:** For each pixel index `n > 0`:
- Compute `n mod 3`.
- If 0: `V'(n) = V(n) XOR X2(n) XOR V'(n-1)`.
- If 1: `V'(n) = V(n) XOR Y2(n) XOR V'(n-1)`.
- If 2: `V'(n) = V(n) XOR Z2(n) XOR V'(n-1)`.

The `XOR V'(n-1)` chains each output to the previous, producing the avalanche effect.

**Why it exists:** Pure XOR with a keystream is breakable if the keystream repeats. Cycling three streams + chaining makes attacks much harder.

**How to talk about it:** *"Equation 13 is the workhorse — XOR each plaintext pixel with one of three chaotic streams (cycled by index mod 3), AND XOR with the previous encrypted pixel. That chaining is what gives the avalanche effect — a one-bit change ripples through every subsequent pixel."*

---

## Equation (14) — First-pixel inverse diffusion

**Section 4.2 Step 1, defines:** Decryption of the very first pixel.

**What it does:** `V(0) = V'(0) XOR seed`. XOR is its own inverse, so applying the same XOR undoes it.

**Why it exists:** Symmetric to Equation 12.

**How to talk about it:** *"Equation 14 is the inverse of Equation 12 — just XOR with the same seed to recover the first plaintext pixel. XOR is self-inverse."*

---

## Equation (15) — General inverse diffusion

**Section 4.2 Step 2, defines:** Decryption rule for all subsequent pixels.

**What it does:** Walk from the last pixel backwards. For each `n`:
- `V(n) = V'(n) XOR keystream(n) XOR V'(n-1)`.

Same XORs as encryption — XOR being self-inverse means encryption and decryption use identical operations.

**Why it exists:** The receiver, knowing the key, can regenerate the same X2, Y2, Z2, V'(n-1), and recover the plaintext.

**How to talk about it:** *"Equation 15 reverses diffusion — XOR is symmetric, so encryption and decryption use the same operation. You walk through the cipher and apply the same XORs to recover plaintext."*

---

## Equation (16) — PSNR formula

**Section 5, defines:** Reconstruction quality metric.

**What it does:** `PSNR = 10 · log₁₀(MAX² / MSE)`, in dB. `MAX = 255` for 8-bit. `MSE` = mean squared error between original and reconstructed images.

**Why it exists:** Quantifies how close the reconstructed image is to the original. Higher = better.

**How to talk about it:** *"Equation 16 is the PSNR formula — peak signal-to-noise ratio. Higher means closer to original. Anything above 30 dB is visually clean. The paper hits 32.06 dB."*

---

## Equation (17) — NPCR formula

**Section 6.1.2 / 6.2.1, defines:** Differential attack metric.

**What it does:** Counts how many pixels differ between two cipher images after a 1-pixel plaintext change, divided by total pixel count, times 100%.

**Why it exists:** Measures the avalanche property. Should be near 99.6094% for a strong cipher.

**How to talk about it:** *"Equation 17 computes NPCR — number of pixel change rate. Encrypt twice — once original, once with one pixel flipped — and count what percentage of cipher pixels differ. Ideal is 99.6094%. Paper hits 99.65%."*

---

## Equation (18) — UACI formula

**Section 6.2.1, defines:** Differential attack intensity metric.

**What it does:** Average of `|C1(i,j) - C2(i,j)| / 255` across all pixel positions, times 100%.

**Why it exists:** Measures not just *how many* pixels change but *by how much*. Should be near 33.4635% for a strong cipher.

**How to talk about it:** *"Equation 18 is UACI — unified average changing intensity. Average intensity difference between two ciphers as a percentage. Ideal is 33.46%. Paper hits 33.49%."*

---

## Quick reference card (memorize this table)

| Equation # | One-line summary |
|---|---|
| 1 | The chaotic map (iteration rule) |
| 2 | Burn-in preprocessing (take fractional part) |
| 3 | Quantize chaos → integer keystream |
| 4 | DWT split image into LL, LH, HL, HH |
| 5 | Stack LL sub-bands into a 3D cube |
| 6 | Compute cube depth z |
| 7 | Six plaintext-derived key parameters |
| 8 | Chaotic sequences X, Y, Z (for confusion) |
| 9 | Quantize X, Y, Z → integer offsets S1, T1, U1 |
| 10 | 9 swap cases for confusion |
| 11 | Chaotic sequences X2, Y2, Z2 (for diffusion) |
| 12 | First-pixel diffusion (XOR with seed) |
| 13 | General diffusion (XOR with chaos + previous output) |
| 14 | First-pixel inverse diffusion |
| 15 | General inverse diffusion |
| 16 | PSNR formula |
| 17 | NPCR formula |
| 18 | UACI formula |

If you can describe each row's purpose in one sentence, you can answer any "what does equation X do?" question.

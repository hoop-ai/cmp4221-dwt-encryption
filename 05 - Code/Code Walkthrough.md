---
sticker: emoji//1f4d6
tags:
  - code
  - walkthrough
---
# Code Walkthrough

> Read this alongside the three Python files. Each section explains the corresponding code in plain English.

---

## File 1: `chaotic_map.py`

### What it does

This file is the **pseudo-random source** for the whole encryption. It implements:
1. The 3D chaotic map (one iteration step).
2. Iteration with burn-in (1.25×10⁵ throwaway iterations to warm up).
3. Quantization (convert real values to integers in a target range).

### Walkthrough

**`chaotic_step(x, y, z, p)`** — One iteration of the map. Given current state `(x, y, z)` and parameter dict `p`, returns the new `(x', y', z')`. The exact form is a Hénon-like 3-variable system, chosen as a plausible stand-in for the paper's Equation 1 (whose body lives in a figure we don't have).

**`iterate_map(n_samples, ...)`** — Calls `chaotic_step` repeatedly. First it runs 125,000 *throwaway* iterations (burn-in) to push the trajectory deep onto the chaotic attractor. Then it collects `n_samples` more iterations into three sequences `X`, `Y`, `Z`. **This is the core PRNG used everywhere else.**

**`quantize_to_range(seq, modulus, decimals)`** — Equation 3 of the paper. Converts real-valued chaotic outputs (which are between roughly −2 and 2) into integers in `[0, modulus-1]`. The recipe:
1. Take absolute value.
2. Multiply by `10^decimals` to shift the meaningful precision into the integer part.
3. `floor` to integer.
4. `mod modulus` to wrap into the target range.

**`make_keystream_byte(n_samples)`** — Convenience wrapper: generate `n_samples` bytes (0-255) for XOR diffusion.

**`make_offset_sequences(cube_h, cube_w, cube_d)`** — Generates three integer sequences (`S1`, `T1`, `U1`) where each value is a valid coordinate in the cube. Used by confusion.

### What to remember

- **Burn-in matters.** Without it, the first few values can have weak statistics and the whole encryption inherits the bias.
- **Quantization is what converts continuous chaos into discrete keystream values.**

---

## File 2: `dwt_compress.py`

### What it does

Implements:
1. DWT compression on a single channel (image → LL sub-band).
2. DWT decompression on a single channel (LL → recovered image, with zeros for LH/HL/HH).
3. Per-image RGB versions of the above (3 channels independent).
4. Stacking compressed images into the 3D plaintext cube.

### Walkthrough

**`dwt_compress_channel(channel)`** — Takes an H×W grayscale array. Calls `pywt.dwt2(channel, 'haar')` which returns `LL` and a tuple `(LH, HL, HH)`. **We discard LH, HL, HH and keep only LL.** That's the 1/4 compression — Equation 4 of the paper.

**`dwt_decompress_channel(LL)`** — The reverse. Creates zero arrays for the missing LH/HL/HH, calls `pywt.idwt2`, clips to [0, 255], returns uint8. Because LH/HL/HH are zeros (not the originals), this is lossy — the recovered channel is softer than the original.

**`dwt_compress_image(image_rgb)`** — Splits an RGB image into 3 channels, compresses each. Returns a (H/2)×(W/2)×3 array.

**`dwt_decompress_image(LL_rgb)`** — Reverses the previous. Returns an H×W×3 array.

**`stack_into_cube(compressed_images)`** — Takes a list of compressed images (possibly different sizes), finds the max H and W, pads smaller ones with zeros, and stacks every channel of every image as a separate cube layer. This is Equation 5 of the paper.

### What to remember

- **DWT keeps LL, throws LH/HL/HH.** That's the compression.
- **Zero-padding for different sizes is the paper's main limitation.** It wastes space.

---

## File 3: `encrypt_decrypt.py`

### What it does

Implements the full encryption + decryption pipeline using `chaotic_map.py` and `dwt_compress.py`.

### Walkthrough

#### Confusion (Section 4.1.2 of paper)

**`confusion_encrypt(cube, S1, T1, U1)`** — Scrambles pixel positions. For each pixel `(i, j, k)`:
1. Look up the offsets `(S1[k], T1[k], U1[k])` from the chaotic offset sequences.
2. Compute the swap target `(ni, nj, nk)` using the 9-case rule (Equation 10):
   - If `i > S1[k]`: `ni = (i + S1[k]) mod H` → "swap with i + offset" (mod for safety)
   - If `i < S1[k]`: `ni = |i - S1[k]|` → "swap with absolute difference"
   - If `i = S1[k]`: `ni = i` → "stay"
   - Same logic for `j` and `k`.
3. Swap the two pixels.

Pixel values are unchanged; only positions move.

**`confusion_decrypt(cube, S1, T1, U1)`** — Iterates the SAME swap procedure but in **reverse order** (last pixel first). Each swap is its own inverse, so running the loop backwards undoes the encryption confusion.

#### Diffusion (Section 4.1.3 of paper)

**`diffusion_encrypt(cube, keystream, seed)`** — Changes pixel values:
1. Flatten the cube to a 1D vector `V`.
2. First pixel: `V'(0) = V(0) XOR seed` (Equation 12).
3. Each subsequent pixel: `V'(n) = V(n) XOR keystream(n) XOR V'(n-1)` (Equation 13 simplified — we use one stream here for clarity; the paper uses three cycled by `n mod 3`).
4. Reshape back into a cube.

The crucial part is `XOR V'(n-1)` — chaining each output to the previous one. **That's the avalanche source.**

**`diffusion_decrypt(cube, keystream, seed)`** — Reverses diffusion using the SAME XORs (XOR is self-inverse). Walks from the LAST pixel backwards so `V'(n-1)` is the original cipher value, not a recovered one.

#### End-to-end

**`encrypt_pipeline(plaintext_images)`** — The full encryption:
1. DWT-compress each image.
2. Stack into a cube.
3. Confusion.
4. Diffusion.
5. Return the cipher cube + metadata.

**`decrypt_pipeline(cipher_cube, metadata)`** — The full decryption (reverse order):
1. Inverse diffusion.
2. Inverse confusion.
3. Unstack the cube into LL sub-bands.
4. Inverse DWT each one.
5. Return the recovered images.

### What to remember

- **Encryption order: DWT → stack → confusion → diffusion.**
- **Decryption order: inverse diffusion → inverse confusion → unstack → inverse DWT.**
- **Both XOR operations in diffusion use the same keystream — that's why decryption uses the same XORs.**

---

## How the three files connect

```
                ┌──────────────────────┐
                │  chaotic_map.py      │  ← Random source
                │  (iterate, quantize) │
                └──────────┬───────────┘
                           │ produces keystream + offset sequences
                           ▼
                ┌──────────────────────┐         ┌──────────────────────┐
                │  encrypt_decrypt.py  │ ◄────── │  dwt_compress.py     │
                │  (confusion +        │         │  (DWT, inverse DWT,  │
                │   diffusion +        │         │   stack cube)        │
                │   pipeline)          │         └──────────────────────┘
                └──────────────────────┘
```

`encrypt_decrypt.py` is the orchestrator. It imports from the other two and ties them together.

---

## Q&A using the code

**Q: "How is the cube formed if images have different sizes?"**
> *"In `dwt_compress.py`, look at `stack_into_cube`. It takes the max height and max width across all compressed images, and pads smaller ones with zeros to fit. That zero-padding is the paper's main limitation."*

**Q: "What exactly is the diffusion chaining?"**
> *"In `encrypt_decrypt.py`, look at `diffusion_encrypt`. The line `V_prime[n] = V[n] ^ keystream[n] ^ V_prime[n-1]` — that third XOR is the chaining. Each output depends on every previous output, so a single bit change at the start cascades through the rest. That's why NPCR hits 99.65%."*

**Q: "Why is decryption nearly the same code as encryption?"**
> *"XOR is its own inverse. Look at `diffusion_decrypt` — same XOR operation, just walked in reverse so we use the original cipher values, not the recovered ones."*

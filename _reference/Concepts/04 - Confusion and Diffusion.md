---
sticker: emoji//1f9ec
tags:
  - concept
  - confusion
  - diffusion
  - cryptography
---
# Concept 04 — Confusion and Diffusion

> The two principles every image cipher follows. Confusion moves things; diffusion changes them.

---

## Where these terms come from

In 1949, **Claude Shannon** (the father of information theory) wrote *Communication Theory of Secrecy Systems*. In it he defined two properties any strong cipher must have:

> **Confusion** — the relationship between the ciphertext and the secret key is so complex that an attacker can't deduce the key from the ciphertext.
>
> **Diffusion** — the statistical structure of the plaintext is spread out across the ciphertext, so that a change in one plaintext bit affects many ciphertext bits.

For image encryption, these translate cleanly to:

- **Confusion = rearrange pixel positions.**
- **Diffusion = change pixel values such that changes spread.**

---

## Confusion: scramble positions

Take a 4×4 mini-image:

```
A B C D
E F G H
I J K L
M N O P
```

Apply confusion (a permutation of pixel positions):

```
K I D B
N A F M
J O P L
G H C E
```

Same 16 letters, different arrangement. **Pixel values are unchanged. Only positions moved.**

### How the paper does confusion (Section 4.1.2)

Recall the chaotic map produces 3 sequences `X, Y, Z`. Post-process them into integer offset sequences `S1, T1, U1`. Then for each pixel position `(i, j, k)` in the cube:

1. Compare `i` to `S1(k)`, `j` to `T1(k)`, `k` to `U1(k)`.
2. Each comparison has 3 possible outcomes (>, <, =).
3. 3 coordinates × 3 outcomes = **9 swap cases** (Equation 10 in the paper).
4. Each case specifies a swap target. Example: if all three are >, swap `(i, j, k)` with `(i + S1(k), j + T1(k), k + U1(k))`.

After running for every pixel, the cube is the **confusion cube `C'`** — same data, scrambled positions.

### Why confusion alone isn't enough

Imagine confusion only. The attacker captures `C'`. They can:
- Compute the **histogram** (count how often each pixel value appears). Since values were not changed, the histogram is identical to the plaintext's histogram. That leaks information.
- Compute **correlation** between adjacent pixels. After confusion these are low, but if you can recover the original positions (e.g., by spotting structure), you get the image back.

So you need diffusion too.

---

## Diffusion: change values

Take the same 4×4 mini-image:

```
A B C D
E F G H
I J K L
M N O P
```

Apply diffusion (replace each value with `value XOR keystream_value`):

```
%j_d
m`#z
qY8x
*\&Q
```

Same positions. **Completely different values.**

### How the paper does diffusion (Section 4.1.3)

After confusion, take the cube `C'` and flatten it into a 1D vector `V`. Iterate the chaotic map again to get sequences `X2, Y2, Z2`. Then:

1. **For the first pixel `V(0)`:** XOR it with a seed derived from the chaotic sequence. Call the result `V'(0)`.
2. **For every subsequent pixel `V(n)`:**
   - Compute `n mod 3`.
   - If 0: `V'(n) = V(n) XOR X2(n) XOR V'(n−1)`.
   - If 1: `V'(n) = V(n) XOR Y2(n) XOR V'(n−1)`.
   - If 2: `V'(n) = V(n) XOR Z2(n) XOR V'(n−1)`.
3. Reshape `V'` back into a cube → **cipher cube `D`**.

The XOR with the previous output `V'(n−1)` is the **chaining trick**. It's what gives the scheme its avalanche property — a one-bit change at pixel 0 cascades to change every subsequent pixel.

### Why diffusion alone isn't enough

Diffusion only would mean: every pixel value changes, but positions stay the same. Imagine encrypting a checkerboard — every pixel value flips, but the checkerboard pattern is still there. The attacker can still see the spatial structure.

So you need confusion too.

---

## Why both together is strong

| Attack | Defeated by confusion | Defeated by diffusion |
|---|---|---|
| Histogram analysis | No (positions don't change values) | **Yes** |
| Spatial structure detection | **Yes** | No (positions still meaningful) |
| Correlation between adjacent pixels | Mostly | Mostly |
| Differential attack (1-pixel flip) | Partially | **Yes** (avalanche via chaining) |
| Brute force on key | Depends on key space, not on this distinction | Same |

Both together = strong cipher. One without the other = weak.

---

## The avalanche effect (why chaining matters)

The paper's diffusion is `V'(n) = V(n) XOR keystream(n) XOR V'(n−1)`. That third term is the chain.

**Without chaining** (`V'(n) = V(n) XOR keystream(n)`):
- Flip one bit of `V(0)`. Only `V'(0)` changes. The rest stays the same.
- NPCR would be tiny.

**With chaining** (paper's approach):
- Flip one bit of `V(0)`. `V'(0)` changes.
- Now `V'(1) = V(1) XOR keystream(1) XOR V'(0)` — and `V'(0)` changed, so `V'(1)` changes too.
- `V'(2)` depends on `V'(1)`, so it also changes.
- Cascade continues to the end.
- NPCR ≈ 99.6% (basically every output pixel different).

This avalanche is precisely what the **differential attack** test (NPCR/UACI) measures, and it's why the paper hits the ideal targets.

---

## The order matters: confusion first, then diffusion

The paper does **confusion → diffusion**. The reverse (diffusion → confusion) would also work but is generally considered slightly weaker because:

- After diffusion, every pixel value is already "scrambled."
- If you then confuse positions, the cipher is strong but the chaining effect (avalanche) hasn't been applied to the right pixels.

By doing **confusion first**, you guarantee:
1. The diffusion's chaining cascades through pixels in their *scrambled* order.
2. Any single plaintext change first hits a random-looking position, then cascades through diffusion. Two layers of unpredictability stacked.

---

## How decryption reverses both

The receiver has the same key, so they can regenerate `X, Y, Z, X2, Y2, Z2, S1, T1, U1` identically.

**Step 1: Inverse diffusion.** Start from the cipher cube `D`. Flatten to `V'`. For each pixel from `n = N-1` down to `n = 1`:
- Compute `V(n) = V'(n) XOR keystream(n) XOR V'(n−1)`.
- XOR is its own inverse, so this exactly undoes the encryption diffusion.

For `V(0)`, undo the seed XOR.

**Step 2: Inverse confusion.** Walk through the cube **in reverse order** (last pixel first). For each `(i, j, k)`, look up the same `(S1(k), T1(k), U1(k))` and reverse the swap.

After both steps, you have the plaintext cube `C`. Then inverse DWT each LL sub-band → recovered images.

---

## What to remember for the talk

1. **Confusion** = move pixel positions around. **Diffusion** = change pixel values.
2. Both are necessary; one without the other is weak.
3. The paper's confusion uses **chaotic sequences as position offsets** with 9 swap cases.
4. The paper's diffusion uses **XOR with chaotic sequences plus chaining** (each new pixel XORs with the previous encrypted pixel).
5. **Chaining is what gives avalanche** — a 1-bit input change ripples through the rest of the cipher, hitting NPCR ≈ 99.65%.
6. Decryption reverses both in opposite order (inverse diffusion first, then inverse confusion).

---

## If asked: "What are the 9 confusion cases?"

> *"For each pixel at position (i, j, k), the algorithm compares each coordinate to its chaotic offset. Each comparison has 3 outcomes — bigger, smaller, or equal. Three coordinates times three outcomes gives nine cases. Bigger means swap with i + offset; smaller means swap with abs(i − offset); equal means stay in place. The exact nine are listed in Equation 10 of the paper, but the takeaway is just: each pixel gets pushed to a chaos-determined new location."*

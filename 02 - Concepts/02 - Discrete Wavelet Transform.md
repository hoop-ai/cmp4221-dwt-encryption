---
sticker: emoji//1f30a
tags:
  - concept
  - dwt
  - compression
---
# Concept 02 — Discrete Wavelet Transform (DWT)

> What DWT does to an image, why it produces four sub-bands, and why keeping only LL gives you 1/4 compression with visually clean reconstruction.

---

## One-line definition

**DWT splits an image into four smaller sub-images, each capturing a different type of detail. Keeping only the "approximation" sub-image gives you a compressed version that's 1/4 the size but still visually recognizable.**

---

## Why DWT instead of DCT?

You already learned DCT in Week 6 for JPEG. DCT works in 8×8 blocks and transforms each block into a frequency representation. Why use DWT instead?

| Property | DCT | DWT |
|---|---|---|
| Domain | Frequency | **Time-frequency (localized)** |
| Block size | Fixed 8×8 (JPEG) | Variable / multi-resolution |
| Handles edges | Poorly (causes blockiness) | Well (preserves edges cleanly) |
| Suited to | Smooth regions | Mixed smooth + edges |
| Used in | JPEG | JPEG 2000, this paper |

**The key advantage of DWT:** it sees both *where* a feature is in the image AND *what frequency* it is. DCT only sees the frequency mix and loses location info. So DWT can preserve edges (a high-frequency local feature) better than DCT, which is exactly why this paper picks DWT.

**Concrete example:** in JPEG, you sometimes see "blockiness" at high compression (8×8 grid artifacts). JPEG 2000 (DWT-based) doesn't have this — it gets soft blur instead. That's the DWT difference.

---

## How DWT splits an image

Start with an `N × N` grayscale image. After one DWT pass, you get **four `N/2 × N/2` sub-bands**:

```
┌──────────────┬──────────────┐
│              │              │
│      LL      │      LH      │   ← top-left = LL = "approximation"
│  (low-low)   │  (low-high)  │   ← top-right = LH = horizontal detail
│              │              │
├──────────────┼──────────────┤
│              │              │
│      HL      │      HH      │   ← bottom-left = HL = vertical detail
│  (high-low)  │  (high-high) │   ← bottom-right = HH = diagonal detail
│              │              │
└──────────────┴──────────────┘
```

### What each sub-band actually contains

- **LL — Low-Low (approximation).** A blurred, half-sized version of the original. Where most of the perceptual content lives.
- **LH — Low-High (horizontal detail).** Captures horizontal edges (i.e., where pixels change in the vertical direction). Think: a horizon line.
- **HL — High-Low (vertical detail).** Captures vertical edges (where pixels change in the horizontal direction). Think: a tree trunk.
- **HH — High-High (diagonal detail).** Captures diagonal edges and noise. Think: a leaning roof.

**Naming convention:** the first letter is the filter applied along **rows**; the second letter is the filter applied along **columns**. L = low-pass (smoothing), H = high-pass (edge detection).

---

## How the split actually works (the procedure)

You don't need to memorize the math for the talk, but here's the procedure so you understand what's happening:

1. **Filter rows.** For each row of the image, apply a low-pass filter (smoothing) → get a smoothed row. Apply a high-pass filter (edge detection) → get an edges row.
2. **Downsample rows by 2.** Keep every other column. Now you have an image that's `N rows × N/2 columns` (smoothed half) and another `N rows × N/2 columns` (edges half).
3. **Filter columns.** Repeat for each column on both halves.
4. **Downsample columns by 2.** Keep every other row.
5. **Result:** four `N/2 × N/2` sub-bands.

The filters used are the **wavelet filter coefficients** (Haar, Daubechies, Symlets, etc.). The paper doesn't specify which one, but Haar (the simplest) is `[1/√2, 1/√2]` for low-pass and `[1/√2, -1/√2]` for high-pass.

---

## Why the paper keeps only LL

The paper does this:

1. Apply DWT → get LL, LH, HL, HH.
2. **Throw away LH, HL, HH.**
3. Keep LL. That's the "compressed" image.

This compresses to **1/4 the original size** because LL has half the height and half the width: `(N/2) × (N/2) = N²/4`.

### What you lose

The discarded sub-bands held the edge details. Without them:
- Sharp edges become slightly soft.
- Fine texture (high-frequency content) is lost.
- The image is **still recognizable** because LL preserves the overall structure.

This is **lossy compression**. The recovery PSNR is 32.06 dB in the paper — which means the recovered image is visually very close to the original but mathematically not identical.

### Why LL alone is enough

Human vision is much more sensitive to low frequencies (broad shapes) than high frequencies (fine detail). Throwing away the high-frequency details barely affects what your eye perceives, but it cuts the data by 75%.

This is the same insight JPEG exploits — it just uses DCT instead of DWT and throws away the high-frequency DCT coefficients via quantization.

---

## Visualizing it

Imagine you have a 256×256 photo of a face:

| Sub-band | What you'd see |
|---|---|
| LL (128×128) | A blurred, half-sized face — clearly recognizable as a face |
| LH (128×128) | A mostly black image with bright streaks along horizontal edges (eyebrows, mouth, hairline) |
| HL (128×128) | A mostly black image with bright streaks along vertical edges (nose, side of face) |
| HH (128×128) | A mostly black image with sparse bright spots on diagonal edges and noise |

The reason you can reconstruct the original from all four: LL + LH + HL + HH together contain *exactly* the same information as the original, just rearranged into frequency/location bins. Inverse DWT puts them back together perfectly.

But if you discard LH + HL + HH and reconstruct from just LL (with zeros for the others), you get a slightly soft version of the original. That's what the paper does.

---

## Reconstruction (inverse DWT)

To recover the image from a compressed LL:

1. Create empty (zero-filled) LH, HL, HH sub-bands at the same size as LL.
2. Apply the inverse DWT formula on the four sub-bands.
3. Get back an `N × N` image — softer than the original but recognizable.

In code (PyWavelets), this is:

```python
import pywt
# Encode: 256x256 image → 128x128 LL + 3 throwaways
LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')

# Send only LL across the wire (after encryption)

# Decode: 128x128 LL + zeros → 256x256 reconstructed image
import numpy as np
zeros = np.zeros_like(LL)
reconstructed = pywt.idwt2((LL, (zeros, zeros, zeros)), 'haar')
```

This is exactly what [`05 - Code/dwt_compress.py`](../05%20-%20Code/dwt_compress.py) implements.

---

## Multi-level DWT (NOT used in this paper, but you might get asked)

You can apply DWT to the LL sub-band **again** to get even more compression:

- Level 1: image → LL₁ (1/4 size)
- Level 2: LL₁ → LL₂ (1/16 size)
- Level 3: LL₂ → LL₃ (1/64 size)

JPEG 2000 uses multi-level DWT. **This paper uses only one level** — single DWT pass per channel, then keep LL. So compression is fixed at 1/4.

---

## What to remember for the talk

1. DWT splits an image into 4 sub-bands: **LL, LH, HL, HH**.
2. **LL is the approximation** (smoothed half-sized version).
3. LH, HL, HH are edges (horizontal, vertical, diagonal).
4. The paper **keeps only LL** → compresses to 1/4 size.
5. Reconstruction works by inverse DWT with zeros for LH/HL/HH.
6. This is **lossy**, but the loss is barely perceptible — PSNR 32 dB.
7. DWT > DCT for this paper because **DWT preserves edges better** thanks to time-frequency localization.

---

## If asked: "How does DWT compare to JPEG?"

> *"JPEG uses DCT in 8×8 blocks. DWT works on the whole image at once with multi-resolution wavelets. JPEG 2000 uses DWT and gets cleaner reconstruction at high compression — no block artifacts. This paper uses DWT for the same reason: when you compress and then encrypt and then decompress, you want a transform that preserves edges, and DWT does that better than DCT."*

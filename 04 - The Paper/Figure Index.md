---
sticker: emoji//1f5bc
tags:
  - paper
  - figures
  - reference
---
# Figure Index

> Every figure in the paper, what it shows, and whether it's worth putting on a slide.

---

## Quick reference

| Fig | Section | What it shows | Slide-worthy? |
|---|---|---|---|
| 1 | 2.1.1 | 3D chaotic map phase diagrams for 3 values of `f` | No (too abstract) |
| 2 | 2.1.2 | Bifurcation diagrams + Lyapunov exponents | No (technical chart) |
| 3 | 2.1.3 | Spectral entropy across parameter space | No |
| **4** | **4.1** | **Encryption pipeline flow chart** | **YES — best diagram in the paper** |
| 5 | 4.1.1 | DWT compression and recovery process | Maybe (good for slide 3) |
| 6 | 4.2 | Decryption pipeline flow chart | No (slide 5 covers this) |
| **7** | **5** | **Plaintext → cipher cube → cipher → decrypted images** | **YES — best visual proof** |
| 8 | 5 | PSNR values per channel per image (bar chart) | No (Table 2 is better) |
| 9 | 6.1.2 | Failed decryption with `x₀ + 10⁻¹⁵` perturbation | Maybe (dramatic for Q&A) |
| 10 | 6.1.2 | NPCR test results bar chart | No |
| 11 | 6.2.2 | All-black + all-white test results | No |
| 12 | 6.3.1 | Plaintext vs cipher histograms for `4.1.01.tiff` | Maybe (slide 9 backup) |
| 13 | 6.3.1 | Plaintext vs cipher histograms for `4.2.07.tiff` | No (12 is enough) |
| 14 | 6.3.2 | Adjacent-pixel correlation H, V, D | No |
| 15 | 6.4 | Sheared cube + reconstructed images | No (interesting but off-topic) |
| 16 | 6.5 | Noise attack reconstruction | No |

---

## Detailed descriptions

### Figure 1 — Phase diagrams of the 3D chaotic map

**Caption:** *Phase diagram (a) f = −1.8 (b) f = −1.1 (c) f = −0.2.*

**What it shows:** Three plots of the trajectory `(x, y, z)` as the chaotic map is iterated, for three values of parameter `f`. The trajectory makes complex looped shapes that don't repeat — that's the *attractor*.

**What it proves:** The map's behavior is genuinely chaotic (complex, aperiodic) for the chosen `f` values. Not periodic, not converging to a single point.

**Use it if asked:** *"How do you know the map is chaotic?"* → Reference this figure: *"The phase diagrams in Figure 1 show complex non-repeating trajectories — that's the visual signature of chaos."*

---

### Figure 2 — Bifurcation diagram + Lyapunov exponents

**Caption:** *Parameter f: (a) bifurcation diagram; (c) LEs. Parameter a: (b) bifurcation diagram; (d) LEs.*

**What it shows:** Four plots. (a) and (b) are bifurcation diagrams — they show how the system's behavior changes as `f` or `a` is varied. (c) and (d) plot Lyapunov exponents for the same parameter ranges. Wherever `LE > 0`, the system is chaotic.

**What it proves:** The Lyapunov exponent is positive across the parameter ranges the paper uses. That's the formal definition of chaos.

**Use it if asked:** *"Is the system really chaotic across all parameter choices?"* → *"Figure 2 shows Lyapunov exponents are positive throughout the parameter ranges they use. By definition, that means the system is chaotic."*

---

### Figure 3 — Spectral entropy

**Caption:** *Complexity for different values (a) (b, c, d, e) = (0.3, 0.94, 0.89, −1.8); (b) (a, b, d, e); (c) (a, b, c, e).*

**What it shows:** Three plots of spectral entropy (SE) as the remaining parameter varies. SE near 1 = complex / chaotic. The plots show SE close to 1 across the tested parameter ranges.

**What it proves:** The chaotic sequences are statistically complex, which is what you want for a key stream.

---

### Figure 4 — Encryption flow chart ★

**Caption:** *Encryption flow chart.*

**What it shows:** A box-and-arrow diagram of the encryption pipeline: input images → DWT compression → cube formation → confusion → diffusion → cipher cube.

**Why it's great for slides:** This is the single most important diagram in the paper. It's the visual answer to "how does this scheme work?" Use it on Slide 5 (pipeline overview) if you have time to capture and add it.

---

### Figure 5 — DWT decomposition and recovery

**Caption:** *DWT compression and recovery process.*

**What it shows:** A diagram of: original image → DWT → 4 sub-bands (LL, LH, HL, HH) → take LL → inverse DWT → reconstructed image.

**Why it's good for slides:** Visual proof of how DWT works. Could be used on Slide 3 to show the 4-sub-band split. Alternative: a custom diagram (what's currently in the deck).

---

### Figure 6 — Decryption flow chart

**Caption:** *Decryption flow chart.*

**What it shows:** Reverse of Figure 4. Cipher cube → inverse diffusion → inverse confusion → inverse DWT → reconstructed images.

**Why we don't use it:** Slide 5 already covers the pipeline; showing both encryption and decryption diagrams doubles up.

---

### Figure 7 — Visual result ★

**Caption:** *(a) Plaintext images; (b) Compressed images; (c) Cipher cube; (d) Cipher images; (e) Decrypted images; (f) Decompressed images.*

**What it shows:** A 6-panel collage:
- (a) Original photos (lena, peppers, etc.)
- (b) Compressed (LL only) — visually similar to originals, just smaller
- (c) Cipher cube — looks like static noise
- (d) Cipher images per layer — noise
- (e) Decrypted cube — recovered LL sub-bands
- (f) Decompressed — final recovered photos, visually identical to (a)

**Why it's great for slides:** **This is the single best visual proof in the paper.** It shows the encrypt → noise → decrypt round trip working. If you want one figure on your slides, this is it.

---

### Figure 8 — PSNR per channel bar chart

**Caption:** *PSNR values for three channels of different images.*

**What it shows:** A grouped bar chart of PSNR values for R, G, B channels across the 12 test images.

**Why we use Table 2 instead:** A table is easier to read than a bar chart on a small slide. The headline number (32.06 dB average) is in Table 2.

---

### Figure 9 — Key sensitivity failure

**Caption:** *Decryption images x₀' = x₀ + 10⁻¹⁵.*

**What it shows:** Decryption attempted with a key perturbed by 10⁻¹⁵. The result is pure noise — nothing recognizable.

**Why it's a great backup slide:** If asked *"how sensitive is the key?"*, you can pull this up and say *"a perturbation in the 15th decimal of one parameter destroys the decryption completely — Figure 9."*

---

### Figure 10 — NPCR bar chart

**Caption:** *Test results of NPCR.*

**What it shows:** Bar chart of NPCR values per test image. All above 99%.

**Why we don't use it:** Table 5 numbers are more impactful — you can say the actual numbers out loud (99.6533%) rather than gesturing at a chart.

---

### Figure 11 — All-black + all-white test

**Caption:** *All-black and all-white test results.*

**What it shows:** All-black input → cipher (still looks like noise, no structure leaks). Same for all-white input.

**Why it matters:** Proves the cipher doesn't leak structure even on pathological inputs. Useful for Q&A about chosen-plaintext attacks.

---

### Figure 12 — Histograms for `4.1.01.tiff` (256×256)

**Caption:** *(a) Plaintext image of "4.1.01.tiff" with R, G, B; (b) Cipher image of "4.1.01.tiff" with R, G, B.*

**What it shows:** Six histograms total. The three plaintext channel histograms are spiky (showing natural color distribution). The three cipher histograms are FLAT (uniform distribution).

**Why it's useful:** Direct visual proof of the "flat cipher histogram" claim. Could replace Slide 9's text bullet about histograms.

---

### Figure 13 — Histograms for `4.2.07.tiff` (512×512)

**Caption:** *(a) Plaintext image of "4.2.07.tiff" with R, G, B; (b) Cipher image of "4.2.07.tiff" with R, G, B.*

**What it shows:** Same idea as Figure 12 but for a 512×512 image.

**Why we don't need both:** Either Figure 12 or 13 makes the point.

---

### Figure 14 — Correlation diagrams

**Caption:** *(a) Plaintext image of "4.1.01.tiff" with H, V, D; (b) Cipher image of "4.1.01.tiff" with H, V, D.*

**What it shows:** Scatter plots of pairs of adjacent pixels — horizontal, vertical, diagonal. Plaintext: pairs lie tightly along the diagonal (high correlation). Cipher: pairs scatter randomly (no correlation).

**Why we don't use it:** Too technical for the 10-min talk. The take-home is "correlation drops from ~1 to ~0," which we say verbally on Slide 9.

---

### Figure 15 — Shear attack

**Caption:** *(a) Cipher cube sheared by 15%; (b) Cutting and reconstructing images.*

**What it shows:** Cipher cube with 15% cut out, and the partial reconstructions.

**Why we don't use it:** Robustness is mentioned on Slide 10 as a one-liner; the full Figure 15 would derail the 10-min budget.

---

### Figure 16 — Noise attack

**Caption:** *Noise attack test results (a) SPN, 0.002; (b) GN, 10⁻⁶.*

**What it shows:** Reconstructed images after salt-pepper noise (0.002) and Gaussian noise (10⁻⁶) added to the cipher.

**Why we don't use it:** Same as Figure 15 — noise robustness is a one-liner in our talk.

---

## How to grab a figure for the slides

If you want to capture Figure 4 or Figure 7 from the paper PDF:

1. Open the paper PDF in your browser (https://doi.org/10.1145/3769123).
2. Use a screenshot tool (Windows: `Win+Shift+S`) to capture the figure.
3. Crop to just the figure area + the caption text.
4. Save as PNG.
5. Insert into the relevant slide (currently the deck uses custom diagrams; replacing them with paper figures is optional).
6. **Credit the source** in slide notes or in small text: *"Figure 4 from Xu et al., 2026."*

---

## Tables to remember (not figures, but slide-worthy)

| Table | What it shows | Memorize? |
|---|---|---|
| 1 | NIST test results (15 tests, all pass) | Mention pass-rate |
| **2** | **PSNR comparison vs prior work** | **Yes — 32.06 vs 26-27** |
| 3 | Key space composition | Mention "≥ 2¹⁰⁰" |
| 4 | Key space comparison | No |
| **5** | **NPCR + UACI per test image** | **Yes — 99.65% and 33.49% averages** |
| 6 | NPCR + UACI vs prior work | No |
| **7** | **Information entropy per test image** | **Yes — 7.9994 average** |
| 8 | Entropy vs prior work | No |
| 9 | PSNR after shear attack | No |
| 10 | Encryption time/speed | Mention 6.15 MB/s |
| 11 | Decryption time/speed | No |

Tables 2, 5, 7 are the headline numbers. Memorize their averages: **32.06 / 99.65 / 33.49 / 7.9994**.

---
sticker: emoji//1f4ca
tags:
  - concept
  - metrics
  - security
  - psnr
  - npcr
  - uaci
  - entropy
---
# Concept 06 — Security Metrics

> Every test the paper runs to prove the scheme is secure. What each metric measures, what the "good" value is, and what the paper's number means.

---

## The full scorecard at a glance

| Metric | What it tests | Ideal | Paper's result | Status |
|---|---|---|---|---|
| **PSNR** | Reconstruction quality | High (>30 dB) | **32.06 dB** | Good |
| **Key space** | Number of possible keys | ≥ 2¹⁰⁰ | Several hundred bits | Strong |
| **Key sensitivity** | Does 10⁻¹⁵ perturbation break decryption? | Yes (NPCR > 99%) | Yes | Pass |
| **NPCR** | Pixel change rate under 1-pixel perturbation | 99.6094% | **99.6533%** | On target |
| **UACI** | Average intensity change under perturbation | 33.4635% | **33.4887%** | On target |
| **Information entropy** | Cipher unpredictability | 8 bits | **7.9994 bits** | Basically max |
| **Histogram** | Cipher value distribution | Flat | Flat | Pass |
| **Correlation** | Adjacent cipher pixel correlation | ≈ 0 | ≈ 0 | Pass |
| **NIST randomness** | Chaotic sequence randomness | 15/15 tests pass | 15/15 | Pass |
| **Shear (cropping) resistance** | Decryption survives 15% cut | Recognizable | PSNR ~30 dB | Pass |
| **Noise resistance** | Decryption survives noise | Recognizable | Yes | Pass |

Below: deep dive on each.

---

## 1. PSNR — Peak Signal-to-Noise Ratio

**Measures:** how close the reconstructed image is to the original.

**Formula:**

$$
\text{PSNR} = 10 \cdot \log_{10}\!\left(\frac{\text{MAX}^2}{\text{MSE}}\right) \text{ dB}
$$

Where:
- `MAX` = the maximum possible pixel value (255 for 8-bit images).
- `MSE` = mean squared error between original and reconstructed images, computed pixel-by-pixel.

**Reference points:**
- ∞ dB → perfect reconstruction (MSE = 0)
- 50+ dB → indistinguishable
- 30–40 dB → visually very close, near-imperceptible differences
- 20–30 dB → noticeable artifacts but still recognizable
- < 20 dB → significant degradation

**Paper's result: 32.06 dB.** Compared to prior schemes at 26–27 dB.

**Why logarithmic?** Because perception of noise is roughly logarithmic. A 6 dB difference in PSNR is a 4× reduction in error — meaningful, not noise.

**Worth saying out loud during the talk:** *"32 dB is solidly in the 'visually very close' zone — the recovered image looks the same to a human observer."*

---

## 2. Key space

**Measures:** how many possible keys an attacker would have to try in a brute-force attack.

**Formula:** if there are `n` independent secret quantities, each with precision `p`:

$$
\text{Key space} \approx p^n
$$

**Paper's setup:** 9 chaotic parameters (`a, b, c, d, e, f, x₀, y₀, z₀`) plus plaintext-derived parameters. Each chaotic parameter has precision ~10⁻¹⁵ (15 decimal digits). So:

$$
\text{Key space} \approx 10^{15 \cdot 9} = 10^{135} \approx 2^{448}
$$

The paper conservatively quotes the theoretical lower bound as `2¹⁰⁰`, citing reference [39].

**Why 2¹⁰⁰ matters:** trying `2¹⁰⁰` keys at 1 trillion keys/second would take `~4 × 10¹³` years — the age of the universe is about `1.4 × 10¹⁰` years. So brute force is infeasible.

**Worth saying:** *"At least 2¹⁰⁰ — well beyond brute force."*

---

## 3. Key sensitivity

**Measures:** does a tiny key perturbation make decryption fail?

**Test:** encrypt with `x₀ = 0.1`. Try to decrypt with `x₀' = 0.1 + 10⁻¹⁵` (a perturbation in the 15th decimal place). Compare the failed-decryption output to the correctly-decrypted image.

**Ideal:** the failed decryption should look like noise, with NPCR > 99% (basically every pixel different).

**Paper's result:** failed decryption is noise; NPCR > 99% (Figure 10 of paper).

**Why this matters:** proves the only way to decrypt is with the exact key. An attacker who has a key off by 10⁻¹⁵ in any one of nine parameters gets nothing useful.

---

## 4. NPCR — Number of Pixel Change Rate

**Measures:** how many pixels of the cipher change when one pixel of the plaintext is flipped.

**Formula:** let `C₁` be the cipher of original plaintext, `C₂` be the cipher after flipping one plaintext pixel. Then:

$$
\text{NPCR} = \frac{\sum_{i,j} D(i,j)}{W \cdot H} \times 100\%
$$

Where:
- `D(i,j) = 1 if C₁(i,j) ≠ C₂(i,j), else 0`
- `W, H` = image dimensions

**Ideal:** 99.6094% for 8-bit images (this is the theoretical expected value for two truly random images of the same size — see [Why 99.6094%](#why-996094)).

**Paper's result:** 99.6533% average across 12 test images.

**What it tells you:** flipping one input bit should cascade to change essentially every output pixel — that's the **avalanche effect**. A weak cipher would have NPCR near zero (output barely changes).

---

## 5. UACI — Unified Average Changing Intensity

**Measures:** *by how much* do those changed pixels differ (not just whether they differ).

**Formula:**

$$
\text{UACI} = \frac{1}{W \cdot H} \sum_{i,j} \frac{|C_1(i,j) - C_2(i,j)|}{255} \times 100\%
$$

**Ideal:** 33.4635% for 8-bit images.

**Paper's result:** 33.4887% average.

**Why these specific ideals?** They come from the expected mean and intensity difference of two truly uniform random 8-bit images. If your cipher hits these targets, it's behaving like random data — the gold standard.

**NPCR vs UACI in one sentence:** NPCR is *how many* pixels differ; UACI is *how much* they differ on average.

---

### Why 99.6094% (the deep math, for hostile Q&A)

For two truly random 8-bit images, the probability of any pair of corresponding pixels being identical is `1 / 256`. So the probability of differing is `255 / 256 ≈ 99.6094%`. That's the theoretical expected NPCR.

For UACI: the expected absolute difference between two uniformly random 8-bit values is computed by integrating `|x - y| / 255` over all pairs, giving approximately `1/3 × 100% ≈ 33.4635%`.

---

## 6. Information Entropy (IE)

**Measures:** how unpredictable / how uniformly distributed the cipher pixel values are.

**Formula** (Shannon entropy):

$$
H(X) = -\sum_{i=0}^{255} p_i \log_2(p_i)
$$

Where `pᵢ` = probability of pixel value `i` appearing in the image.

**Range:**
- 0 → completely predictable (one pixel value everywhere)
- 8 → maximum entropy for 8-bit (every value equally likely)

**Ideal:** 8 (uniform distribution).

**Paper's result:** 7.9994 bits, averaged across cipher images.

**Why this matters:** if the cipher's pixel distribution were biased (some values much more common than others), an attacker could exploit that. Entropy 7.9994 means the distribution is essentially flat — no information leaks via histogram analysis.

**For the talk:** *"Entropy of 7.9994 — basically the maximum possible 8. The cipher is statistically indistinguishable from pure noise."*

---

## 7. Histogram Analysis

**Measures:** the distribution of pixel values in the image.

**Test:** plot a histogram of pixel values (0-255 on x-axis, count on y-axis). For:
- **Plaintext:** spiky — certain values much more common than others (e.g., a sky image has lots of blue, few reds).
- **Ciphertext:** should be **flat / uniform** — every value roughly equally likely.

**Paper's result:** flat histograms (Figures 12 and 13 of paper).

**Why this matters:** spiky histograms leak structural info about the original. Flat histograms reveal nothing.

---

## 8. Correlation Analysis

**Measures:** are adjacent pixels related?

**Test:** pick pairs of horizontally / vertically / diagonally adjacent pixels. Compute Pearson correlation coefficient.

**Ideal:**
- Plaintext correlation ≈ 1 (neighboring pixels are very similar — natural images are smooth)
- Cipher correlation ≈ 0 (neighboring cipher pixels should be unrelated)

**Paper's result:** plaintext ≈ 1, cipher ≈ 0 in all three directions (Figure 14).

**Why this matters:** if cipher correlation > 0, an attacker can guess values from neighbors. Cipher correlation ≈ 0 means each pixel is independent.

---

## 9. NIST Randomness Suite

**Measures:** is the chaotic stream statistically random?

**Test:** run the chaotic stream through 15 statistical tests, each checking a different aspect of randomness.

**Pass criteria:**
- p-value ≥ 0.01 for each test
- Pass rate > 96%

**Paper's result:** all 15 tests pass (Table 1).

See [`03 - Chaotic Maps.md`](03%20-%20Chaotic%20Maps.md#the-nist-randomness-tests-table-1-in-paper) for the test list.

---

## 10. Shear (Cropping) Resistance

**Measures:** does decryption survive if part of the cipher is lost in transmission?

**Test:** cut 15% out of the cipher cube. Attempt to decrypt the remainder. Measure reconstruction quality.

**Paper's result:** images still recognizable with PSNR around 28–34 dB (Table 9). Slight quality loss from the missing data, but the rest of the image is intact.

**Why this matters:** in real-world transmission, packets get dropped. A cipher where one missing byte ruins the whole decryption is fragile. This scheme is **fault-tolerant**.

---

## 11. Noise Resistance

**Measures:** does decryption survive added noise?

**Test:** add salt-pepper noise (intensity 0.002) or Gaussian noise (intensity 10⁻⁶) to the cipher. Decrypt.

**Paper's result:** images visually recognizable despite noise (Figure 16).

**Why this matters:** real channels introduce noise. A cipher that amplifies noise into total destruction is useless. This one degrades gracefully.

---

## Summary: how to talk about these in the Q&A

If anyone asks "how secure is the scheme?", the structured answer is:

> *"It passes every standard test. NIST randomness 15-for-15. NPCR and UACI right on the ideal targets. Entropy 7.9994 out of 8. Histogram is flat, correlation between adjacent cipher pixels is zero. Key sensitivity to 10⁻¹⁵. Survives shear attacks at 15% cut, and noise attacks at standard intensities. Brute force is blocked by a key space of at least 2¹⁰⁰. It's empirical not formal — no mathematical proof — but the empirical evidence covers every known attack class for image ciphers."*

That paragraph hits every metric and frames the empirical-vs-formal distinction cleanly.

---

## What to remember for the talk

1. **PSNR 32.06 dB** — recovered image is visually clean.
2. **NPCR 99.6533%, UACI 33.4887%** — avalanche right on the ideal targets.
3. **Entropy 7.9994** — basically max (8).
4. **NIST 15/15** — chaotic stream is statistically random.
5. **Key space ≥ 2¹⁰⁰** — brute force impossible.
6. **Survives shear 15% + noise** — robust to transmission errors.

If you remember those 6 numbers, you can defend any "how good is the security" question.

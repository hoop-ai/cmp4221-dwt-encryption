---
sticker: emoji//1f4d6
tags:
  - concept
  - glossary
  - reference
---
# Concept 07 — Glossary

> Every term used in this folder, defined in one place. If you see a word you don't recognize, look here first.

---

## A

**AES (Advanced Encryption Standard).** The most widely used symmetric encryption algorithm in production. Used in HTTPS, banking, file encryption. Standardized by NIST in 2001 (FIPS 197). The paper does NOT use AES; it uses chaos-based encryption as a research alternative.

**Aperiodic.** A sequence that never settles into a repeating cycle (or has a cycle so long it doesn't matter). One of the formal properties of chaos.

**Approximation (sub-band).** Another name for the LL sub-band — the smoothed, half-sized version of the image after DWT.

**Attractor.** In chaos theory, the set of states a chaotic trajectory tends toward. Burning in the chaotic map (iterating 1.25×10⁵ times) ensures the sequence is *on* the attractor before being used for encryption.

**Avalanche effect.** When a tiny input change (1 bit) cascades to change most output bits. The paper achieves this via XOR chaining in diffusion.

---

## B

**Bifurcation diagram.** A plot showing how a system's behavior changes as you vary one parameter. In Section 2.1.2, the paper uses bifurcation diagrams to confirm the 3D chaotic map is actually chaotic across the parameter ranges used.

**Bit.** A single 0 or 1. An 8-bit pixel has 256 possible values.

**Block cipher.** An encryption algorithm that operates on fixed-size blocks (e.g., AES operates on 128-bit blocks). The paper's scheme is closer to a stream cipher (operates pixel-by-pixel) than a block cipher.

**Brute force attack.** Trying every possible key until one decrypts correctly. The defense is a large key space.

**Burn-in.** Iterating a chaotic map many times before using its output, to push the trajectory onto the chaotic attractor. The paper burns in for 1.25×10⁵ iterations.

---

## C

**C (plaintext cube).** The 3D cube formed by stacking all DWT-compressed LL sub-bands from the input images.

**C' (confusion cube).** Plaintext cube after pixel positions have been scrambled.

**Cascade / chaining.** The diffusion technique where each output pixel XORs with the previous output pixel, making single-bit input changes ripple through the rest of the cipher.

**Chaos / chaotic map.** A deterministic function that, when iterated, produces a sequence that looks random but is reproducible given the starting state.

**Cipher / ciphertext.** The encrypted output that an attacker sees but can't read.

**Cipher cube (D).** The final encrypted output of the paper's scheme — the cube after both confusion and diffusion.

**Confusion.** Cryptographic principle of scrambling pixel positions (or equivalent operation) so the relationship between ciphertext and key is complex.

**Correlation.** Statistical measure of how related two values are. Plaintext images have correlation ≈ 1 between adjacent pixels (smooth). Ciphertext should have correlation ≈ 0 (independent).

**Crossref.** A metadata registry for academic publications. Used to verify a paper's publication date (e.g., DOI 10.1145/3769123).

**Cube.** The 3D array structure used by the paper to encrypt multiple images at once.

---

## D

**D (cipher cube).** Final cipher output after both confusion and diffusion.

**DCT (Discrete Cosine Transform).** Frequency-domain transform used in JPEG. Operates on 8×8 blocks. The paper's DWT is a better alternative because DWT is localized in both space and frequency.

**Decryption.** Inverse of encryption: cipher → plaintext, given the key.

**Determinism / deterministic.** No randomness in the process. Same inputs always produce same outputs.

**Differential attack.** An attack where the attacker flips one bit of the plaintext, re-encrypts, and compares the two ciphertexts. Measured by NPCR and UACI.

**Diffusion.** Cryptographic principle of changing pixel values so a small input change spreads across many output bits.

**DOI (Digital Object Identifier).** A persistent identifier for academic papers. Our paper's DOI: 10.1145/3769123.

**DWT (Discrete Wavelet Transform).** Image transform that splits an image into 4 sub-bands (LL, LH, HL, HH). The paper uses one-level DWT and keeps only LL for 1/4 compression.

---

## E

**Encryption.** Transforming plaintext into ciphertext so only key holders can read it.

**Entropy (information entropy).** Measure of unpredictability of a distribution. For 8-bit images, max is 8 (every value equally likely). Paper's cipher achieves 7.9994.

---

## F

**Floor.** Mathematical operation: round down to the nearest integer. `floor(3.7) = 3`. Used in the paper's quantization of chaotic values to integers.

---

## H

**Haar wavelet.** The simplest wavelet filter, used in DWT. Filter coefficients: `[1/√2, 1/√2]` for low-pass, `[1/√2, -1/√2]` for high-pass. Other wavelets (Daubechies, Symlets) exist; the paper doesn't specify which it uses.

**HH (High-High sub-band).** DWT sub-band capturing diagonal edges. Discarded by the paper.

**Histogram.** Plot of pixel value frequency. Plaintext histograms are spiky; cipher histograms should be flat (uniform).

**HL (High-Low sub-band).** DWT sub-band capturing vertical edges. Discarded by the paper.

**Hyperchaotic map.** A chaotic map with at least two positive Lyapunov exponents (extra unpredictability). Some prior schemes use these; the paper's 3D map provides similar properties.

---

## I

**IE (Information Entropy).** See **Entropy**.

**Initial conditions.** The starting state of the chaotic map: `(x₀, y₀, z₀)`. Combined with parameters, this forms the encryption key.

**Inverse DWT.** Reverses the DWT operation: given LL (plus optionally LH, HL, HH), reconstructs an image. The paper uses inverse DWT with zeros for the discarded sub-bands.

**Iteration.** Applying a function repeatedly. Each step uses the previous output as the new input. Chaotic maps are iterated.

---

## J

**JPEG.** Standard image compression format using DCT in 8×8 blocks.

**JPEG 2000.** Newer image compression standard using DWT. Cleaner artifacts than JPEG but less widely adopted.

---

## K

**Key.** The secret value an attacker doesn't know. In this paper: 9 chaotic parameters + plaintext-derived parameters.

**Key sensitivity.** Property where a tiny key change (e.g., 10⁻¹⁵ perturbation) makes decryption fail completely. A required property for strong ciphers.

**Key space.** Total number of possible keys. Defines brute force resistance. Paper claims ≥ 2¹⁰⁰.

**Key stream.** A long pseudo-random sequence generated from the key, used for XOR in stream ciphers.

---

## L

**LE (Lyapunov Exponent).** Number that measures how fast nearby trajectories of a dynamical system diverge. `λ > 0` means chaotic. Paper computes LEs to prove their map is chaotic.

**LH (Low-High sub-band).** DWT sub-band capturing horizontal edges. Discarded by the paper.

**LL (Low-Low sub-band).** DWT sub-band capturing the low-frequency approximation. Kept by the paper as the compressed image.

**Logistic map.** The simplest example of a chaotic map: `xₙ₊₁ = r·xₙ·(1−xₙ)`. Used in this glossary's explainer as the intuition vehicle; not the paper's map.

**Lossy compression.** Compression where some information is permanently lost. The paper's DWT-keep-LL is lossy because LH, HL, HH are discarded.

**Lossless compression.** Compression with no information loss. PNG is lossless; JPEG and our paper's DWT are not.

---

## M

**M_h, M_w.** Cube dimensions in the paper. `M_h = h_max / 2`, `M_w = w_max / 2`, where `h_max, w_max` are the largest input image's height and width.

**Map (mathematical).** A function from a state to a new state. A chaotic map is a specific kind.

**Mod (modulo).** Remainder after division. `7 mod 3 = 1`. Used in the paper to wrap chaotic values into specific ranges.

**MSE (Mean Squared Error).** Average of squared differences between original and reconstructed images. Used in PSNR computation.

**Multi-image encryption.** Encrypting multiple images at once. The paper's whole pitch.

---

## N

**N.** Number of input images in the paper's scheme.

**NIST (National Institute of Standards and Technology).** US standards body that publishes the AES standard (FIPS 197) and the Statistical Test Suite for randomness.

**NIST Test Suite.** 15 statistical tests for randomness. The paper passes all 15 for its chaotic sequence.

**Noise attack.** An attack where the attacker injects noise into the cipher to disrupt decryption. The paper survives this.

**NPCR (Number of Pixel Change Rate).** Fraction of cipher pixels that differ between two ciphers after a 1-pixel plaintext flip. Ideal: 99.6094%. Paper: 99.6533%.

---

## O

**One-time pad.** The only provably unbreakable cipher: XOR plaintext with a truly random key as long as the message, used only once. Impractical in real life because of key distribution.

---

## P

**P.** Total number of pixels in the cube. Used in computing cube depth `z`.

**Padding.** Adding fake values (usually zeros) to make data fit a required size. The paper pads smaller images with zeros to fit the cube.

**Phase diagram.** Plot of a dynamical system's trajectory in state space. The paper uses these in Section 2.1.1 to visualize the 3D chaotic map.

**Plaintext.** The original, unencrypted data.

**PSNR (Peak Signal-to-Noise Ratio).** Measure of reconstruction quality, in decibels. Higher = better. Paper: 32.06 dB.

**Pseudo-random.** Looks random, but actually deterministic given a seed. Chaotic maps generate pseudo-random sequences.

---

## Q

**Quantization.** Converting continuous (real) values to discrete (integer) values. The paper quantizes chaotic outputs into integers via `floor(|x| · 10ᵏ) mod M`.

---

## R

**R, G, B.** Red, Green, Blue color channels. The paper processes each channel independently.

**Robustness.** A cipher's ability to survive transmission errors (noise, cropping). The paper is robust to both.

---

## S

**S1, T1, U1.** Integer offset sequences for the confusion step, derived from the chaotic map's X, Y, Z outputs.

**Salt-pepper noise (SPN).** Noise that randomly sets pixels to either black (0) or white (255). The paper survives SPN intensity 0.002.

**Sensitivity to initial conditions.** Property of chaos where tiny changes in starting state lead to wildly different trajectories.

**SE (Spectral Entropy).** Complexity measure for chaotic sequences. The paper uses SE in Section 2.1.3 to confirm complexity is high.

**Seed.** A starting value for a pseudo-random generator. For chaos, the seed is the initial state `(x₀, y₀, z₀)`.

**Shear attack.** Cutting (cropping) part of the ciphertext to disrupt decryption. Paper survives 15% cut.

**Stream cipher.** A cipher that XORs plaintext with a long pseudo-random key stream. The paper's diffusion is a stream-cipher-style operation.

**Sub-band.** One of the four outputs of DWT (LL, LH, HL, HH).

---

## T

**TOMM (ACM Transactions on Multimedia Computing, Communications, and Applications).** The journal where our paper is published. One of the two allowed sources by the prof.

---

## U

**UACI (Unified Average Changing Intensity).** Average pixel intensity difference between two ciphers after a 1-pixel plaintext flip. Ideal: 33.4635%. Paper: 33.4887%.

**Uniform distribution.** Every value equally likely. The cipher's pixel distribution should be uniform.

---

## V

**V.** 1D vector flattened from the confusion cube C', used in the diffusion step.

**V'.** 1D vector after diffusion.

---

## W

**Wavelet.** A short oscillating waveform used in DWT. Different wavelets (Haar, Daubechies, etc.) give slightly different DWT results.

---

## X

**X, Y, Z.** Three sequences produced by iterating the 3D chaotic map. Used to build the confusion offsets S1, T1, U1.

**X2, Y2, Z2.** Second set of chaotic sequences, generated after the confusion step, used for diffusion XOR.

**XOR (exclusive OR).** Bitwise operation that returns 1 when input bits differ. Self-inverse: `A XOR B XOR B = A`. The fundamental building block of stream ciphers.

**x₀, y₀, z₀.** Initial values of the chaotic map. Part of the encryption key.

---

## Z

**z.** Depth of the cube C. Computed as `ceil(P / (M_h · M_w))`.

**Zero padding.** Filling unused cube positions with zero values to match required dimensions. Paper's main limitation (wastes space).

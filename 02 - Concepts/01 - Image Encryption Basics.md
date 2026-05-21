---
sticker: emoji//1f510
tags:
  - concept
  - encryption
  - image
---
# Concept 01 — Image Encryption Basics

> What is image encryption, why does it exist, and what makes it different from regular file encryption.

---

## What is image encryption?

**Image encryption** is the process of transforming a viewable image into a noise-looking output that nobody can interpret without a secret key. After encryption:

- An attacker sees random-looking pixels.
- Statistical analysis on the cipher image reveals nothing about the original.
- With the correct key, the original image can be perfectly (or near-perfectly) recovered.

Without encryption, intercepting an image is the same as seeing it. With encryption, intercepting an image gives you a meaningless block of noise.

---

## Why not just use AES on the image file?

You can. AES doesn't care whether the bytes are an image, a text file, or a movie. So a totally valid approach is:

1. Save the image as a `.png` file.
2. Encrypt the `.png` bytes with AES.
3. Send the encrypted file.

This works. But there are reasons image-specific encryption schemes exist:

| Reason | Explanation |
|---|---|
| **Image data has structure AES doesn't exploit** | Adjacent pixels are usually similar (a sky region is mostly the same blue). An image-specific scheme can be designed to break this correlation directly. |
| **AES doesn't compress** | You still pay full bandwidth. Image-specific schemes can combine encryption + compression in one step. |
| **AES doesn't handle multi-image batches naturally** | Encrypting 10 images means running AES 10 times. Image-specific schemes can encrypt a whole batch as one unit. |
| **Performance for huge images** | AES on a 4K image is slow because AES processes 128-bit blocks. Chaos-based schemes can run in parallel per pixel. |
| **Research / academic value** | Cryptography research wants alternative primitives in case AES is ever broken. Chaos and DNA-based encryption are studied for this reason. |

Bottom line: **AES is still better for general data protection**, but image-specific schemes have niches where they win, particularly when compression matters.

---

## The two pillars of any image cipher

Every image encryption scheme — including the one in our paper — does these two things:

### Pillar 1: Confusion (mess with positions)

**Confusion** scrambles where each pixel is. The pixel at row 100, column 50 moves to row 273, column 12. The values stay the same — only the locations change.

Why this matters: a recognizable image relies on pixels being in the right places. Scramble the positions and the image becomes a noise pattern, even though every pixel value is unchanged.

Think of it like cutting a printed photo into 1-pixel squares and shuffling them on a table.

### Pillar 2: Diffusion (mess with values)

**Diffusion** changes what each pixel's value is. Pixel at row 100, column 50 was `(0xA3, 0xFF, 0x12)` for R, G, B. After diffusion it's `(0x71, 0x4C, 0xD8)`.

Why this matters: if you only confuse positions, an attacker could in theory analyze the **histogram** (how often each color appears) and recover information. Diffusion replaces every pixel value with something derived from a chaotic stream, so the histogram becomes flat — no information leaks.

Diffusion in our paper is done via **XOR with a chaotic sequence** — see [`05 - XOR Cipher.md`](05%20-%20XOR%20Cipher.md).

### Always both, never one

A strong scheme always uses **both**. Confusion alone leaks histogram info. Diffusion alone leaves spatial structure. Together, they produce noise-like ciphertext.

See [`04 - Confusion and Diffusion.md`](04%20-%20Confusion%20and%20Diffusion.md) for the deep dive.

---

## The standard image encryption pipeline

Almost every image cipher in the literature follows this template:

```
Plaintext image
    │
    ▼
[Generate key stream from a chaotic system, given secret key]
    │
    ▼
[Confusion: scramble pixel positions using key stream]
    │
    ▼
[Diffusion: XOR pixel values with key stream]
    │
    ▼
Cipher image  →  transmit  →  Cipher image
                                  │
                                  ▼
                  [Regenerate same key stream from secret key]
                                  │
                                  ▼
                  [Inverse diffusion: XOR again (undoes XOR)]
                                  │
                                  ▼
                  [Inverse confusion: reverse swap order]
                                  │
                                  ▼
                              Plaintext image
```

The paper we're presenting follows exactly this template, with two twists:

1. **DWT compression added before encryption** — shrinks each image to 1/4 size first.
2. **The "image" is actually a 3D cube** containing multiple stacked images — encrypted as one unit.

---

## What makes an image cipher "good"?

There's a standard checklist that every paper has to pass to be publishable. Our paper passes all of them:

| Property | What you test | Standard |
|---|---|---|
| **Key space** | How many possible keys exist | ≥ 2¹⁰⁰ |
| **Key sensitivity** | Does a tiny key change ruin decryption? | Yes — perturbation of 10⁻¹⁵ should fail |
| **Histogram** | Is the cipher's pixel distribution flat? | Should be uniform |
| **Correlation** | Are adjacent cipher pixels correlated? | Should be ≈ 0 |
| **Information entropy** | Is the cipher unpredictable? | Should be ≈ 8 for 8-bit images |
| **NPCR** | Does a 1-pixel plaintext change avalanche? | Should be ≈ 99.61% |
| **UACI** | Average pixel intensity change after avalanche? | Should be ≈ 33.46% |
| **NIST randomness** | Is the chaotic stream statistically random? | 15/15 tests pass |
| **Robustness** | Does it survive cropping / noise? | Decrypted image should still be visible |

See [`06 - Security Metrics.md`](06%20-%20Security%20Metrics.md) for what each metric actually measures and why those exact numbers.

---

## Chaos-based encryption vs. AES — the honest comparison

| Property | AES | Chaos-based (this paper) |
|---|---|---|
| Mathematical security proof | Strong (decades of cryptanalysis) | Empirical only (statistical tests) |
| Speed | Hundreds of MB/s | 6 MB/s |
| Compression built in | No | Yes (via DWT) |
| Multi-image batch encryption | No (one image at a time) | Yes (the cube) |
| Handles different-size inputs naturally | No (requires padding logic) | Yes (cube absorbs size variation) |
| Standardized / production-ready | Yes (NIST FIPS 197) | No (research-grade) |
| Use case | Bank, OS, TLS | Research / niche multi-image transmission |

**For the talk:** if asked "why not AES?", the answer is:
> *"AES is more battle-tested and would be the right choice for general image encryption. This paper's pitch is integrated compression + encryption for multi-image batches, which AES alone doesn't give you. It's not 'better than AES,' it's 'AES + compression + multi-image in one pipeline.'"*

---

## Key terms used in this folder

- **Plaintext** — the original, viewable image. Latin for "plain text."
- **Ciphertext** — the encrypted, noise-looking output.
- **Key** — the secret value an attacker doesn't know. With the key, decryption is trivial; without it, infeasible.
- **Key stream** — the sequence of random-looking numbers generated from the key, used to confuse and diffuse the plaintext.
- **Avalanche effect** — when a tiny input change (1 bit) cascades to change most output bits. Strong ciphers have strong avalanche.

See [`07 - Glossary.md`](07%20-%20Glossary.md) for everything else.

---

## What to remember

1. Image encryption = transform image into noise that only the key holder can reverse.
2. Every scheme uses **confusion** (scramble positions) + **diffusion** (change values).
3. Quality is measured by: histogram flatness, low correlation, high entropy, NPCR/UACI on ideal targets, NIST randomness pass.
4. Chaos-based encryption is a research alternative to AES, with niche advantages (compression, multi-image, structure exploitation) and clear disadvantages (slower, no formal proof).

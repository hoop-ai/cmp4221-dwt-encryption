---
sticker: emoji//1f4ca
tags:
  - course
  - multimedia
  - project
  - slides
  - final
---
# Slide Deck Source — DWT Encryption

> Paper: Yidan Xu, Suo Gao, Yinghong Cao, Jun Mou. "Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression." *ACM Transactions on Multimedia Computing, Communications, and Applications*, Vol. 22, Issue 3, Article 82, pp. 1-20, March 2026. DOI: [10.1145/3769123](https://doi.org/10.1145/3769123).
> Crossref check: ACM TOMM Vol. 22 Issue 3; published online 2026-02-27; published print 2026-03-31.
> Word-for-word speaker scripts in [`03 - Speaker Scripts/`](03%20-%20Speaker%20Scripts/). Q&A prep in [`06 - Q&A and Rehearsal.md`](06%20-%20Q%26A%20and%20Rehearsal.md).

## Deliverables

| File | Purpose |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` / `.pdf` | Graded 10-slide, 10-minute presentation |
| `CMP4221 - DWT Encryption Study Deck.pptx` / `.pdf` | Full companion study deck with backup explanations and defense material |
| `_build/build_deck.py` | Single build command for both decks |

Run from this folder:

```powershell
python _build/build_deck.py
```

## Speaker Split

| Slides | Speaker | Role | Target |
|---|---|---|---|
| 1-5 | Abdul Rahman Malak (2285310) | title, problem, ingredients, novelty, pipeline | ~5 min |
| 6-10 | Maria Alftaih (2285921) | confusion, diffusion, findings, security, take-home | ~5 min |

---

## Main Deck — 10-Minute Version

### Slide 1 — Compression + encryption in one pipeline

**On screen**
- Multi-Image Encryption with DWT + Chaotic Map
- Xu, Gao, Cao, Mou — ACM TOMM Vol. 22 Issue 3, March 2026
- Thesis: compress multiple color images to 1/4 size, stack them, encrypt one cube

**Speaker script**
> Hi everyone, I'm Abdul, and this is Maria. For our final project we picked a 2026 paper from ACM Transactions on Multimedia, by Xu, Gao, Cao and Mou. The title is Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression. The idea is simple to state: take several color images, shrink them with the wavelet transform we saw in class, and then scramble them all at once using chaos. I'll do the first five slides, and Maria takes the rest.

### Slide 2 — Sending color images is slow AND unsafe

**On screen**
- Bandwidth: color images are 3 channels times millions of pixels
- Confidentiality: intercepted images must not be readable
- Scale: most schemes encrypt one image at a time
- Goal: compress and encrypt multiple images in one pass

**Speaker script**
> Think about what happens when you send a photo over the internet. A 512 by 512 color image already has about 786 thousand pixels across the R, G, and B channels. Multiply that by ten images, and you're moving a lot of data, and any of it can be intercepted. So the paper says there are really two problems happening at the same time: first, transmission is heavy, and second, transmission is unsafe. Most existing schemes handle one image at a time, which is fine for one selfie, but breaks down when you want to send a whole batch, like medical scans or surveillance frames. The authors point out that you need both compression and encryption working together, otherwise you're just bolting one on top of the other and paying the cost twice. Their goal is to do both in one shot, on multiple images, of different sizes.

### Slide 3 — Two ingredients: DWT and chaos

**On screen**
- DWT splits each channel into LL, LH, HL, HH
- Keep LL only: half width times half height = 1/4 size
- 3D chaotic map generates deterministic pseudo-random sequences
- Tiny key change creates a completely different sequence

**Speaker script**
> Okay so the first ingredient is the Discrete Wavelet Transform, the DWT. We saw this idea in lecture: instead of using sines and cosines like the Fourier transform, you use little localized waves called wavelets, and you split the image into four sub-bands. There's LL, which is the low-frequency approximation, basically a smaller blurry version of the image. Then there's LH, HL, and HH, which capture horizontal, vertical, and diagonal edges. The trick the paper uses is, they keep only the LL sub-band and throw the rest away. That immediately compresses the image to one quarter of its original size, because LL has half the height and half the width. Now the second ingredient is a three-dimensional discrete chaotic map. A chaotic map is just a function you iterate: you plug in x, y, z, you get new x, y, z, and you keep going. The output looks random, but it's fully deterministic if you know the starting values. Tiny change in those numbers, completely different sequence. That sensitivity is what makes it useful as a key.

### Slide 4 — Novelty: encrypt the cube, not the images

**On screen**
- DWT-compress every image
- Stack all LL sub-bands into one 3D cube
- Encrypt the cube once
- Handles different image sizes using zero-padding

**Speaker script**
> Here's the core trick. Instead of encrypting each image one by one, they DWT-compress every image down to its LL sub-band, and then they stack all those LL sub-bands on top of each other into a single three-dimensional cube. Then they encrypt the whole cube as one object. That's the novelty: one encryption pass, multiple images at once, even when those images have different sizes. They handle the size mismatch by padding with zeros.

### Slide 5 — Methodology: DWT → stack → confusion → diffusion

**On screen**
- Stage 1: DWT compression
- Stage 2: stack compressed images into cube C
- Stage 3: confusion swaps pixel positions
- Stage 4: diffusion changes pixel values with XOR

**Speaker script**
> Let me walk you through this end to end. Stage one, you take each color image, you split it into R, G, B channels, and you run the DWT on each channel. You keep only the LL sub-band; that's where the compression comes from, you're now at one quarter the size. Stage two, you take all those LL sub-bands from all your images, and you stack them into a single three-dimensional cube called C. The width and height come from the biggest image in the batch, and the depth comes from how many images you have. Stage three is what they call confusion. The chaotic map gets iterated to produce three sequences, S1, T1, U1, and these tell you how to swap pixel positions inside the cube. Stage four is diffusion. Here you don't just move pixels, you change their values, by XOR-ing each pixel with another chaotic sequence. After that, you have the cipher cube D, and that's what gets transmitted. Maria, over to you.

### Slide 6 — Confusion: scrambling pixel positions

**On screen**
- Iterate chaotic map once per cube pixel
- Generate coordinate offsets S1, T1, U1
- Nine swap cases depending on i, j, k versus offsets
- Pixel values unchanged; only positions move

**Speaker script**
> Thanks Abdul. So I'll start with confusion. Confusion in cryptography just means changing where things are, not what they are. The pixel values stay the same, only their positions move. The way they do it is, they iterate the chaotic map once for every pixel in the cube. From those iterations, they get three sequences, X, Y, Z, and they post-process them with mod and floor operations to land on integers in the right range. Those become S1, T1, U1, the three coordinate offsets. Then for every single pixel at position i, j, k, they compare each coordinate with its offset. There are nine possible swap cases. After running this for every pixel, you get the confusion cube C-prime. The nice thing is the offsets depend on the plaintext itself, which makes the scheme plaintext-aware. For the presentation, the clean definition is: confusion hides the location of information. The pixel values can be the same, but they no longer sit in meaningful image positions.

### Slide 7 — Diffusion: XOR with a chaotic stream

**On screen**
- Flatten C-prime into a 1D vector
- First pixel XORs with a seed
- Each next pixel uses one of three chaotic streams
- Previous encrypted pixel is reused, so one bit change cascades

**Speaker script**
> Diffusion changes the actual pixel values, not just their positions. The way they do it: first, they flatten the confusion cube into a one-dimensional vector V. Then they iterate the chaotic map again, this time getting sequences X2, Y2, Z2. For the very first pixel of V, they XOR it with a seed derived from the chaotic sequence. Then for every pixel after that, they take the index mod 3. Each result picks a different chaotic sequence to XOR with, so you're not just using one stream, you're cycling through three. And critically, the diffusion uses the previous pixel as part of the input. That means a single bit change at the start cascades through the rest of the encrypted data. After the loop, they reshape the vector back into the cipher cube D. This is stronger than a simple one-time XOR because the previous output links the whole vector together, so the effect spreads instead of staying local.

### Slide 8 — Findings: PSNR 32.06 dB beats prior work

**On screen**
- Reconstructed PSNR: 32.0601 dB
- Prior work range: 26.2896-27.6917 dB
- Compression ratio: 1/4 of original
- Encryption speed: 6.1529 MB/s

**Speaker script**
> Reconstruction quality is measured with PSNR, peak signal-to-noise ratio, in decibels. Anything around 30 dB is considered visually good. The paper reports 32.06 dB on average, and that's after lossy DWT compression and a full encrypt-decrypt round trip. Compare that to four prior schemes they benchmarked against: those land between 26.3 and 27.7 dB. So this paper's reconstruction is roughly 4 to 6 dB better, which on the PSNR scale is a meaningful jump because the scale is logarithmic. On the speed side, total encryption runs at about 6.15 megabytes per second on their setup. So the scheme is not just secure on paper; the recovered image is actually clean. That matters because quality is preserved, not merely decrypted.

### Slide 9 — Security: NIST, NPCR, UACI, IE all green

**On screen**
- NIST randomness: 15/15 tests passed
- NPCR mean: 99.6533%, target 99.6094%
- UACI mean: 33.4887%, target 33.4635%
- Information entropy: 7.9994 / 8

**Speaker script**
> Four security checks, all passed. First, the chaotic sequence itself goes through the NIST randomness suite: fifteen statistical tests, and every single one passes. Second, differential attack analysis. They flip one pixel of the input and re-encrypt, then measure NPCR and UACI. The standards are 99.6094 percent and 33.4635 percent. They hit 99.65 percent and 33.49 percent on average across twelve test images, so right on the ideal numbers. Third, information entropy of the cipher image is 7.9994, where the theoretical maximum is exactly 8. And fourth, the key space is way beyond brute force. So statistical attacks, differential attacks, and brute force are all blocked.

### Slide 10 — Limitation and take-home

**On screen**
- Limitation: zero-padding wastes space for mixed-size images
- Take-home: DWT + chaos combines compression and encryption in one pipeline
- Numbers to remember: PSNR 32 dB, IE 7.9994, NPCR 99.65%

**Speaker script**
> One honest limitation: when the images in the batch are different sizes, the cube has to be padded with zeros, which wastes space. The authors flag this as future work. The take-home is this: by combining DWT compression with a 3D chaotic map, you get encryption and compression in a single pass, with reconstruction quality of 32 dB and entropy basically equal to perfect noise. One pipeline, multiple images, strong security. Thanks for listening. We're happy to take questions.

---

## Companion Study Deck

The study deck is intentionally separate from the graded deck. It expands the same story into backup material:

1. Assignment requirement proof
2. Paper identity and DOI metadata
3. Problem framing
4. DWT formula and LL-only compression
5. Chaotic map/key parameters
6. Full pipeline
7. Cube sizing and zero-padding
8. Confusion algorithm
9. Diffusion algorithm
10. PSNR definition
11. PSNR comparison table/chart
12. NIST randomness table summary
13. Differential attack metrics: NPCR and UACI
14. Information entropy
15. Speed and efficiency
16. Limitations/future work
17. Likely Q&A
18. Rehearsal checklist

## Requirement Checklist

| Requirement | Status |
|---|---|
| Group of 2 | Abdul + Maria |
| 10-minute presentation | Main deck is 10 slides with timed speaker notes |
| Equal speaking | Slides 1-5 Abdul, 6-10 Maria |
| Journal paper | ACM TOMM |
| Published in 2026 | Crossref: online 2026-02-27, print 2026-03-31 |
| Novelty | Slide 4 |
| Methodology | Slides 5-7 |
| Findings | Slides 8-9 |

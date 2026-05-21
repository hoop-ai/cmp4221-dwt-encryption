---
sticker: emoji//1f4ca
tags:
  - course
  - multimedia
  - project
  - slides
  - final
---
# Slide deck source - DWT Encryption

Paper: Yidan Xu, Suo Gao, Yinghong Cao, Jun Mou. "Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression." ACM TOMM, Vol. 22, Issue 3, Article 82, March 2026. DOI: [10.1145/3769123](https://doi.org/10.1145/3769123).

Build command, from this folder:

```powershell
python _build/build_deck.py
```

## Deliverables

| File | Purpose |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` | Main 10-slide live deck |
| `CMP4221 - DWT Encryption Presentation.pdf` | PDF backup |
| `CMP4221 - DWT Encryption Study Deck.pptx` | Backup explanations for Q&A |
| `CMP4221 - DWT Encryption Study Deck.pdf` | PDF backup for study deck |
| `_build/build_deck.py` | Source builder for both decks |

## Speaker split

| Slides | Speaker | Role | Target |
|---|---|---|---|
| 1-5 | Abdul Rahman Malak | hook, problem, tools, novelty, pipeline | about 5 min |
| 6-10 | Maria Alftaih | confusion, diffusion, results, security, close | about 5 min |

## Visual system

Clean technical palette:

| Role | Color |
|---|---|
| Background | off-white `#F7FAFC` |
| Main text | deep navy `#102033` |
| Accent | teal `#0F766E` |
| Warning/limitation | amber `#D97706` |

No red accent. No fake Swiss letter-spacing. No decorative clutter. One idea per slide.

## Main deck - 10 slides

### Slide 1 - Encrypt a batch, not one image

**On screen**
- Encrypt a batch, not one image.
- DWT compresses images.
- Chaos encrypts the cube.
- 10-minute presentation.

**Speaker job**
Open with the thesis. Tell the audience the whole paper in plain English before naming every method.

### Slide 2 - Image batches are big and exposed

**On screen**
- Color images carry millions of values
- Batches multiply bandwidth cost
- Interception exposes raw pixels
- One-by-one encryption does not scale

**Speaker job**
Frame the two problems: size and privacy. Do not over-explain networking.

### Slide 3 - Two tools do the work

**On screen**

DWT:
- Splits channels into four bands
- LL keeps the visual base
- LL is one-quarter size

Chaos:
- Same key, same stream
- Tiny key change breaks it
- Stream drives pixel scrambling

**Speaker job**
Define DWT and chaos once, clearly. The audience only needs enough to follow the pipeline.

### Slide 4 - One cube. One encryption pass.

**On screen**

Old pattern:
- Compress image 1
- Encrypt image 1
- Repeat for every image

This paper:
- DWT-compress every image
- Stack LL bands into cube
- Encrypt the cube once
- Pad smaller images with zeros

**Speaker job**
Make the novelty impossible to miss: the cube is the contribution.

### Slide 5 - DWT, stack, confuse, diffuse

**On screen**
- DWT: keep LL bands
- Stack: build cube C
- Confuse: swap positions
- Diffuse: XOR values
- Output: cipher cube D

**Speaker job**
Walk the full pipeline, then hand off cleanly: "Maria, over to you."

### Slide 6 - Confusion moves positions

**On screen**
- Positions move
- Values stay unchanged
- Offsets come from chaos
- Nine cases choose swaps
- Same pixels. Different locations.

**Speaker job**
Define confusion as location hiding. Avoid drowning the audience in Equation 10.

### Slide 7 - Diffusion changes values

**On screen**
- Flatten cube to vector
- XOR with chaotic stream
- Reuse previous cipher pixel
- One bit change spreads forward
- Avalanche effect

**Speaker job**
Explain the chain. The previous output is what makes one small change spread.

### Slide 8 - Recovered images stay usable

**On screen**
- This paper: 32.06 dB
- Prior work: 26-27 dB
- Above 30 dB threshold
- Compression kept image quality

**Speaker job**
Say the number naturally: "thirty-two point oh-six." Do not read 32.0601 aloud.

### Slide 9 - The cipher behaves like noise

**On screen**
- NIST: 15/15 passed
- NPCR: 99.6533%
- UACI: 33.4887%
- Entropy: 7.9994/8
- Statistical, not formal proof

**Speaker job**
Be precise. These are empirical security checks, not a proof that the scheme beats AES.

### Slide 10 - Strong result, one real limitation

**On screen**
- 32 dB PSNR
- 7.9994 entropy
- 99.65% NPCR
- Zero-padding wastes cube space
- DWT handles size
- Chaos handles secrecy
- Cube handles batches

**Speaker job**
Close with the limitation first, then the take-home. End cleanly and invite questions.

## Companion study deck

The study deck is not for the live talk. It is backup material for rehearsal and Q&A:

1. Requirement check
2. Paper identity
3. DWT reminder
4. Chaos reminder
5. Cube construction
6. Confusion answer
7. Diffusion answer
8. PSNR answer
9. Security answer
10. Critique answer
11. Q&A anchors

## Requirement checklist

| Requirement | Status |
|---|---|
| Group of 2 | Abdul + Maria |
| 10-minute presentation | Main deck is 10 slides |
| Equal speaking | Abdul 1-5, Maria 6-10 |
| Journal paper | ACM TOMM |
| Published in 2026 | March 2026 issue |
| Novelty | Slide 4 |
| Methodology | Slides 5-7 |
| Findings | Slides 8-9 |

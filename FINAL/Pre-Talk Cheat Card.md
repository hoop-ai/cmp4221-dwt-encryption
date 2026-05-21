---
sticker: emoji//1f3ab
tags:
  - cheat-card
  - presentation
  - printable
---
# Pre-Talk Cheat Card

> **Print this. Fold it. Put it in your pocket.**
> Glance at it 5 minutes before walking up to present.
> Fits on one A4 page (Ctrl+P → Fit to page).
> Everything you need to land a clean 10 minutes.

---

## The 3-word summary

# SHRINK. STACK. SCRAMBLE.

The whole paper. Don't forget.

---

## The 6 numbers (memorize cold)

| Metric | Number | What it means |
|---|---|---|
| **PSNR** | **32.06 dB** | Recovered image quality (>30 = looks identical to original) |
| **NPCR** | **99.65 %** | 1-pixel input change avalanches the output (ideal 99.61) |
| **UACI** | **33.49 %** | Intensity of the avalanche (ideal 33.46) |
| **Entropy** | **7.9994** | Cipher is uniform noise (max 8 for 8-bit) |
| **NIST** | **15 / 15** | Chaotic stream passes all randomness tests |
| **Key space** | **≥ 2¹⁰⁰** | Brute force is infeasible |

---

## The novelty (slide 9 — the graded slide)

> "OLD WAY: encrypt one image at a time, repeat N times.
> NEW WAY: stack all N images into a 3D cube, encrypt the cube ONCE."

If you only deliver one slide cleanly, deliver this one.

---

## The 4-stage pipeline

1. **DWT compress** — each image → keep only LL → 1/4 size
2. **Stack into cube C** — all LL sub-bands stacked
3. **Confusion** — chaos scrambles positions
4. **Diffusion** — XOR with chaos + chain to previous output

Decryption = same 4 stages in reverse.

---

## Speaker split + handoff

| Slides | Speaker | Time |
|---|---|---|
| 1–8 | **Abdul** | ~5:00 |
| 9–16 | **Maria** | ~5:00 |

**Handoff line:** Abdul says *"Maria, take it from here"* at the end of slide 8. Maria responds *"Thanks Abdul"* and steps forward. **Practice this once before walking up.**

---

## If your brain blanks mid-talk

Say this slowly:

> *"This paper combines DWT compression with a 3D chaotic map to encrypt multiple color images in a single cube, reaching 32 dB PSNR and entropy 7.9994."*

That sentence buys you 8–10 seconds to recover.

---

## Q&A defense moves

| Question | Answer in one breath |
|---|---|
| *"Is this lossless?"* | "No — DWT keeps only LL. But PSNR is past 30 dB, so visually it looks identical." |
| *"Why not just use AES?"* | "AES doesn't compress and doesn't handle batches. This paper bakes both in." |
| *"What's the main limitation?"* | "Zero-padding wastes space when batch images have different sizes. The authors flag it as future work." |
| *"What's the strongest result?"* | "PSNR 32 dB AND entropy 7.9994 simultaneously — visually clean AND statistically random." |
| *"How does it compare to JPEG?"* | "More aggressive compression (1/4 vs JPEG's variable), no built-in encryption — this paper does both in one pipeline." |
| *"Could you scale to video?"* | "In principle yes — frames could stack into the cube. Paper doesn't address video, so it's an extension." |
| *"You don't know"* (any question) | "Good question. The paper doesn't address that directly, but my best guess is [reasonable guess]. [Partner], thoughts?" |

---

## Body language reminders

- Stand at slight angle to the screen, not back-to-audience
- Hands out of pockets — hold the clicker or rest at sides
- Feet planted — don't sway or pace during your script
- Find 3 friendly faces in audience (left, center, right) — rotate eye contact
- Move only at the handoff

---

## Timing rules

| Total time | What it signals |
|---|---|
| **> 10:00** | Cut off mid-sentence — bad |
| **9:30 – 10:00** | Ideal target |
| **8:00 – 9:30** | Fine, take questions earlier |
| **< 8:00** | Looks unprepared |

If you're 30 seconds over by slide 12, **cut a sentence per slide**, don't speed up. Speed reads as nervous.

If you're 30 seconds under by slide 12, **pause more between slides**, don't add content. Silence reads as confidence.

---

## Day-of checklist

- [ ] Both decks on USB stick + cloud backup (OneDrive / Drive link bookmarked)
- [ ] Water bottle within reach
- [ ] Phone on **silent** (not vibrate)
- [ ] Arrived 10 minutes early
- [ ] Tested the projector with your laptop
- [ ] One quick whispered run of the handoff line out loud
- [ ] This cheat card in pocket

---

## Last thought before you walk up

> Nobody in the room knows the paper better than you two right now. The prof picked these papers expecting you to teach the class. **You're the expert for the next 10 minutes.** Speak with that confidence.

---
sticker: emoji//1f6a6
tags:
  - course
  - multimedia
  - project
  - start
---
# START HERE — DWT Encryption Project

> Final paper: **Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression** (Xu, Gao, Cao, Mou. ACM TOMM Vol 22 Issue 3, March 2026. DOI [10.1145/3769123](https://doi.org/10.1145/3769123)).
> Group: **Abdul Rahman Malak (2285310) + Maria Alftaih (2285921)**.
> Talk: 10 minutes total, 5 min each, in Week 14 or 15.

---

## Read this folder in this order

You and your partner both go through these in the order shown. The numbering = the reading order.

| # | What | Why read it | Time |
|---|---|---|---|
| 0 | **[00 - START HERE](00%20-%20START%20HERE.md)** (this file) | Orientation. Know what each folder is for. | 5 min |
| 1 | **[01 - Project Report](01%20-%20Project%20Report.md)** | The master document. Everything else expands on this. Read top to bottom. | 45 min |
| 2 | **[02 - Concepts/](02%20-%20Concepts/)** | One file per concept. Start with `01 - Image Encryption Basics.md` and go in order. You'll understand every word of the paper after this. | 2-3 hours |
| 3 | **[03 - Speaker Scripts/](03%20-%20Speaker%20Scripts/)** | Your individual word-for-word script. Read your own one out loud, time it, internalize it. | 30 min × several passes |
| 4 | **[04 - The Paper/](04%20-%20The%20Paper/)** | Verbatim paper + equations explained in plain English + figure index. Reference only. | dip-in |
| 5 | **[05 - Code/](05%20-%20Code/)** | Python implementation of every algorithm. Read `Code Walkthrough.md` first. | 1 hour |
| 6 | **[06 - Q&A and Rehearsal](06%20-%20Q%26A%20and%20Rehearsal.md)** | 20 anticipated audience questions + rehearsal checklist + stage directions | 30 min |
| 7 | **[07 - Slide Deck Source](07%20-%20Slide%20Deck%20Source.md)** | Markdown source of the slides. Mirror of what's on screen. | reference |
| — | **[_meta/](_meta/)** | Prof brief, requirements breakdown, form schema. Admin only — read once, ignore after. | once |

---

## What's the project, in 60 seconds

The prof wants a 10-minute paired talk on a 2026 journal paper. We picked a paper about **encrypting images using two tools combined**:

1. **DWT (Discrete Wavelet Transform)** — a way to compress images by keeping only their low-frequency "approximation" sub-band. Same family as the DCT we learned in Week 6 for JPEG, but better at handling local edges. After DWT, an image is 1/4 of its original size.
2. **Chaotic map** — a math function that, when iterated, produces a sequence that *looks* random but is fully deterministic if you know the starting numbers. The starting numbers become the encryption key.

The novelty: instead of encrypting one image at a time, the paper takes multiple color images, DWT-compresses each one, stacks them all into a single 3D "cube," and encrypts that whole cube using the chaotic sequence. Result: **compression and encryption in one pass, on multiple images at once**.

If you only ever remember one sentence, remember **that one**.

---

## The speaker split

| Slide | Speaker | Content |
|---|---|---|
| 1 | Abdul | Title + paper intro |
| 2 | Abdul | Problem statement (transmission is slow + unsafe) |
| 3 | Abdul | Two ingredients (DWT + chaotic map) |
| 4 | Abdul | **Novelty** (encrypt the cube) |
| 5 | Abdul | Pipeline overview + **handoff to Maria** |
| — | — | — |
| 6 | Maria | Confusion step (scramble positions) |
| 7 | Maria | Diffusion step (XOR with chaos) |
| 8 | Maria | **Findings** (PSNR 32 dB beats prior work) |
| 9 | Maria | Security analysis (NIST, NPCR, UACI, IE) |
| 10 | Maria | Limitation + take-home |

The handoff line is "Maria, over to you." Maria physically steps forward. Practice this — it's the easiest part to fumble.

---

## Hard cap rules (from prof)

- ❌ **Over 10 minutes** → she cuts you off mid-sentence
- ❌ **Under 8 minutes** → looks unprepared
- ✅ **9:30–10:00** → ideal
- ❌ **One person dominating** → graded down ("equal length")
- ❌ **One person doing fluff while the other does math** → graded down ("both technical")
- ✅ Both speakers explain technical content

---

## If you're starting from zero (you said you don't know anything)

Read in this order over **3-4 study sessions**:

**Session 1** (~1.5 hours) — Get the big picture
1. [01 - Project Report](01%20-%20Project%20Report.md) cover to cover
2. [02 - Concepts/07 - Glossary.md](02%20-%20Concepts/07%20-%20Glossary.md) — skim so vocab feels familiar

**Session 2** (~2 hours) — Understand the building blocks
3. [02 - Concepts/01 - Image Encryption Basics.md](02%20-%20Concepts/01%20-%20Image%20Encryption%20Basics.md)
4. [02 - Concepts/02 - Discrete Wavelet Transform.md](02%20-%20Concepts/02%20-%20Discrete%20Wavelet%20Transform.md)
5. [02 - Concepts/03 - Chaotic Maps.md](02%20-%20Concepts/03%20-%20Chaotic%20Maps.md)

**Session 3** (~2 hours) — Understand the encryption pipeline
6. [02 - Concepts/04 - Confusion and Diffusion.md](02%20-%20Concepts/04%20-%20Confusion%20and%20Diffusion.md)
7. [02 - Concepts/05 - XOR Cipher.md](02%20-%20Concepts/05%20-%20XOR%20Cipher.md)
8. [02 - Concepts/06 - Security Metrics.md](02%20-%20Concepts/06%20-%20Security%20Metrics.md)

**Session 4** (~1.5 hours) — Internalize the talk
9. Re-read [01 - Project Report.md](01%20-%20Project%20Report.md) — it'll click much harder this time
10. Your own speaker script in [03 - Speaker Scripts/](03%20-%20Speaker%20Scripts/) — read out loud
11. [06 - Q&A and Rehearsal.md](06%20-%20Q%26A%20and%20Rehearsal.md) — answer each question out loud

After 4 sessions you can defend the paper.

---

## Final deliverables (graded files)

| File | Purpose |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` | The deck you actually project on screen |
| `CMP4221 - DWT Encryption Presentation.pdf` | PDF backup of the deck (in case PPTX dies) |
| `CMP4221 - DWT Encryption Study Deck.pptx` | Companion backup deck — extra slides for Q&A defense |
| `CMP4221 - DWT Encryption Study Deck.pdf` | PDF of the study deck |

To rebuild any of these from source, run from this folder:

```powershell
python _build/build_deck.py
```

---

## The one-line summary if your brain blanks during the talk

> *"This paper combines DWT compression with a 3D chaotic map to encrypt multiple color images of different sizes in a single cube, reaching 32 dB PSNR reconstruction and entropy of 7.9994 — compression and encryption in one pipeline."*

Memorize it. If you freeze, say it slowly, and you've earned 10 seconds to recover.

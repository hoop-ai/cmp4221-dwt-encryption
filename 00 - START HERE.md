---
sticker: emoji//1f6a6
tags:
  - course
  - multimedia
  - project
  - start
---
# START HERE — DWT Encryption Project

> **Paper:** *Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression* — Xu, Gao, Cao, Mou. ACM TOMM Vol 22 Issue 3, March 2026. [DOI 10.1145/3769123](https://doi.org/10.1145/3769123).
> **Group:** Abdul Rahman Malak (2285310) + Maria Alftaih (2285921).
> **Talk:** 10 minutes total, 5 min each, in Week 14 or 15.

---

## What's in this folder

Split into **stuff you actually open** (top level) and **deep reference** (`_reference/`, `_meta/`, `_build/`). Ignore anything that starts with `_` unless you specifically need it.

### The seven study files (read top to bottom in this order)

| # | File | What it is | Time |
|---|---|---|---|
| 1 | [What This Project Is](What%20This%20Project%20Is.md) 🗺️ | **Start here.** What's the assignment, what paper we picked, what we have to do. Zero technical content. | 10 min |
| 2 | [Plain English Walkthrough](Plain%20English%20Walkthrough.md) 👶 | The paper explained with everyday analogies. No math. No jargon. | 25 min |
| 3 | [Visual Cheat Sheet](Visual%20Cheat%20Sheet.md) 🎨 | Every concept as a diagram. For visual learners. | 15 min |
| 4 | [STUDY GUIDE](STUDY%20GUIDE.md) 📘 | Slide-by-slide deep dive. What to say, what to know, memory anchors. | 90 min |
| 5 | [Speaker Scripts/](Speaker%20Scripts/) 🎤 | Word-for-word lines. [Abdul](Speaker%20Scripts/Abdul%20(Slides%201-5).md) + [Maria](Speaker%20Scripts/Maria%20(Slides%206-10).md). | 30 min × passes |
| 6 | [_reference/Q&A and Rehearsal](_reference/Q%26A%20and%20Rehearsal.md) 🛡️ | 20 anticipated questions with model answers + rehearsal plan. | 30 min |
| 7 | [_reference/](_reference/) 📚 | Academic backup — project report, concept files, verbatim paper, Python code, equations walkthrough. | dip-in |

### The graded deliverables (what you actually project)

| File | What it is |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` / `.pdf` | The deck you project on screen |
| `CMP4221 - DWT Encryption Study Deck.pptx` / `.pdf` | Backup deck for Q&A defense |

### Hidden folders (ignore unless needed)

- **`_meta/`** — admin only. Prof brief, requirements breakdown, form schema, class channel message.
- **`_build/`** — Python script that generates the PPTX. Run `python _build/build_deck.py` to rebuild.

---

## How to get ready — pick your timeline

**If you have a few evenings (recommended):**
1. Read files 1, 2, 3 in one evening. (1 hour total — you understand the paper.)
2. Read file 4 (STUDY GUIDE) in a second evening. (90 min — you can defend each slide.)
3. Rehearse your speaker script with a timer, 2-3 times. Run Q&A drill with your partner.

**If you have 90 minutes:**
1. Skip to file 4 ([STUDY GUIDE](STUDY%20GUIDE.md)) with the deck open. Read top to bottom.
2. Glance at file 3 ([Visual Cheat Sheet](Visual%20Cheat%20Sheet.md)) for the diagrams.
3. Read your speaker script out loud once with a timer.

**If you have 30 minutes:**
1. Read [What This Project Is](What%20This%20Project%20Is.md) §6 + §11. (10 min — you know what we're doing.)
2. Read the **Panic-mode summary** at the top of [STUDY GUIDE](STUDY%20GUIDE.md). (5 min.)
3. Skim your speaker script out loud with a timer. (15 min.)

**Right before the talk:**
1. Re-read the **Defense moves** section at the bottom of [STUDY GUIDE](STUDY%20GUIDE.md).
2. Memorize **"Shrink. Stack. Scramble."** and the six headline numbers.

---

## The paper, in 60 seconds

1. **DWT (Discrete Wavelet Transform)** — splits a color image into 4 sub-bands. The paper keeps only LL (the smaller blurry version) and throws the rest away. Each image is now ¼ the size.
2. **3D chaotic map** — a deterministic function that looks random. The starting numbers are the encryption key.

The novelty: instead of encrypting one image at a time, the paper takes a batch of images, DWT-compresses each one, **stacks them all into a single 3D cube**, and encrypts the whole cube using the chaotic stream. Compression and encryption in one pass, on multiple images at once.

If you only ever remember one sentence: **shrink, stack, scramble.**

---

## The speaker split

| Slide | Speaker | Topic |
|---|---|---|
| 1 | Abdul | Title + thesis |
| 2 | Abdul | Problem — slow AND unsafe |
| 3 | Abdul | Two tools — DWT + chaos |
| 4 | Abdul | **Novelty** — encrypt the cube |
| 5 | Abdul | Pipeline + handoff to Maria |
| 6 | Maria | Confusion — scramble positions |
| 7 | Maria | Diffusion — XOR with chain |
| 8 | Maria | **Findings** — PSNR 32 dB beats prior work |
| 9 | Maria | Security — NIST, NPCR, UACI, entropy |
| 10 | Maria | Limitation + take-home |

The handoff line is **"Maria, over to you."** Practice the moment — it's the easiest part to fumble.

---

## Hard cap rules (from the prof)

- Over 10 minutes → cut off mid-sentence
- Under 8 minutes → looks unprepared
- Ideal target → 9:30 to 10:00
- Both speakers must talk roughly equally
- Both must cover technical content (no fluff role)

---

## If your brain blanks during the talk

Say slowly: *"This paper combines DWT compression with a 3D chaotic map to encrypt multiple color images in a single cube, reaching 32 dB PSNR and entropy 7.9994."*

That sentence buys you 8-10 seconds to recover.

---

## To rebuild the deck after edits

From this folder:

```powershell
python _build/build_deck.py
```

Outputs both PPTX and PDF files plus PNG previews in `_build/rendered/`.

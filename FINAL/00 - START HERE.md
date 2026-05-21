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

### The eight study files (read top to bottom in this order)

| # | File | What it is | Time |
|---|---|---|---|
| 1 | [What This Project Is](What%20This%20Project%20Is.md) 🗺️ | **Start here.** What's the assignment, what paper we picked, what we have to do. Zero technical content. | 10 min |
| 2 | [Plain English Walkthrough](Plain%20English%20Walkthrough.md) 👶 | The paper explained with everyday analogies. No math. No jargon. | 25 min |
| 3 | [Visual Cheat Sheet](Visual%20Cheat%20Sheet.md) 🎨 | Every concept as a diagram. For visual learners. | 15 min |
| 4 | [STUDY GUIDE](STUDY%20GUIDE.md) 📘 | Slide-by-slide deep dive. What to say, what to know, memory anchors. | 90 min |
| 5 | [Speaker Scripts/](Speaker%20Scripts/) 🎤 | Word-for-word lines, timed, with trim/expand options. [Abdul (Slides 1-8)](Speaker%20Scripts/Abdul%20(Slides%201-8).md) + [Maria (Slides 9-16)](Speaker%20Scripts/Maria%20(Slides%209-16).md). | 30 min × passes |
| 6 | [Pre-Talk Cheat Card](Pre-Talk%20Cheat%20Card.md) 🎫 | One printable page. Numbers, novelty, handoff, blank-recovery sentence. **Read this 5 min before walking up.** | 3 min |
| 7 | [../_reference/Q&A and Rehearsal](../_reference/Q%26A%20and%20Rehearsal.md) 🛡️ | 20 anticipated questions with model answers + rehearsal plan. | 30 min |
| 8 | [../_reference/](../_reference/) 📚 | Academic backup — project report, concept files, verbatim paper, Python code, equations walkthrough. | dip-in |

### The graded deliverables (what you actually project)

| File | What it is |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` / `.pdf` | The deck you project on screen |
| `CMP4221 - DWT Encryption Study Deck.pptx` / `.pdf` | Backup deck for Q&A defense |

### Hidden folders (ignore unless needed)

These live one level up at `../` (outside FINAL/):

- **`../_meta/`** — admin only. Prof brief, requirements breakdown, form schema, class channel message.
- **`../_reference/`** — academic backup material (project report, concepts, verbatim paper, code).
- **`../_build/`** — Python script that generates the PPTX/PDF. Run `python ../_build/build_deck.py` to rebuild.

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

**Right before the talk (5 minutes out):**
1. Open [Pre-Talk Cheat Card](Pre-Talk%20Cheat%20Card.md) — one page, everything you need.
2. Memorize **"Shrink. Stack. Scramble."** and the six headline numbers.
3. Whisper your handoff line out loud once.

---

## The paper, in 60 seconds

1. **DWT (Discrete Wavelet Transform)** — splits a color image into 4 sub-bands. The paper keeps only LL (the smaller blurry version) and throws the rest away. Each image is now ¼ the size.
2. **3D chaotic map** — a deterministic function that looks random. The starting numbers are the encryption key.

The novelty: instead of encrypting one image at a time, the paper takes a batch of images, DWT-compresses each one, **stacks them all into a single 3D cube**, and encrypts the whole cube using the chaotic stream. Compression and encryption in one pass, on multiple images at once.

If you only ever remember one sentence: **shrink, stack, scramble.**

---

## The speaker split (16 slides)

| Slide | Speaker | Topic |
|---|---|---|
| 1 | Abdul | Title + intros |
| 2 | Abdul | Paper in one breath (anchor) |
| 3 | Abdul | Color images are HEAVY (bandwidth) |
| 4 | Abdul | The wire is not safe (security) |
| 5 | Abdul | Two tools — DWT + chaos preview |
| 6 | Abdul | DWT splits into 4 sub-bands |
| 7 | Abdul | Keep LL, throw the rest — 1/4 size |
| 8 | Abdul | Chaos + handoff |
| 9 | Maria | **Novelty** — encrypt the cube |
| 10 | Maria | Pipeline overview (4 stages) |
| 11 | Maria | Stages 1-2: compress + stack |
| 12 | Maria | Confusion — scramble positions |
| 13 | Maria | Diffusion — XOR + chain |
| 14 | Maria | **Findings** — PSNR 32 dB beats prior work |
| 15 | Maria | Security — NIST, NPCR, UACI, entropy |
| 16 | Maria | Limitation + take-home + Q&A |

The handoff line is **"Maria, take it from here."** Maria responds **"Thanks Abdul"** and steps forward. Practice this moment — it's the easiest part to fumble.

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

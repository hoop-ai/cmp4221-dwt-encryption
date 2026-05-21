# CMP4221 — DWT Encryption Project

> Final project for **CMP4221 Multimedia Systems** (BAU, Spring 2026).
> Paired 10-minute paper presentation on a 2026 ACM TOMM journal paper.

**Group:** Abdul Rahman Malak (2285310) + Maria Alftaih (2285921)
**Course:** Asst. Prof. Dr. Selin Nacakli
**Talk:** 10 minutes, Week 14 or 15, both presenters cover technical content

---

## The paper

**Title:** Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression
**Authors:** Yidan Xu, Suo Gao, Yinghong Cao, Jun Mou
**Journal:** ACM Transactions on Multimedia Computing, Communications, and Applications, Vol. 22 Issue 3, March 2026
**DOI:** [10.1145/3769123](https://doi.org/10.1145/3769123)
**Free access:** Yes (open access on ACM DL)

**One-line summary:**
> *This paper combines DWT compression with a 3D chaotic map to encrypt multiple color images of different sizes in a single cube, reaching 32 dB PSNR reconstruction and entropy of 7.9994 — compression and encryption in one pipeline.*

**Three magic words:** SHRINK → STACK → SCRAMBLE.

---

## How to use this repo

### Reading order (start at the top, go down)

| # | File | What it is | Time |
|---|---|---|---|
| 1 | [What This Project Is](What%20This%20Project%20Is.md) | **Start here.** Orientation. What's the assignment, what paper we picked, what we have to do. Zero technical content. | 10 min |
| 2 | [Plain English Walkthrough](Plain%20English%20Walkthrough.md) | The paper explained with everyday analogies. No math. No jargon. | 25 min |
| 3 | [Visual Cheat Sheet](Visual%20Cheat%20Sheet.md) | Every concept as a diagram. Mermaid + ASCII art. | 15 min |
| 4 | [STUDY GUIDE](STUDY%20GUIDE.md) | Slide-by-slide deep dive. What to say, what to know, memory anchors, Q&A defense. | 90 min |
| 5 | [Speaker Scripts/](Speaker%20Scripts/) | Word-for-word lines for each presenter | 30 min × passes |
| 6 | [_reference/Q&A and Rehearsal](_reference/Q%26A%20and%20Rehearsal.md) | 20 anticipated audience questions with model answers + rehearsal plan | 30 min |
| 7 | [_reference/](_reference/) | Academic backup material — full project report, concept files, verbatim paper text, equations walkthrough, reference Python implementation | dip-in |

### Hidden folders (ignore unless you need them)

- **[_meta/](_meta/)** — admin only: prof brief, requirements breakdown, form schema, class channel message
- **[_build/](_build/)** — the Python script that generates the .pptx and .pdf

---

## Graded deliverables (what gets projected)

| File | Purpose |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` | The deck projected during the talk |
| `CMP4221 - DWT Encryption Presentation.pdf` | PDF backup of the deck |
| `CMP4221 - DWT Encryption Study Deck.pptx` | Companion backup deck with extra slides for Q&A defense |
| `CMP4221 - DWT Encryption Study Deck.pdf` | PDF of the study deck |

To rebuild from source:

```powershell
python _build/build_deck.py
```

(Requires `pip install python-pptx`.)

---

## Numbers to memorize cold

If you only remember 6 numbers, remember these:

- **PSNR 32.06 dB** — reconstruction quality (vs prior work at 26–27 dB)
- **NPCR 99.6533%** — pixel-change rate (ideal: 99.6094%)
- **UACI 33.4887%** — average intensity change (ideal: 33.4635%)
- **Information entropy 7.9994 bits** — basically max (8 for 8-bit)
- **NIST 15/15** — chaotic stream passes all 15 randomness tests
- **Key space ≥ 2¹⁰⁰** — brute force is infeasible

These 6 numbers answer 80% of "how good is the security" questions.

---

## If you're starting from zero and have only 30 minutes

Skip everything else. Do this:

1. Read [What This Project Is](What%20This%20Project%20Is.md) sections 6 and 11 (10 min) — what's the assignment, what we found
2. Read the **Panic-mode summary** at the top of [STUDY GUIDE](STUDY%20GUIDE.md) (5 min)
3. Read your speaker script out loud with a timer (15 min)

You'll survive.

---

## License

Educational use only. The paper itself is © ACM (open access); see DOI for citation.

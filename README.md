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

---

## How to use this repo (read in this order)

| Step | File | What it gives you |
|---|---|---|
| 0 | [`00 - START HERE.md`](00%20-%20START%20HERE.md) | Navigation + 4-session study plan |
| 1 | [`01 - Project Report.md`](01%20-%20Project%20Report.md) | Master 15-20 page report on the paper |
| 2 | [`02 - Concepts/`](02%20-%20Concepts/) | 8 explainers — image encryption, DWT, chaotic maps, confusion/diffusion, XOR, security metrics, glossary, notation |
| 3 | [`03 - Speaker Scripts/`](03%20-%20Speaker%20Scripts/) | Word-for-word scripts for each speaker (Abdul slides 1-5, Maria slides 6-10), timed and trimmable |
| 4 | [`04 - The Paper/`](04%20-%20The%20Paper/) | Verbatim paper text + plain-English walkthrough of all 18 equations + figure index |
| 5 | [`05 - Code/`](05%20-%20Code/) | Reference Python implementation of the algorithm + line-by-line walkthrough |
| 6 | [`06 - Q&A and Rehearsal.md`](06%20-%20Q%26A%20and%20Rehearsal.md) | 20 anticipated audience questions + rehearsal plan + stage directions |
| 7 | [`07 - Slide Deck Source.md`](07%20-%20Slide%20Deck%20Source.md) | Markdown source of the slides — mirrors the .pptx content |
| — | [`_meta/`](_meta/) | Prof brief, requirements breakdown, form schema (admin only) |
| — | [`_build/`](_build/) | Python script that builds the .pptx and .pdf deliverables |

## Deliverables (graded files)

| File | Purpose |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` | The deck projected during the talk |
| `CMP4221 - DWT Encryption Presentation.pdf` | PDF backup of the deck |
| `CMP4221 - DWT Encryption Study Deck.pptx` | Companion backup deck with extra slides for Q&A defense |
| `CMP4221 - DWT Encryption Study Deck.pdf` | PDF of the study deck |

To rebuild any of these:

```powershell
python _build/build_deck.py
```

(Requires `pip install python-pptx`.)

---

## Speaker split

| Slide | Speaker | Content |
|---|---|---|
| 1 | Abdul | Title + paper intro |
| 2 | Abdul | Problem (bandwidth + safety) |
| 3 | Abdul | Two ingredients (DWT + chaotic map) |
| 4 | Abdul | **Novelty** (encrypt the cube) |
| 5 | Abdul | Pipeline overview + **handoff** |
| 6 | Maria | Confusion (scramble positions) |
| 7 | Maria | Diffusion (XOR with chaos) |
| 8 | Maria | **Findings** (PSNR 32 dB beats prior work) |
| 9 | Maria | Security (NIST, NPCR, UACI, IE) |
| 10 | Maria | Limitation + take-home |

Both speakers aim for ~5:00 each, 10:00 total. Both blocks are 100% technical content (per professor's grading criteria).

---

## Numbers to memorize

If you only remember 6 numbers, remember these:

- **PSNR 32.06 dB** — reconstruction quality (vs prior work at 26–27 dB)
- **NPCR 99.6533%** — pixel-change rate (ideal: 99.6094%)
- **UACI 33.4887%** — average intensity change (ideal: 33.4635%)
- **Information entropy 7.9994 bits** — basically max (8 for 8-bit)
- **NIST 15/15** — chaotic stream passes all 15 randomness tests
- **Key space ≥ 2¹⁰⁰** — brute force is infeasible

These 6 numbers answer 80% of "how good is the security" questions.

---

## License

Educational use only. The paper itself is © ACM (open access); see DOI for citation.

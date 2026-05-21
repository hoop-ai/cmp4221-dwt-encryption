---
sticker: emoji//1f4cb
tags:
  - course
  - multimedia
  - project
  - requirements
---
# Requirements Breakdown — what the professor actually said

> Source: [[Project Brief]] (verbatim teacher announcement). Each section below quotes the exact lines from the brief, then says what they mean operationally and how we satisfy them.

---

## Section 1 — Sources we are allowed to use

**Verbatim quote:**
> "I want each group to choose 1 paper published in year 2026 from either https://dl.acm.org/loi/tomm (ACM Transactions on Multimedia Computing, Communications, and Applications) or https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=11342315&punumber=6046 (IEEE Transactions on Multimedia). You can access all the papers with your BAU credentials."

**What it means:**

| Constraint | Allowed |
|---|---|
| Number of papers | Exactly **one** |
| Year | **2026** only |
| Journal #1 | ACM TOMM (ACM Transactions on Multimedia Computing, Communications, and Applications) |
| Journal #2 | IEEE Transactions on Multimedia |
| Access | Through BAU credentials (SSO) |

**Anything else is off-limits.** Conferences, other journals, preprints, books — none qualify. No matter how good the paper is, if it's not in those two journals and not from 2026, the entry will be rejected.

**How we comply:** We picked from ACM TOMM, **Vol. 22 Issue 3, March 2026** — the journal is exactly the first allowed source, the year is exactly 2026 (verified via Crossref: published online 2026-02-27, print 2026-03-31).

---

## Section 2 — Paper-choice rules (which specific paper)

**Verbatim quote:**
> "in order to make your entry, you need to form your group and also choose the paper. I will not consider incomplete entries."
>
> "You can check previously selected papers from this link: CMP4221 Paper Presentations.xlsx You need to make sure that you are choosing a paper that was not selected before. Paper titles will also be first-come-first-served. Just before your form entry, make sure that paper is not in the Excel to have no issues."
>
> "If your entry is not valid (missing information, paper chosen previously, student in two different groups etc..), then I will delete that entry and you need to make a valid entry which may cause you to lose your week preference."

**What it means:**

1. **Form your group first** — Abdul + Maria — done.
2. **Pick the paper before submitting** — done.
3. **Verify not previously taken** — Ctrl+F the title in the Excel right before submitting. **Paper titles are first-come-first-served**: once a title is in the Excel, no other group can take it.
4. **Both students locked to one group** — same student cannot appear in two groups.
5. **Incomplete = deleted** — missing names, missing IDs, missing paper, or duplicated title means the entry gets thrown out and you might lose your preferred week.

**How we comply:** Group is formed (Abdul Rahman Malak 2285310 + Maria Alftaih 2285921). Paper is chosen (DWT Encryption, DOI 10.1145/3769123). The pre-submit check (Ctrl+F in the Excel) is on Abdul to perform tonight.

---

## Section 3 — Best paper to choose (our criteria, since the brief doesn't say)

**The brief gives only structural rules** (year + journal + not duplicate). It does **not** rank papers. So "best" is ours to define. Our chosen criteria, in priority order:

| Priority | Criterion | Why it matters |
|---|---|---|
| 1 | **Math difficulty fits an undergrad audience** | We've studied DCT/Huffman/convolution. Variational calculus, ADMM, transformers, NeRFs are out of scope. |
| 2 | **Course-topic alignment** | The professor will reward visible connection to W3-W6 lectures. |
| 3 | **Single, intuitive novelty** | "Encrypt the cube" is one sentence. Easier to defend in Q&A than multi-component systems. |
| 4 | **Visual results** | Encrypt-then-decrypt before/after = audience-friendly slides. |
| 5 | **Short, self-contained paper** | 20 pages digestible in two reads; not buried in supplementary material. |
| 6 | **Open access if possible** | No paywall friction during prep; instructor can verify the source easily. |

**Why DWT Encryption wins on all six:**

| Criterion | DWT Encryption status |
|---|---|
| Math difficulty | **3/10** — only paper in our 254-paper pool with zero advanced ML. Pure DWT + chaotic-map cryptography. |
| Course-topic alignment | DWT is the wavelet sister of W6 DCT. XOR diffusion is high-school CS. NPCR/UACI/IE are arithmetic. |
| Single novelty | "Encrypt the cube of multiple stacked LL sub-bands as one object." |
| Visual results | Plaintext → cipher cube → recovered image, all shown in Fig. 7. Striking. |
| Length | 20 pages, single article (Article 82 in Vol 22 Issue 3). |
| Open access | **Yes** — paper labelled "Free access" on ACM DL. No BAU SSO needed. |

---

## Section 4 — How the presentation must be structured

**Verbatim quote:**
> "In the last 2 weeks (Week 14 and Week 15) there will be student presentations. We can spare 10 minutes per each group because of time limitations."
>
> "You will read the paper and present the novelty, methodology and the findings of the paper in 10 minutes with your partner. Make sure that each student is presenting equally for approximately 5 minutes."

**What it means:**

| Format rule | Mandatory value |
|---|---|
| When | Week 14 OR Week 15 (chosen on form, first-come-first-served) |
| Total length | **10 minutes** (instructor will cut; "time limitations" wording is firm) |
| Speakers | **2 students**, both presenting |
| Per-speaker length | **~5 minutes each, equal split** |
| Required content (3 sections) | **Novelty · Methodology · Findings** |
| Prep | "Read the paper" — both partners must read it |

**The three required content blocks (instructor's exact words):**

1. **Novelty** — what's new in this paper vs prior work
2. **Methodology** — how the proposed approach actually works
3. **Findings** — what numbers and conclusions the authors report

**How our deck satisfies the structure:**

| Required block | Where it lives in our deck |
|---|---|
| Title + setup | Slide 1 (Abdul) |
| Background / motivation | Slides 2–3 (Abdul) |
| **Novelty** | **Slide 4** (Abdul) — explicit, dedicated |
| **Methodology** | **Slides 5–7** (Slide 5 Abdul → Maria handoff; slides 6–7 Maria) |
| **Findings** | **Slides 8–9** (Maria) — PSNR results + security scorecard |
| Take-home | Slide 10 (Maria) |
| Speaker split | Abdul slides 1-5 ≈ 5 min · Maria slides 6-10 ≈ 5 min |
| Total time | 10:30 scripted with documented trim points to land at 10:00 |

---

## Section 5 — What the professor actually wants delivered

The brief asks for **two distinct deliverables** at two different times.

### Deliverable 1 — the FORM ENTRY (due tonight, end of April)

**Verbatim quote:**
> "One student from each group will make a form entry from the Tab above named as Fill | CMP4221 Paper Presentations (next to Posts and Shared). Week preference will work on first-come-first-served basis. However, in order to make your entry, you need to form your group and also choose the paper. I will not consider incomplete entries. The entries should be finished by the end of April."
>
> "After making your entry, check the link again to make sure that your entry is saved in the Excel provided. If not contact me."

**What it requires (from the sample classmate entry decoded in [[Form Schema + Sample Entry]]):**

| Field | Our value |
|---|---|
| Submitter email | `abdul.malak@bahcesehir.edu.tr` |
| Submitter name + student ID | `Abdul Rahman Malak 2285310` |
| Partner name + student ID | `Maria Alftaih 2285921` |
| Week preference | `Week 14` (first-come-first-served preference) |
| Paper title | `Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression` |
| DOI | `10.1145/3769123` |
| Paper URL | `https://doi.org/10.1145/3769123` |

**Verification step (also part of the deliverable):**
After submitting, re-open the Excel and confirm your row exists. If it's not there within a few minutes, email the instructor.

**Status:** ⏳ **Not yet submitted. This is the only thing standing between us and being done with the form deliverable today.**

### Deliverable 2 — the LIVE PRESENTATION (Week 14 or 15)

A **live, 10-minute paired talk** on the chosen paper, structured around novelty / methodology / findings, delivered in front of the class with both students speaking ~5 minutes each.

**The professor did NOT ask for:**
- ❌ A separate written report
- ❌ A submitted PowerPoint file
- ❌ A submitted PDF
- ❌ Speaker notes turned in
- ❌ A code implementation

**The deliverable is the live performance, not a file upload.** The .pptx and .pdf we've built are the *tools we use* during the presentation, not the deliverable itself. (Unless the professor asks separately for the slides — then we hand them over.)

**Status:** ✅ Tools ready: graded deck + study deck + Q&A prep + speaker scripts ≈ 1,800 words. ⏳ Rehearsal still on us in the weeks before Week 14.

---

## TL;DR — the four checks against the brief

| # | Brief requirement | Our compliance |
|---|---|---|
| 1 | One 2026 paper from ACM TOMM or IEEE TMM | ✅ ACM TOMM Vol 22 Issue 3, March 2026 |
| 2 | Group of 2 students, both verified | ✅ Abdul (2285310) + Maria (2285921) |
| 3 | 10-minute paired live presentation, ~5 min each, covering novelty + methodology + findings | ✅ Deck built, scripts written, structure maps each block |
| 4 | Form entry submitted by end of April with all info, paper not previously taken, entry verified in Excel afterward | ⏳ **Pending — submit tonight** |

We are 75% done. The remaining 25% is one form submission tonight, then rehearsal before Week 14.

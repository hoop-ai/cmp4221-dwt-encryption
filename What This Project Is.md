---
sticker: emoji//1f5fa
tags:
  - orientation
  - beginner
  - context
---
# What This Project Is

> **Read this FIRST. Before anything else.**
> If you have no idea what you're looking at, this file orients you.
> No technical content. Just the big picture of what we're doing and why.

---

## 1. What class is this for?

**CMP4221 — Multimedia Systems.** It's a 4th-year course at BAU. The professor is **Asst. Prof. Dr. Selin Nacakli**.

The course covers stuff like image compression, signal processing, encryption — basically how computers handle pictures, video, and audio. We're at the end of the semester, in Week 13.

---

## 2. What does the professor want us to do?

She gave one big assignment for the whole semester. Here's the rule, in plain English:

| What she wants | What it means |
|---|---|
| **Work in pairs of 2** | Two people per group. We're Abdul + Maria. |
| **Pick one journal paper from 2026** | Find a 2026 academic paper on a multimedia topic |
| **From ACM TOMM or IEEE TMM** | Only papers from these two specific journals count. Anything else gets rejected. |
| **Give a 10-minute presentation** | We have to stand in front of the class and explain the paper |
| **Both speakers must talk 5 minutes each** | Equal time. She specifically said "approximately 5 minutes." |
| **Cover 3 things: novelty, methodology, findings** | What's new in the paper, how it works, what they discovered |
| **Slide style is graded** | The PowerPoint has to look professional |
| **Both must cover technical content** | One person can't just do "intro" while the other does math. Both have to teach something |

That's the whole assignment. **There is no written report deliverable.** The prof grades you on:
- How good your slides look
- How you present (body language, voice, confidence)
- Whether your content makes sense
- Whether you hit the 10-minute mark cleanly

---

## 3. So why is this folder called a "report" / "study folder"?

Because **we built our own study materials**, even though the prof didn't ask for them. The reason: we need to UNDERSTAND the paper before we can present it. The paper is technical — we'd embarrass ourselves if we just memorized slides without knowing what they mean.

So this folder has two kinds of files:

| Kind | Purpose | Examples |
|---|---|---|
| **Graded deliverable** | What we actually present in class | The .pptx slide deck, the .pdf backup |
| **Study materials** (everything else) | For us to learn the paper privately | This file, STUDY GUIDE, Plain English Walkthrough, Visual Cheat Sheet, Speaker Scripts |

**Nobody but us reads the study materials.** They exist so we can show up to class knowing what we're talking about. The prof only sees the slides + hears us speak.

---

## 4. What paper did we pick?

**Title:** *Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression*

**Translation of the title:** "A way to encrypt multiple photos at once, using two ideas: a chaotic math system and a compression trick called DWT."

**Authors:** Yidan Xu, Suo Gao, Yinghong Cao, Jun Mou (researchers in China)
**Journal:** ACM Transactions on Multimedia Computing, Communications, and Applications (ACM TOMM)
**Published:** March 2026
**DOI (the paper's permanent ID):** [10.1145/3769123](https://doi.org/10.1145/3769123)

The paper is **20 pages long** and **freely available online**.

---

## 5. Why this paper?

We had 254 candidate papers to pick from. We chose this one because:

| Reason | Detail |
|---|---|
| **Easy math** | Most papers use deep learning / fancy math we haven't studied. This one uses stuff we DO know: DWT (similar to the DCT we learned for JPEG), and basic XOR (high-school logic). |
| **One clear novelty** | "Encrypt the cube of stacked images" — easy to explain in one sentence. Multi-component papers are hard to defend in Q&A. |
| **Cool visuals** | The paper has nice before/after pictures of encrypted vs decrypted images — good for slides. |
| **Short** | 20 pages is digestible. |
| **Free access** | No paywall = the prof can verify the paper easily. |
| **Course-relevant** | DWT is exactly the kind of transform she taught us (Week 6 on image compression). |

---

## 6. What does "analyzing a paper" mean?

When the prof says "read the paper and present the novelty, methodology, and findings," she wants us to do three things:

### A. Understand the PROBLEM the paper is solving

Every research paper exists because some existing problem wasn't solved well enough. Our job: figure out what problem this paper attacks.

> **For our paper:** "Sending multiple color images across a network is slow (images are big) AND unsafe (anyone can intercept them). Current solutions handle the two problems separately, one image at a time, which is wasteful."

### B. Understand the SOLUTION the paper proposes

How does the paper actually solve the problem? What's the new idea?

> **For our paper:** "Shrink every image with DWT, stack them all into a 3D cube, and encrypt the whole cube as one object using a chaotic system."

### C. Understand the EVIDENCE the paper provides

How do they prove their solution actually works? What numbers/experiments back it up?

> **For our paper:** "Six different tests — PSNR, NPCR, UACI, information entropy, NIST randomness, and robustness checks. All pass. Reconstruction quality (32 dB) beats four prior schemes (26-27 dB)."

That's analyzing a paper. Three questions: **what problem, what solution, what evidence.**

---

## 7. What did we find by reading the paper?

We read the paper end-to-end and pulled out these key takeaways:

### The novelty (slide 9 — the most important slide)

> Instead of encrypting one image at a time, encrypt a whole BATCH of images at once by stacking them into a 3D cube.

That's the paper's contribution in one sentence. **The professor specifically grades on "novelty," so this is where the points are.**

### The methodology (how it actually works)

The encryption has **4 stages**:

1. **DWT compression** — shrink each image to 1/4 size by keeping only the "LL" sub-band.
2. **Stacking** — pile the shrunken images into a 3D cube.
3. **Confusion** — scramble pixel POSITIONS using random offsets from a chaotic system.
4. **Diffusion** — flip pixel VALUES using XOR with a chaotic stream, with each output linked to the previous one (creating an avalanche effect).

To decrypt, you run all 4 stages backwards with the same secret key.

### The findings (what numbers they got)

Six results, all good:

| Metric | What it measures | Their number | Status |
|---|---|---|---|
| **PSNR** | Reconstruction quality | 32.06 dB | Above the 30 dB visual threshold |
| **NPCR** | Avalanche on 1-pixel changes | 99.65% | Right on the ideal 99.61% |
| **UACI** | Avalanche intensity | 33.49% | Right on the ideal 33.46% |
| **Entropy** | Randomness of cipher | 7.9994/8 | Basically max |
| **NIST suite** | Randomness of key stream | 15/15 pass | All pass |
| **Beats prior work** | vs 4 other schemes | by 4-6 dB on PSNR | Significantly better |

### The limitation (honest weakness)

When the images in a batch have different sizes, the cube has to be padded with zeros. That wastes space. The authors openly admit this is future work.

**Saying "no limitations" in academic Q&A looks fake. Owning a real limitation is honest and scores points.**

---

## 8. What are we presenting?

A **10-minute slide presentation** to the class. The deck has **16 slides** that walk through:

```
SLIDES 1-2:    Title + the paper in one breath
SLIDES 3-4:    The two problems (slow + unsafe)
SLIDES 5-8:    The two tools (DWT + chaotic map)
SLIDE 9:       ★ THE NOVELTY ★ (encrypt the cube, not the images)
SLIDES 10-13:  The 4-stage encryption pipeline
SLIDE 14:      Headline result (PSNR 32.06 dB beats prior work)
SLIDE 15:      Security analysis (all 4 checks pass)
SLIDE 16:      Limitation + take-home + "Questions?"
```

**Speaker split** (per prof requirement: equal time, both technical):

- **Abdul:** slides 1-8 (~5 minutes) — title, problems, tools, novelty
- **Maria:** slides 9-16 (~5 minutes) — wait, let me adjust... actually depends on slide deck version

> ⚠️ **Note:** The current deck has 16 slides. The original speaker scripts in `Speaker Scripts/` were written for the 10-slide version. They'll need to be re-split. But the substance carries over — both speakers cover technical content and aim for ~5 minutes each.

**The handoff line:** Whoever speaks first ends their half with *"Maria, over to you"* (or vice versa) and the other person physically steps forward. **Practice this — it's the easiest moment to fumble.**

---

## 9. How does the rest of this folder help?

Now that you know what the project IS, here's what each file/folder helps you DO:

| File | Use it when... |
|---|---|
| **[Plain English Walkthrough](Plain%20English%20Walkthrough.md)** | You need to understand the paper using everyday analogies, zero math |
| **[Visual Cheat Sheet](Visual%20Cheat%20Sheet.md)** | You're a visual learner, want diagrams of everything |
| **[STUDY GUIDE](STUDY%20GUIDE.md)** | You want a slide-by-slide deep dive — what each slide means, what to say |
| **[Speaker Scripts/](Speaker%20Scripts/)** | You're rehearsing your half out loud and need the word-for-word lines |
| **[_reference/](_reference/)** | You want the academic-style backup material — full report, concept files, verbatim paper text, code |
| **[_meta/](_meta/)** | You want to verify the prof's exact wording or fill out the submission form |

### Recommended reading order (for someone who knows NOTHING)

1. **This file** ← *you are here* (5 min) — what's the project, what's the assignment
2. **[Plain English Walkthrough](Plain%20English%20Walkthrough.md)** (25 min) — what's the paper, with analogies
3. **[Visual Cheat Sheet](Visual%20Cheat%20Sheet.md)** (15 min) — same concepts, in diagrams
4. **[STUDY GUIDE](STUDY%20GUIDE.md)** (90 min) — slide-by-slide deep dive, what to say
5. **Your own [speaker script](Speaker%20Scripts/)** (30 min) — read out loud, with a timer
6. **[Q&A and Rehearsal](_reference/Q%26A%20and%20Rehearsal.md)** (30 min) — practice answering hard questions

**Total: ~3 hours.** Spread over 2-3 evenings. After that you can defend the paper.

---

## 10. The simple checklist for showing up ready

Tick off each item before presentation day:

- [ ] Read this file (orientation)
- [ ] Read [Plain English Walkthrough](Plain%20English%20Walkthrough.md) (the paper as analogies)
- [ ] Glance through [Visual Cheat Sheet](Visual%20Cheat%20Sheet.md) (visual reinforcement)
- [ ] Read [STUDY GUIDE](STUDY%20GUIDE.md) (the deep dive)
- [ ] Memorize the **6 numbers**: 32.06 dB, 99.65%, 33.49%, 7.9994, 15/15, ≥2¹⁰⁰
- [ ] Memorize the **3-word summary**: "Shrink. Stack. Scramble."
- [ ] Read your [speaker script](Speaker%20Scripts/) out loud 3+ times with a timer
- [ ] Practice the handoff line and the physical step-forward swap with your partner
- [ ] Read [Q&A and Rehearsal](_reference/Q%26A%20and%20Rehearsal.md) — answer each Q out loud
- [ ] On the morning of: re-read the **Panic-mode summary** at the top of [STUDY GUIDE](STUDY%20GUIDE.md)

That's the path. Don't skip steps. Don't try to memorize the equations. **Understand the story, internalize the headline numbers, rehearse your script with a timer, and you'll do fine.**

---

## 11. If you only have 30 minutes total

Forget everything above. Just do these in order:

1. Read **section 6** of this file (5 min) — the three questions: what problem, what solution, what evidence
2. Read the **Panic-mode summary** at the top of [STUDY GUIDE](STUDY%20GUIDE.md) (5 min)
3. Read your **speaker script** out loud with a timer (10 min)
4. Read the **Defense moves** section at the bottom of [STUDY GUIDE](STUDY%20GUIDE.md) (5 min)
5. Memorize **"Shrink, Stack, Scramble"** and **"PSNR 32 dB beats prior work"** (5 min)

You'll survive.

---

## The single most important thing to remember

> **The professor grades on three things: novelty, methodology, findings.**
> **Slide 9 is the novelty. Slides 10-13 are the methodology. Slides 14-15 are the findings.**
> **Hit those three blocks clearly and you've earned most of the points.**

---
sticker: emoji//1f5fa
tags:
  - course
  - multimedia
  - project
  - briefing
---
# What This Project Is

> 10-minute briefing. Zero technical content. Just: what's the assignment, what we picked, what we have to do, and who does what.

---

## §1. The assignment

CMP4221 Multimedia Systems with Asst. Prof. Dr. Selin Nacakli. The project replaces a final exam component. Each pair of students picks **one paper published in 2026** from one of these two journals:

- ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM)
- IEEE Transactions on Multimedia (TMM)

The pair then gives a **10-minute presentation** on the paper. Each speaker holds the floor for about 5 minutes. Both must talk about technical content — no one gets to do "intro stuff" while the other carries the math.

## §2. The grading

The professor grades on four things, all roughly equal weight:

1. **Slide style** — does the PowerPoint look good
2. **Presentation delivery** — pacing, body language, handoff
3. **Content explanation** — do you understand what you're saying, can you defend it
4. **Time usage** — close to 10:00. Over → cut off. Under 8:00 → looks unprepared

The professor wants three specific content blocks visible in the deck:

- **Novelty** — what's new about the paper
- **Methodology** — how it works, step by step
- **Findings** — what numbers came out

If any of those three is missing or unclear, points come off.

## §3. The paper we picked

**Title:** *Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression*

**Authors:** Yidan Xu · Suo Gao · Yinghong Cao · Jun Mou

**Venue:** ACM TOMM, Volume 22, Issue 3, Article 82, pages 1-20

**Published:** Online 2026-02-27 · Print 2026-03-31

**DOI:** [10.1145/3769123](https://doi.org/10.1145/3769123)

It's a 20-page journal paper about image encryption. We chose it because the topic connects to multimedia (it operates on color images), it uses the wavelet transform we covered in lecture, and the novelty is clear enough to explain in 10 minutes.

## §4. The group

| Name | Student ID | Slides |
|---|---|---|
| Abdul Rahman Malak | 2285310 | 1-5 |
| Maria Alftaih | 2285921 | 6-10 |

## §5. The split — what each speaker covers

**Abdul (slides 1-5, ~5 minutes):**

- Slide 1: Title + thesis
- Slide 2: The problem — sending color images is slow AND unsafe
- Slide 3: The two tools we use — DWT + chaos
- Slide 4: **The novelty** — stack the images into a cube, encrypt the cube
- Slide 5: The pipeline + handoff line to Maria

**Maria (slides 6-10, ~5 minutes):**

- Slide 6: Confusion — scramble pixel positions
- Slide 7: Diffusion — XOR with chaos, chain to previous output
- Slide 8: **The findings** — PSNR 32 dB beats prior work
- Slide 9: Security — 4 tests, all pass
- Slide 10: Limitation + take-home + Q&A invitation

The handoff happens at the end of slide 5 when Abdul says **"Maria, over to you."** Maria physically steps forward.

## §6. What the paper is actually about — in one paragraph

The authors solve a practical networking problem: sending color images is slow because color images are big (three channels), and it's unsafe because anyone tapping the network can see what you're sending. The standard fix is to compress, then encrypt, then send each image one at a time. The paper proposes something cleaner: shrink every image with the wavelet transform, stack the shrunken images into a single 3D block they call a *cube*, and encrypt the whole cube in one pass using a chaotic system. So instead of doing compression and encryption separately on each image, both jobs happen together on the whole batch. That's the contribution.

## §7. What you have to physically do on presentation day

1. Show up to class on time.
2. When your slot is called, both go to the front. One of you brings a laptop or uses the projector PC with your PDF backup.
3. Open the deck PDF — backup in case the PPTX fails.
4. Abdul opens with the title slide. Both should be on camera/visible.
5. Talk through slides 1-5 (Abdul), hand off, slides 6-10 (Maria).
6. Sit down. Take audience questions for ~2 minutes.

## §8. What you must NOT do

- **Go over 10 minutes** — the professor explicitly said she will cut you off mid-sentence.
- **Read every slide word-for-word from the deck** — you can use printed speaker notes, but make eye contact too.
- **One person dominates** — both must speak for roughly 5 minutes each.
- **Skip technical content** — both speakers cover algorithms, results, or methodology. No "intro role."
- **Forget the handoff** — practice "Maria, over to you" out loud at least three times.

## §9. The deliverables already in this folder

| File | Purpose |
|---|---|
| `CMP4221 - DWT Encryption Presentation.pptx` | The deck you project on screen |
| `CMP4221 - DWT Encryption Presentation.pdf` | Backup of the deck in case PPTX fails |
| `CMP4221 - DWT Encryption Study Deck.pptx` | Backup defense deck for Q&A (do NOT present) |
| `CMP4221 - DWT Encryption Study Deck.pdf` | Backup PDF of the study deck |
| `Speaker Scripts/Abdul (Slides 1-5).md` | Word-for-word lines for Abdul |
| `Speaker Scripts/Maria (Slides 6-10).md` | Word-for-word lines for Maria |

## §10. The study materials (also in this folder)

You don't need to read the paper itself. You need to read these three files, in this order:

1. **[Plain English Walkthrough](Plain%20English%20Walkthrough.md)** — the paper in everyday language, with analogies. No math, no jargon. 25 minutes.
2. **[Visual Cheat Sheet](Visual%20Cheat%20Sheet.md)** — every concept as a diagram. 15 minutes.
3. **[STUDY GUIDE](STUDY%20GUIDE.md)** — slide-by-slide deep-dive with worked examples and Q&A defense. 90 minutes.

After those three, you can defend the talk against any reasonable question.

## §11. The single sentence to memorize

**"Shrink, stack, scramble."**

If your brain blanks during the talk, those three words ARE the paper:

- Shrink = each image gets compressed by DWT to ¼ size
- Stack = the shrunken images are stacked into a 3D cube
- Scramble = the cube is encrypted with chaos

Everything else is detail under that umbrella.

## §12. The key numbers (you will be asked)

| Number | What it means |
|---|---|
| **32.06 dB** | Image quality after the full encrypt-decrypt round trip. Above the 30 dB visual threshold. |
| **¼ size** | DWT shrinks each image to one-quarter the original size |
| **99.65 %** | NPCR — how much the cipher changes if you flip one input pixel. Ideal target hit. |
| **7.9994 / 8** | Entropy — cipher is statistically indistinguishable from random noise |
| **15 / 15** | NIST randomness tests — all passed |

## §13. The honest limitation (always admit if asked)

When images in a batch have different sizes, the cube has to be padded with zeros. That wastes space. The authors openly flag this as future work. Always admit this if a question pushes you — honesty about limitations scores points. Trying to hide it does not.

---

**Next read:** [Plain English Walkthrough](Plain%20English%20Walkthrough.md) — same content, but with stories and analogies instead of jargon.

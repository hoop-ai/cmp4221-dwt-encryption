---
sticker: emoji//1f399
tags:
  - speaker
  - script
  - abdul
  - presentation
---
# Speaker Script — Abdul (Slides 1–8, ~5:00)

> **Word-for-word script.** Matches the 16-slide deck.
> Read out loud while timing yourself. Each slide has a target time.
> **Total target: 5:00.** Cadence: ~150 wpm (calm, not rushed).

> **The handoff line at the end of slide 8 is the most important sentence in your half.** Memorize it. Then physically take one step back as Maria steps forward.

---

## Slide 1 — Title (≈ 0:25)

**On-screen:** Paper title, authors (Xu, Gao, Cao, Mou), journal (ACM TOMM, March 2026), DOI, your names.

**Script:**

> *"Hi everyone, I'm Abdul, and this is Maria. We picked a paper from this March's ACM Transactions on Multimedia, by Xu, Gao, Cao, and Mou. The paper is about encrypting multiple color images at once, using two ideas we've already met in class. I'll do the first half — the problem, the tools, and what's new. Maria will take the algorithm details and the results."*

**Stage direction:** Calm, friendly tone. Smile briefly. Don't rush.

---

## Slide 2 — The paper in one breath (≈ 0:30)

**On-screen:** One-sentence thesis: *"Take a batch of color images. Shrink each one with DWT. Stack them into one cube. Scramble the cube with chaos."* Small visual: batch → cube → cipher.

**Script:**

> *"Before we get into details — here's the entire paper in one sentence. The authors take a batch of color photos, shrink them all using the wavelet transform, stack the shrunken images into a single 3D block they call a cube, and then scramble the whole cube using chaos. So in one pipeline you get compression AND encryption AND it works on the whole batch instead of one image at a time. If you remember nothing else from the next 10 minutes — remember that."*

**Stage direction:** Slow down at *"if you remember nothing else."* This is your anchor line.

---

## Slide 3 — Color images are HEAVY (≈ 0:35)

**On-screen:** The number 786,432 with breakdown 512 × 512 × 3. A second number ~7.8 million for batch of 10. Visual of stacked batch.

**Script:**

> *"Okay, first problem the paper is attacking — bandwidth. Color images are heavy. A single 512-by-512 photo has almost 800 thousand pixel values — height times width times three channels for red, green, and blue. Now think about real use cases — medical scans across hospitals, surveillance cameras, satellite frames. You're never sending one image, you're sending dozens. Each one eats bandwidth. Transmission is slow before you even worry about security."*

**Stage direction:** Use your hand to gesture "stacking" when you say "you're never sending one image."

---

## Slide 4 — The wire is not safe (≈ 0:40)

**On-screen:** SENDER → wire → RECEIVER with an ATTACKER tapping the middle. Bottom strip: *"Slow AND unsafe — the paper attacks both at once."*

**Script:**

> *"Second problem — the wire is not safe. Once an image leaves your device, anyone tapping the connection can read it. Medical, financial, surveillance — that's unacceptable. Encryption fixes it, but historically encryption is treated as a SECOND step AFTER compression. So you pay two costs separately, repeated for every image. The paper's argument is — this is wasteful. Compression and encryption should be ONE pipeline, on the whole batch at once."*

**Stage direction:** This is the setup for the novelty. Lean into *"this is wasteful."*

---

## Slide 5 — Two tools, both from class (≈ 0:25)

**On-screen:** Two boxes side by side. Left: "Tool A — Discrete Wavelet Transform (DWT)." Right: "Tool B — Chaotic Pseudo-Random Map."

**Script:**

> *"To do compression and encryption together, the paper uses two tools we've already touched in class. First is the Discrete Wavelet Transform — DWT — which we used for image processing. Second is a chaotic map — a fancy term for a deterministic function that LOOKS random. The next three slides explain each tool, because once you understand them, the rest is just plumbing."*

**Stage direction:** Quick transition slide. Don't dwell.

---

## Slide 6 — DWT splits an image into 4 sub-bands (≈ 0:50)

**On-screen:** Four sub-bands as a 2×2 grid: LL (top-left, highlighted), LH (top-right), HL (bottom-left), HH (bottom-right).

**Script:**

> *"So DWT first. In lecture we saw Fourier and the cosine transform — both break a signal into frequency components. DWT does the same thing, except wavelets are LOCAL — they catch features in a specific region, not the whole image at once. When you apply DWT to an image, it returns four sub-bands — LL, LH, HL, and HH. LL is a smaller, blurrier version of the image — the low frequencies. LH, HL, HH carry edge details — horizontal, vertical, diagonal. That's all DWT does — split into four."*

**Stage direction:** Point at LL on the slide when you say "smaller blurrier version."

---

## Slide 7 — Keep LL, throw the rest, image is 1/4 size (≈ 0:50)

**On-screen:** Left: explanation paragraph. Right: original image (h × w × 3) → red arrow down → smaller square (h/2 × w/2 × 3, "1/4 size").

**Script:**

> *"And here's the actual compression trick. The paper just keeps LL and throws LH, HL, HH away. That alone shrinks the image to one quarter the original size, because LL has half the height and half the width. Why is that okay? Because most of what your EYE perceives in an image lives in the low frequencies — the broad shapes and colors. The detail bands matter a little, but you can lose them and the image still looks essentially the same. So it's lossy, but acceptable — and the results section proves quality is high enough."*

**Stage direction:** *"One quarter"* is a key phrase. Slow down on it.

---

## Slide 8 — Chaos: deterministic, but looks random (≈ 0:50)

**On-screen:** Left: explanation. Right: chaotic trajectory visual. Below: parameters (a, b, c, d, e, f) = (0.3, 0.94, 0.9, 1.6, -1.8, -1.8).

**Script:**

> *"Now the second tool — a chaotic map. Imagine a function that takes three numbers in, spits three new numbers out, and you feed those back in, get new ones, on and on. The output LOOKS completely random — no pattern, no period. BUT it's deterministic — same starting numbers, same sequence, every time. The trick is — those starting numbers become your secret key. The receiver knows the key and reproduces the exact sequence to decrypt. An attacker without the key sees noise. Maria, take it from here."*

**Stage direction:**
- Pause briefly after *"every time."* That's the key insight landing.
- **The handoff line — "Maria, take it from here" — must be CRISP and confident.** Then take ONE step back. Maria steps forward to center. Practice this transition.

---

## Timing summary

| Slide | Target | What it covers |
|---|---|---|
| 1 | 0:25 | Title + intros |
| 2 | 0:30 | The paper in one breath |
| 3 | 0:35 | Bandwidth problem |
| 4 | 0:40 | Security problem |
| 5 | 0:25 | Two tools preview |
| 6 | 0:50 | DWT splits into 4 sub-bands |
| 7 | 0:50 | Keep LL, throw the rest |
| 8 | 0:50 | Chaos + handoff |
| **Total** | **5:05** | (lands at 5:00 in practice — nerves speed you up) |

---

## If you're running long (>5:30 by slide 8)

Drop these sentences live:

- **Slide 3:** drop *"You're never sending one image, you're sending dozens. Each one eats bandwidth."* Replace with *"Batches of images get heavy fast."*
- **Slide 4:** drop *"Medical, financial, surveillance — that's unacceptable."* Just say *"Anyone tapping the wire can read your images."*
- **Slide 6:** drop the comparison to Fourier and the cosine transform. Say *"DWT splits an image into four sub-bands using localized wavelets."*

## If you're running short (<4:30 by slide 8)

**Slow down.** Don't add content. Take a breath between slides. Silence reads as confidence. Pause for 2 seconds after the handoff line to give Maria a clean entrance.

---

## What to memorize 100%

You don't need to memorize the whole script — speaker notes are fine. But these three moments need eye contact, no script:

1. **Slide 1 opening:** *"Hi everyone, I'm Abdul, and this is Maria."* (Sets the tone.)
2. **Slide 2 anchor line:** *"If you remember nothing else from the next 10 minutes — remember that."* (After the one-sentence thesis.)
3. **Slide 8 handoff:** *"Maria, take it from here."* (The professional pair moment.)

---

## What to expect in Q&A for your half

You'll likely get questions on:
- *"Why DWT and not DCT?"* → "DWT preserves edges better because wavelets are localized in both space and frequency."
- *"What's a chaotic map?"* → "An iterated function that produces random-looking sequences from a starting state. Same key, same sequence — every time."
- *"How does the cube handle different-size images?"* → "Cube dimensions come from the largest image; smaller ones get zero-padded."
- *"What's the novelty?"* → (You haven't said it yet — this is Maria's territory in slide 9. Either let her field it, or briefly bridge: *"Maria covers that in detail on the next slide."*)

See [`_reference/Q&A and Rehearsal.md`](../_reference/Q%26A%20and%20Rehearsal.md) for the full Q&A prep.

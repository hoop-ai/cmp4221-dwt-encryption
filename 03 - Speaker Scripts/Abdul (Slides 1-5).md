---
sticker: emoji//1f399
tags:
  - speaker
  - script
  - abdul
  - presentation
---
# Speaker Script — Abdul (Slides 1–5, ~5:00)

> **Word-for-word script.** Read out loud while timing yourself. Each slide has its own target time. **Total target: 5:00.**
> Cadence target: ~150 words per minute (calm, not rushed).
> When nervous, you'll naturally speed up to ~170 wpm — that lands you at ~4:30, which is fine.

> **The handoff line at the end of slide 5 is the most important sentence in your half.** Practice it until it's automatic: *"Maria, over to you."* Then physically take one step back as Maria steps forward.

---

## Slide 1 — Title (≈ 0:35)

**On-screen:** Title of paper, authors, journal, your names.

**Script:**

> *"Hi everyone. I'm Abdul Rahman, and this is Maria. For our final project, we picked a 2026 paper from ACM Transactions on Multimedia, by Xu, Gao, Cao and Mou. The title is Multi-Image Encryption Scheme Based on Chaotic Pseudo-Random Signal Generator and DWT Compression. The idea is simple to state in one breath — take several color images, shrink them using the wavelet transform we covered in class, and then scramble them all at once using chaos. I'll cover the first five slides — motivation, background, novelty, and the pipeline — and Maria will take the algorithm details, the results, and the security analysis."*

**Stage direction:** Stand at slight angle to the screen. Calm, friendly tone. Don't rush — first impression sets the pace for the rest of the talk.

---

## Slide 2 — The Problem (≈ 1:00)

**On-screen:** "Bandwidth: heavy. Confidentiality: unsafe. Scale: most schemes do one image at a time."

**Script:**

> *"Think about what happens when you send a photo over the internet. A 512 by 512 color image has about 786 thousand pixels across the R, G, and B channels. Multiply that by ten images, and you're moving a lot of data, and any of it can be intercepted. So the paper says there are really two problems happening at the same time. First — transmission is heavy. Second — transmission is unsafe. Most existing schemes handle one image at a time, which is fine for one selfie, but breaks down when you want to send a whole batch, like medical scans or surveillance frames. The authors point out that you need both compression and encryption working together. Otherwise you're just bolting one on top of the other and paying the cost twice. Their goal is to do both in one shot — on multiple images, of different sizes."*

**Stage direction:** Lean into the words "two problems" — that's the setup for the whole talk.

---

## Slide 3 — Two Ingredients (≈ 1:10)

**On-screen:** "DWT → 4 sub-bands → keep only LL → 1/4 size. Chaotic map → deterministic random-looking sequences. Key = starting values."

**Script:**

> *"Okay, so the first ingredient is the Discrete Wavelet Transform — the DWT. We saw this idea in lecture: instead of using sines and cosines like the Fourier transform, you use little localized waves called wavelets, and you split the image into four sub-bands. There's LL, which is the low-frequency approximation — basically a smaller, blurry version of the image. Then there's LH, HL, and HH, which capture horizontal, vertical, and diagonal edges. The trick the paper uses is — they keep only the LL sub-band and throw the rest away. That immediately compresses the image to one quarter of its original size, because LL has half the height and half the width. Now the second ingredient is a three-dimensional discrete chaotic map. A chaotic map is just a function you iterate — you plug in x, y, z, you get new x, y, z, and you keep going. The output looks random, but it's fully deterministic if you know the starting values. Tiny change in those numbers — completely different sequence. That sensitivity is what makes it useful as a key."*

**Stage direction:** When you say "DWT" and "chaotic map" for the first time, slow down slightly. These are the two terms the audience needs to absorb. Look at the audience, not the screen.

---

## Slide 4 — Novelty (≈ 1:00)

**On-screen:** "Encrypt the cube, not the images. DWT-compress every image. Stack all LL sub-bands into one 3D cube. Encrypt the cube once. Handles different sizes via zero-padding."

**Script:**

> *"Here's the core trick — the novelty. Instead of encrypting each image one by one, they DWT-compress every image down to its LL sub-band, and then they stack all those LL sub-bands on top of each other into a single three-dimensional cube. Then they encrypt the whole cube as one object. That's the novelty. One encryption pass, multiple images at once, even when those images have different sizes. They handle the size mismatch by padding with zeros — that's an honest limitation we'll come back to at the end."*

**Stage direction:** This is the *novelty* slide, and the prof grades on novelty being clearly identified. **Pause briefly after "That's the novelty."** Let it land. The whole rest of the talk hangs on this slide.

---

## Slide 5 — Pipeline + Handoff (≈ 1:15)

**On-screen:** "Stage 1: DWT compression. Stage 2: stack cube C. Stage 3: confusion (positions). Stage 4: diffusion (values). Output: cipher cube D."

**Script:**

> *"Let me walk you through this end to end. Stage one — you take each color image, you split it into R, G, B channels, and you run the DWT on each channel. You keep only the LL sub-band; that's where the compression comes from — you're now at one quarter the size. Stage two — you take all those LL sub-bands from all your images, and you stack them into a single three-dimensional cube called C. The width and height come from the biggest image in the batch, and the depth comes from how many images you have. Stage three is what they call confusion. The chaotic map gets iterated to produce three sequences — S1, T1, U1 — and these tell you how to swap pixel positions inside the cube. Stage four is diffusion. Here you don't just move pixels — you change their values, by XOR-ing each pixel with another chaotic sequence. After that, you have the cipher cube D, and that's what gets transmitted."*

> *"Maria, over to you."*

**Stage direction:**
- When you say "Stage one," "Stage two," etc., use your hand to count off on your fingers — visual emphasis.
- The handoff line **"Maria, over to you"** must be CRISP. Calm voice. Then *take one step back* as Maria steps forward to center. Don't fumble the clicker — practice the pass.

---

## Timing summary

| Slide | Target | What it covers |
|---|---|---|
| 1 | 0:35 | Title, paper, group |
| 2 | 1:00 | The problem (bandwidth + safety) |
| 3 | 1:10 | DWT + chaotic map |
| 4 | 1:00 | **Novelty** |
| 5 | 1:15 | Methodology overview + handoff |
| **Total** | **5:00** | |

---

## If you're running long (>5:30 by slide 5)

Drop these sentences in real-time:

- **Slide 2:** drop *"A 512 by 512 color image has about 786 thousand pixels across the R, G, and B channels. Multiply that by ten images, and you're moving a lot of data, and any of it can be intercepted."* Replace with *"Color images are big, and they're not safe in transit."*
- **Slide 3:** drop the explanation of LH, HL, HH. Say *"DWT splits the image into four sub-bands — LL holds the approximation, the other three hold edges. The paper keeps only LL — instant 1/4 compression."*
- **Slide 5:** drop the explanation of cube width/height/depth. Say *"Stage two — stack the LL sub-bands into a cube C."*

---

## If you're running short (<4:30 by slide 5)

Slow down. Don't add content — silence is fine, the audience needs time to process. Pause after each slide's main idea. Take a breath before the handoff.

---

## What to memorize 100%

You don't need to memorize the whole script — you can read most of it from speaker notes. But these **three** moments must be 100% memorized so you can deliver them while making eye contact:

1. **Slide 1 opening line:** *"Hi everyone. I'm Abdul Rahman, and this is Maria."* (Set the tone.)
2. **Slide 4 novelty:** *"That's the novelty — one encryption pass, multiple images at once, even when those images have different sizes."* (This is what the prof grades.)
3. **Slide 5 handoff:** *"Maria, over to you."* (Smooth handoff = professional pair.)

---

## What to expect in Q&A for your half

You'll likely get questions on:
- *Why DWT and not DCT?* → "DWT preserves edges better because it's localized in both space and frequency."
- *What's a chaotic map?* → "An iterated function that produces random-looking sequences from a starting state."
- *How does the cube work for different-size images?* → "Cube dimensions are set by the largest image; smaller ones get zero-padded."

See [`06 - Q&A and Rehearsal.md`](../06%20-%20Q%26A%20and%20Rehearsal.md) for the full Q&A prep.

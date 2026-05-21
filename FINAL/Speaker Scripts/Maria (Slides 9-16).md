---
sticker: emoji//1f399
tags:
  - speaker
  - script
  - maria
  - presentation
---
# Speaker Script — Maria (Slides 9–16, ~5:00)

> **Word-for-word script.** Matches the 16-slide deck.
> Read out loud while timing yourself. Each slide has a target time.
> **Total target: 5:00.** Cadence: ~150 wpm.

> **Your opening line is critical.** Abdul hands off with *"Maria, take it from here."* You respond with *"Thanks Abdul."* and step forward. **Don't skip the thanks** — it anchors the handoff visually and verbally.

---

## Slide 9 — Novelty: encrypt the cube, not the images (≈ 0:50) ★

**On-screen:** Two columns. Left (grey): OLD WAY — one image at a time. Right (red-bordered): NEW WAY — whole batch at once. "ONE PIPELINE. ONE PASS." stamp.

**Script:**

> *"Thanks Abdul. So here's the actual novelty — the one slide to remember. The OLD WAY is — encrypt each image one at a time. Ten photos means running encryption ten times. Compression and encryption are two separate steps. The NEW WAY this paper proposes is — shrink every image first with DWT, stack them all into a single 3D block they call a cube, and run encryption ONCE on the whole cube. Encryption happens once instead of ten times. Compression happens first, so the cube is already small. That's the contribution."*

**Stage direction:**
- **This is THE slide.** The professor grades you on novelty. Slow down. Make eye contact.
- Pause for 1 second after *"That's the contribution."* Let it land.

---

## Slide 10 — The pipeline at a glance (≈ 0:35)

**On-screen:** Four numbered columns: 01 DWT compress, 02 Stack cube C, 03 Confusion, 04 Diffusion. Arrows between. Bottom strip: "OUTPUT — Cipher cube D."

**Script:**

> *"So how does this flow end to end — four stages, in order. Stage one — compress each image with DWT. Stage two — stack the compressed images into the cube C. Those two are the setup. Stage three — confusion, which scrambles pixel POSITIONS. Stage four — diffusion, which changes pixel VALUES. End result is the cipher cube D, transmitted across the network. The receiver runs all four in reverse to recover the originals. Let's walk through each stage."*

**Stage direction:** Use your fingers to count off the four stages — visual emphasis helps the audience follow.

---

## Slide 11 — Stages 1 + 2: Compress and stack (≈ 0:35)

**On-screen:** Left: pseudocode. Right: N color images → DWT → Cube C.

**Script:**

> *"Stages one and two — the setup. Stage one — for each color image, split it into red, green, blue channels, run DWT on each channel, keep only LL. Every image is now a quarter of its original size. Stage two — take all those LL blocks and stack them into a 3D cube. Width and height come from the BIGGEST image divided by two. Depth is the number of images. Smaller images get padded with zeros. Setup done."*

**Stage direction:** Brisk pace. This slide is mechanical — keep it moving.

---

## Slide 12 — Confusion: scramble pixel POSITIONS (≈ 0:40)

**On-screen:** Definition strip. Left: Scrabble analogy + algorithm. Right: BEFORE/AFTER pixel grids.

**Script:**

> *"Stage three — confusion. In cryptography, confusion means — change WHERE the information is, but not WHAT it is. Think of it like shuffling Scrabble tiles on a board — same letters, but the sentence is now nonsense. How does it work? The chaotic map produces three integer offsets per cube pixel. Then for every pixel, the algorithm compares its position to those offsets, and swaps it with another pixel based on the comparison. Nine swap cases total. After running for every pixel, you have the confusion cube C-prime — same values, scrambled positions."*

**Stage direction:** Stress *"WHERE the information is, but not WHAT it is."* That's the definition the audience needs to grasp.

---

## Slide 13 — Diffusion: flip pixel VALUES, chain to previous (≈ 0:50)

**On-screen:** Definition strip. Hero formula: **D[k] = V[k] ⊕ chaos[k mod 3] ⊕ D[k−1]**. Symbol legend. Note: "WHY THE CHAIN MATTERS — avalanche effect."

**Script:**

> *"Stage four — diffusion. Diffusion changes pixel VALUES, not positions. First, flatten the cube into a 1D vector. Then iterate chaos again to get three new streams. For each pixel, the algorithm picks one stream based on index mod 3, and XORs the pixel with that chaos value. The critical part — each output pixel ALSO XORs with the PREVIOUS output. That makes encryption a chain — flip one bit at the start and EVERY later pixel breaks. Reshape the vector back into a cube and you have the cipher cube D."*

**Stage direction:**
- Stress *"chain"* and *"avalanche."* This is the security source.
- Point at the formula on screen when you say *"each output XORs with the previous output."*

---

## Slide 14 — PSNR 32.06 dB · past the visual threshold (≈ 0:45)

**On-screen:** Top: PSNR definition. Left hero number: 32.06 dB. Right: bar chart — this paper (red, longest) vs four prior schemes (black, shorter), with vertical 30 dB threshold marker.

**Script:**

> *"Okay — does it actually work? Reconstruction quality is measured with PSNR — peak signal-to-noise ratio, in decibels. Quick rule — anything around 30 dB is visually good. The recovered image looks essentially the same as the original. This paper hits 32.06 dB on average — PAST the threshold — even after lossy DWT compression PLUS full encrypt-and-decrypt. The four prior schemes they benchmark against land between 26.3 and 27.7 dB — BELOW the threshold. So this paper is the difference between looks-the-same and looks-degraded."*

**Stage direction:** *"32.06"* — say it cleanly. Not "thirty-two point zero six oh one" — that's robotic. Say "thirty-two point oh six."

---

## Slide 15 — Security: four checks, all pass (≈ 0:50)

**On-screen:** Table — NIST randomness, NPCR, UACI, Entropy, Key space. Each with check name, what it tests, paper's result, PASS stamp.

**Script:**

> *"Now security — four checks, all pass. One — the chaotic sequence goes through the NIST randomness battery, 15 statistical tests. Every one passes. Two — differential attack. Flip one pixel of the input, measure how much the cipher changes. NPCR target is 99.6094, paper hits 99.65. UACI target is 33.46, paper hits 33.49. Dead on the ideals. Three — information entropy of the cipher is 7.9994 out of a max of 8. Indistinguishable from uniform noise. Four — key space is enormous, way beyond brute force. Statistical attacks, differential attacks, brute force — all blocked."*

**Stage direction:** Number the four checks with your fingers. Helps the audience follow. Don't rush — these numbers are the proof.

---

## Slide 16 — Limitation, take-home, questions (≈ 0:35)

**On-screen:** Three hero numbers at top: 32 dB, 7.9994, 99.65 %. LIMITATION + TAKE-HOME paragraphs. Big "Questions?" at bottom.

**Script:**

> *"One honest limitation — the authors flag it themselves. When images in a batch have different sizes, the cube has to be padded with zeros, which wastes space. They mark it as future work. Take-home in one breath — by combining DWT with a 3D chaotic map, you get encryption AND compression in one pipeline, for a whole batch of images, with reconstruction past the visual threshold and security all green. Thanks for listening — we're happy to take questions."*

**Stage direction:**
- Brief pause before *"Take-home in one breath."*
- Smile after *"Thanks for listening."* Take half a step back — relaxed posture signals you're ready for Q&A.

---

## Timing summary

| Slide | Target | What it covers |
|---|---|---|
| 9 | 0:50 | **Novelty** — encrypt the cube |
| 10 | 0:35 | Pipeline overview |
| 11 | 0:35 | Compress + stack |
| 12 | 0:40 | Confusion |
| 13 | 0:50 | Diffusion + chain |
| 14 | 0:45 | **Findings — PSNR** |
| 15 | 0:50 | **Findings — Security** |
| 16 | 0:35 | Limitation + take-home + Q&A handoff |
| **Total** | **5:00** | |

---

## If Abdul handed off late (>5:30 used by slide 9)

You have less than 5 minutes. Compress like this:

- **Slide 9 (novelty):** keep all of it. **DO NOT TRIM NOVELTY.** This is the graded slide.
- **Slide 11:** drop *"Width and height come from the BIGGEST image divided by two."* Just say *"Stack into a cube, pad smaller images with zeros."*
- **Slide 12:** drop *"Nine swap cases total."* Just say *"chaos-driven position swaps."*
- **Slide 13:** drop *"Then iterate chaos again to get three new streams."* Just say *"XOR each pixel with chaos AND with the previous output — that's the chain."*
- **Slide 15:** drop *"NPCR target is 99.6094, paper hits 99.65. UACI target is 33.46, paper hits 33.49."* Just say *"NPCR and UACI hit their ideal targets — both right on the marks."*

## If you're running short (<4:30 used)

Slow down. Pause for 1-2 seconds at slide transitions. Take a small breath before each new slide. **Silence reads as confidence.** Don't try to add content — just deliver the same script more deliberately.

---

## What to memorize 100%

Three moments need to be off-script with eye contact:

1. **Slide 9 opening:** *"Thanks Abdul. So here's the actual novelty — the one slide to remember."* (Anchors the handoff + cues the novelty.)
2. **Slide 14 headline number:** *"32.06 dB on average — past the visual threshold, even after the full round trip."* (The headline finding.)
3. **Slide 16 close:** *"Thanks for listening — we're happy to take questions."* (The handover to Q&A.)

---

## What to expect in Q&A for your half

You'll likely get questions on:
- *"Why XOR for diffusion?"* → "Self-inverse, bit-level, one CPU instruction."
- *"What is NPCR?"* → "Number of Pixel Change Rate — how many cipher pixels differ after a 1-pixel plaintext flip. Ideal 99.61%, paper hits 99.65."
- *"What's information entropy?"* → "How uniformly distributed the cipher's pixel values are. Max is 8 for 8-bit; paper hits 7.9994."
- *"How big is the key space?"* → "At least 2¹⁰⁰, with the actual composite key larger because of plaintext-derived parameters."
- *"Why three streams cycled by mod 3?"* → "More keystream variety — an attacker who somehow figured out one stream still wouldn't know what's happening at the other 2/3 of pixels."

See [`_reference/Q&A and Rehearsal.md`](../_reference/Q%26A%20and%20Rehearsal.md) for the full Q&A prep with 20 anticipated questions.

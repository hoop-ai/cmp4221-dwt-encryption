---
sticker: emoji//1f399
tags:
  - speaker
  - script
  - maria
  - presentation
---
# Speaker Script — Maria (Slides 6–10, ~5:00)

> **Word-for-word script.** Read out loud while timing yourself. Each slide has its own target time. **Total target: 5:00.**
> Cadence target: ~150 words per minute (calm, not rushed).
> When nervous, you'll naturally speed up — aim to take a small breath between each slide transition.

> **The opening line is your most important sentence.** Abdul hands off with *"Maria, over to you."* — you respond with *"Thanks, Abdul."* and step forward. **Don't skip the thank you.** It anchors the handoff visually and verbally.

---

## Slide 6 — Confusion (≈ 1:10)

**On-screen:** "Confusion = scramble positions. Iterate chaos → S1, T1, U1 offsets. 9 swap cases. Pixel values unchanged."

**Script:**

> *"Thanks, Abdul. So I'll start with confusion. Confusion in cryptography just means changing where things are, not what they are. The pixel values stay the same — only their positions move. The way they do it is, they iterate the chaotic map once for every pixel in the cube. From those iterations, they get three sequences — X, Y, Z — and they post-process them with mod and floor operations to land on integers in the right range. Those become S1, T1, U1 — the three coordinate offsets. Then for every single pixel at position i, j, k, they compare each coordinate with its offset. There are nine possible swap cases. After running this for every pixel, you get the confusion cube C-prime. The nice thing is — the offsets depend on the plaintext itself, which makes the scheme plaintext-aware. The clean definition is — confusion hides the location of information. The pixel values can be the same, but they no longer sit in meaningful image positions."*

**Stage direction:** Speak slowly when you say "confusion hides the location of information." That's the take-home from this slide.

---

## Slide 7 — Diffusion (≈ 1:10)

**On-screen:** "Diffusion = change values. Flatten cube to 1D vector. First pixel XOR with seed. Each next: XOR with chaos AND previous output. Chains the avalanche."

**Script:**

> *"Diffusion changes the actual pixel values, not just their positions. The way they do it — first, they flatten the confusion cube into a one-dimensional vector V. Then they iterate the chaotic map again, this time getting sequences X2, Y2, Z2. For the very first pixel of V, they XOR it with a seed derived from the chaotic sequence. Then for every pixel after that, they take the index mod 3. Each result picks a different chaotic sequence to XOR with — so you're not just using one stream, you're cycling through three. And critically — the diffusion uses the previous pixel as part of the input. That means a single bit change at the start cascades through the rest of the encrypted data. After the loop, they reshape the vector back into the cipher cube D. This is stronger than a simple one-time XOR because the previous output links the whole vector together, so the effect spreads instead of staying local."*

**Stage direction:** Stress the word "cascades" — that's the key concept (avalanche effect). The audience needs to feel that this is the moment encryption becomes strong.

---

## Slide 8 — Findings (≈ 1:00)

**On-screen:** "PSNR 32.06 dB. Prior work 26-27 dB. Compression 1/4. Encryption speed 6.15 MB/s."

**Script:**

> *"Now the findings. Reconstruction quality is measured with PSNR — peak signal-to-noise ratio, in decibels. Anything around 30 dB is considered visually good. The paper reports 32.06 dB on average, and that's after lossy DWT compression and a full encrypt-decrypt round trip. Compare that to four prior schemes they benchmarked against — those land between 26.3 and 27.7 dB. So this paper's reconstruction is roughly 4 to 6 dB better, which on the PSNR scale is a meaningful jump because the scale is logarithmic. On the speed side, total encryption runs at about 6.15 megabytes per second on their setup. So the scheme is not just secure on paper — the recovered image is actually clean. That matters because quality is preserved, not merely decrypted."*

**Stage direction:** This is the *findings* slide — the prof grades on findings being clearly identified. Round numbers as you speak them: say "thirty-two point oh-six" not "thirty-two point zero six zero one." Sounds natural, not robotic.

---

## Slide 9 — Security Analysis (≈ 1:00)

**On-screen:** "NIST: 15/15 pass. NPCR: 99.65% (target 99.61%). UACI: 33.49% (target 33.46%). Entropy: 7.9994 / 8."

**Script:**

> *"Four security checks — all passed. First, the chaotic sequence itself goes through the NIST randomness suite — fifteen statistical tests, and every single one passes. Second, differential attack analysis. They flip one pixel of the input and re-encrypt, then measure NPCR and UACI. The standards are 99.6094 percent and 33.4635 percent. They hit 99.65 percent and 33.49 percent on average across twelve test images — so right on the ideal numbers. Third, information entropy of the cipher image is 7.9994, where the theoretical maximum is exactly 8. And fourth — the key space is way beyond brute force. So statistical attacks, differential attacks, and brute force are all blocked."*

**Stage direction:** Number the four checks with your fingers as you go. The audience can follow more easily with the visual count.

---

## Slide 10 — Limitation + Take-Home (≈ 0:40)

**On-screen:** "Limitation: zero-padding wastes space. Take-home: DWT + chaos = compression + encryption in one pipeline. PSNR 32 dB, IE 7.9994, NPCR 99.65%."

**Script:**

> *"One honest limitation — when the images in the batch are different sizes, the cube has to be padded with zeros, which wastes space. The authors flag this as future work. The take-home is this — by combining DWT compression with a 3D chaotic map, you get encryption and compression in a single pass, with reconstruction quality of 32 dB and entropy basically equal to perfect noise. One pipeline, multiple images, strong security. Thanks for listening. We're happy to take questions."*

**Stage direction:**
- Pause briefly before "The take-home is this" — signals the audience to focus on the summary.
- After "Thanks for listening" — small smile, take a slight step back. Standing slightly relaxed signals readiness for Q&A.

---

## Timing summary

| Slide | Target | What it covers |
|---|---|---|
| 6 | 1:10 | Confusion |
| 7 | 1:10 | Diffusion |
| 8 | 1:00 | **Findings (PSNR)** |
| 9 | 1:00 | **Findings (security)** |
| 10 | 0:40 | Limitation + take-home + close |
| **Total** | **5:00** | |

---

## If you're running long (Abdul handed off late)

If Abdul finishes at 5:30+, you have less time. Compress like this:

- **Slide 6:** drop *"They iterate the chaotic map once for every pixel in the cube. From those iterations, they get three sequences — X, Y, Z — and they post-process them with mod and floor operations."* Replace with *"They iterate the chaotic map to get offset sequences S1, T1, U1."*
- **Slide 7:** drop *"so you're not just using one stream, you're cycling through three."* You're cycling sequences but the audience doesn't need to know.
- **Slide 9:** drop the explanation of NPCR/UACI standards. Say *"NPCR and UACI hit their ideal targets. Entropy 7.9994. NIST all-pass."*

---

## If you're running short

Pause more between sentences. Don't add content. Take the same 1-minute slide and give it 1:15. Silence is calm. The audience perceives it as confidence.

---

## What to memorize 100%

Three moments need to be off-the-cuff with eye contact:

1. **Slide 6 opening:** *"Thanks, Abdul. So I'll start with confusion. Confusion in cryptography just means changing where things are, not what they are."* (Anchors the handoff.)
2. **Slide 8 headline number:** *"32.06 dB on average — that's after lossy DWT compression and a full encrypt-decrypt round trip."* (The headline finding.)
3. **Slide 10 close:** *"One pipeline, multiple images, strong security. Thanks for listening. We're happy to take questions."* (The handover to Q&A.)

---

## What to expect in Q&A for your half

You'll likely get questions on:
- *Why XOR for diffusion?* → "Self-inverse, bit-level, fast."
- *What is NPCR exactly?* → "Number of pixel change rate — how many cipher pixels differ after a 1-pixel plaintext flip. Should be 99.61%."
- *What's information entropy?* → "How uniformly distributed the cipher's pixel values are. Max is 8 for 8-bit; cipher hits 7.9994."
- *How big is the key space?* → "At least 2¹⁰⁰, with the actual composite key larger because of plaintext-derived parameters."

See [`06 - Q&A and Rehearsal.md`](../06%20-%20Q%26A%20and%20Rehearsal.md) for the full Q&A prep.

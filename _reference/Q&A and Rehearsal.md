---
sticker: emoji//1f4ac
tags:
  - course
  - multimedia
  - project
  - q-and-a
  - rehearsal
---
# Q&A Prep + Rehearsal Guide — DWT Encryption Presentation

> Companion to [[07 - Slide Deck Source]] and [[Paper - Verbatim]] in [`04 - The Paper/`](04%20-%20The%20Paper/).
> Group: Abdul Rahman Malak (2285310) + Maria Alftaih (2285921). Course: CMP4221, Asst. Prof. Dr. Selin Nacakli. Talk length: 10 minutes + Q&A.
> Word-for-word speaker scripts live in [`03 - Speaker Scripts/`](03%20-%20Speaker%20Scripts/) (Abdul slides 1-5, Maria slides 6-10).

> [!tip] How to use this file in the Q&A
> Glance at the question, find the matching block, read the script. Don't improvise off-script for the red ones — the script is calibrated to admit limits without losing face. Cite the paper section out loud; instructors love that.

---

## Q&A Prep — likely audience questions

Difficulty key: 🟢 easy · 🟡 medium · 🔴 hard
Speaker key: **A** = Abdul, **M** = Maria, **E** = either

---

### Definitions (5 questions)

#### Q1. 🟢 A · "What is a chaotic map, in plain words?"
**Source:** Section 2, "Chaotic Map." Paper line: *"Chaotic map has been widely used in the image encryption by virtue of their high nonlinear and sensitivity to initial conditions."*

> "A chaotic map is just a function you keep applying to a number, over and over. Each step uses the previous output as the next input. The output looks random, but it's fully deterministic — same starting numbers, same sequence every time. The reason we use it for encryption is sensitivity: change the starting value by ten to the minus fifteen, and after a few iterations the sequence is completely different. That sensitivity is what makes the starting values a usable secret key."

#### Q2. 🟢 E · "What does DWT actually do to an image?"
**Source:** Section 4.1.1, Fig. 5.

> "DWT, the Discrete Wavelet Transform, splits an image into four sub-bands: LL, LH, HL, HH. LL is the low-frequency part — basically a smaller, blurry version of the image at half the height and half the width. The other three hold horizontal, vertical, and diagonal edges. The paper keeps only LL and throws the rest away. That's how the image shrinks to one quarter of its original size."

#### Q3. 🟡 M · "What is NPCR and what does the number 99.65% mean?"
**Source:** Section 6.1.2 and 6.2.1, Equation 17, Tables 5 and 6.

> "NPCR stands for Number of Pixel Change Rate. You encrypt an image, then change one single pixel of the original and encrypt it again. NPCR counts what percentage of pixels in the two cipher images are different. The ideal target is 99.6094 percent. The paper hits 99.65 percent on average across twelve test images, which means flipping one input pixel changes basically every output pixel. That's exactly what you want — it tells you the encryption has good avalanche behaviour."

#### Q4. 🟡 M · "What is UACI?"
**Source:** Section 6.2.1, Equation 18, Table 5.

> "UACI is Unified Average Changing Intensity. It's the average difference in pixel value between two cipher images, expressed as a percentage of the maximum pixel value. NPCR tells you how many pixels changed; UACI tells you how much they changed on average. The standard target is 33.4635 percent. The paper averages 33.49 percent. So both metrics line up with the ideal."

#### Q5. 🟢 A · "What is information entropy here?"
**Source:** Section 6.3.3, Table 7 and 8.

> "Information entropy measures how unpredictable the pixel distribution is. The theoretical maximum for an 8-bit image is exactly 8, which would mean every pixel value is equally likely. The paper's cipher images hit 7.9994. That's basically pure noise — an attacker looking at the histogram learns nothing about the original."

---

### Methodology mechanics (4 questions)

#### Q6. 🟡 M · "Why XOR for diffusion? Why not addition or multiplication?"
**Source:** Section 4.1.3, Equation 12.

> "Three reasons. First, XOR is its own inverse — XOR-ing twice with the same value gives you back the original, so decryption is the same operation as encryption. Second, it's bit-level, so it spreads the chaotic randomness across every bit of the pixel evenly, not just the high bits. Third, it's fast — one CPU instruction. Addition would also work but you'd have to handle modular wrap-around, and you'd lose the symmetry. The paper picks XOR because it gives perfect mixing at near-zero cost."

#### Q7. 🟡 A · "How exactly is the cube formed when the images are different sizes?"
**Source:** Section 4.1.1, Equation 6.

> "Good question. After DWT, each LL sub-band is half the height and half the width of its original image. The cube takes the largest image's dimensions divided by two as its width and height — so M_h equals h-max over two, M_w equals w-max over two. The depth is the number of images N, plus extra layers if the total pixel count needs more room. Smaller images get zero-padded to fill that volume. That's why the paper admits, in the conclusion, that zero-padding wastes space — that's their main acknowledged limitation."

#### Q8. 🔴 M · "Why iterate the chaotic map 1.25 × 10⁵ times before using it?"
**Source:** Section 3.1, Step 2.

> "It's called the burn-in or warm-up phase. When you start a chaotic map from your initial values, the very first iterations aren't yet on the chaotic attractor — they can be biased or have transient structure. Iterating 125 thousand times pushes the trajectory deep onto the attractor, so by the time you start using values for encryption, the sequence statistically looks like ideal chaos. The paper also uses this same iterated state for the NIST randomness tests in Table 1, which all pass — so empirically 1.25 times ten to the fifth is enough."

#### Q9. 🟡 M · "What are the nine cases in the confusion step?"
**Source:** Section 4.1.2, Equation 10.

> "For each pixel at position (i, j, k), the algorithm compares each coordinate against the offsets S1, T1, U1 from the chaotic sequence. Each comparison has three outcomes — bigger, smaller, or equal. Three coordinates times three outcomes per coordinate gives nine total cases. In the bigger case, you swap with position i plus the offset; in the smaller case, you swap with absolute value of i minus the offset; equal means stay put. Honestly, you don't need to memorise all nine — the takeaway is just that the rule decides which way each pixel slides."

---

### Comparison and critique (3 questions)

#### Q10. 🔴 E · "Is this real cryptographic security or just security through obscurity?"
**Source:** Section 6.1.1 (key space), Section 6 overall.

> "Fair pushback. It's not AES — there's no formal cryptographic proof here. What the paper does provide is empirical security: the chaotic sequence passes all fifteen NIST randomness tests, NPCR and UACI hit the standard targets, the cipher histogram is uniform, and the key space is at least two to the hundredth power, which is well beyond brute force. So it's not obscurity — it has measurable, testable security properties. But you're right that an academic chaos-based scheme would not, today, be deployed instead of AES for, say, banking. Where it shines is when you also need built-in compression and joint multi-image handling, which AES alone doesn't give you."

#### Q11. 🔴 M · "Why not just use AES on the compressed images?"
**Source:** Inferred from Section 1 and Section 4.

> "You absolutely could, and AES is more battle-tested. The paper's argument is that you'd have to compress and encrypt as two separate pipelines, which costs you twice — twice the processing time, twice the implementation complexity. Their scheme couples them: the same chaotic system that scrambles the bits also drives the structure that lets you stack multiple variable-sized images into one cube. AES doesn't naturally extend to that multi-image cube structure. So the question is less 'AES vs chaos' and more 'do you want one integrated pipeline or two stacked ones'. For research-grade transmission of medical or surveillance batches, the integrated approach is interesting."

#### Q12. 🟡 A · "Why DWT and not DCT, like JPEG uses?"
**Source:** Section 1, Section 4.1.1.

> "DCT works in the frequency domain globally — you lose spatial localisation, which is fine for JPEG blocks but limits how well you can recover edges. DWT uses wavelets, which are localised in both space and frequency, so you can analyse local variations better. The paper actually quotes this directly — DWT can better analyse signals with local variations than the Fourier transform. Practically, that translates to higher PSNR after compress-encrypt-decrypt: 32.06 dB versus 26 to 27 dB for prior DCT-based schemes in their Table 2."

---

### Applications and scope (3 questions)

#### Q13. 🟡 E · "Would this work for video?"
**Source:** Beyond paper scope; honest answer.

> "The paper doesn't apply it to video. In principle, you could treat each frame as one of the multiple images and stack them into the cube, which would give you compression and encryption per group of frames. The catch is that video has temporal redundancy that DWT alone doesn't exploit — you'd want something like motion compensation as well, similar to how MPEG works. So short answer: yes, frame by frame, but you'd be leaving compression efficiency on the table. The paper's clear scope is multiple still images of varying sizes, like a medical scan batch."

#### Q14. 🟢 A · "Why these specific test datasets?"
**Source:** Tables 5, 7, 9 — file names like 4.1.01.tiff, 4.2.07.tiff.

> "Those file names — 4.1.01, 4.2.05, and so on — are from the USC-SIPI image database, which is the standard benchmark in image processing and encryption research. Using them lets the authors fairly compare against prior work, because everyone tests on the same images. The 4.1.x ones are 256 by 256, and the 4.2.x ones are 512 by 512, so they cover both small and medium sizes."

#### Q15. 🟡 E · "Who would actually use this?"
**Source:** Section 1 motivation.

> "The paper points to scenarios where you transmit batches of images at once and care about both bandwidth and confidentiality. The clearest fits are medical imaging — sending a patient's scans across hospitals — and surveillance, where multiple camera feeds get archived together. Anywhere you have multiple correlated images, varying sizes, and a need to encrypt and compress in one shot, this scheme is a candidate."

---

### Bonus painful ones (extras for the truly hostile question)

#### Q16. 🔴 A · "How big is the key space exactly?"
**Source:** Section 6.1.1, Table 3.

> "The paper quotes the theoretical lower bound as two to the hundredth power, which they cite as already enough to resist brute force. The actual composite key includes nine chaotic parameters — a, b, c, d, e, f, x0, y0, z0 — plus parameters derived from the plaintext like the cube's pixel sum. With each chaotic parameter precise to about ten to the minus fifteen, you get something well beyond two to the hundredth in practice. The exact total is what they call 'sufficient to defeat any practical brute-force attack,' though they don't pin a single number — they argue it's larger than the schemes in their Table 4."

#### Q17. 🔴 M · "Can you show how the chaotic map equation looks?"
**Source:** Equation 1, Section 2.1. The verbatim paper does NOT include the equation body.

> "Honestly, the equation is given in the paper as Equation 1, but the form we have is just labelled — the body is in the figure of the original PDF that we worked from a transcript of. What we know is that it's a three-variable iterated map, taking x, y, z to new x, y, z, with six tunable parameters a through f. The paper sets those to (0.3, 0.94, 0.9, 1.6, minus 1.8, minus 1.8) and starts at (0.1, 0.1, 0.1). The phase diagrams in Figure 1 confirm the resulting trajectory is chaotic, not periodic, for those values."

#### Q18. 🔴 E · "Have you implemented this?"
**Source:** N/A.

> "No, we haven't implemented it ourselves — this was a paper review, not a re-implementation. We read the paper end to end, traced the algorithm step by step, and checked the reported numbers against the tables. If we had a few more weeks we'd want to reproduce the PSNR and NPCR values in MATLAB or Python to confirm them, but that wasn't in scope for this assignment."

#### Q19. 🟡 M · "What happens if an attacker captures the cipher cube?"
**Source:** Section 6.1.1, 6.2, 6.3.

> "Without the key, they get a noise-like 3D block — uniform histogram, near-zero correlation between adjacent pixels, entropy of 7.9994. The paper tests this directly with all-black and all-white plaintexts, and even then the cipher reveals nothing. So intercepting the cube doesn't help unless the attacker can guess the chaotic parameters and the plaintext-derived parts of the key, which is what the brute-force resistance argument covers."

#### Q20. 🟡 A · "What's the compression ratio compared to JPEG?"
**Source:** Section 5, Table 2.

> "JPEG can give you ratios anywhere from 10 to 1 to over 50 to 1 depending on quality settings. This paper compresses to 1/4, which is a 4 to 1 ratio — much milder. But the trade-off is that JPEG loses information through quantisation of DCT coefficients, while DWT-LL only just downsamples. That's why the recovered PSNR is 32 dB here rather than the typical 25 to 30 dB you'd get from a heavily compressed JPEG. So less compression, but cleaner reconstruction."

---

## Rehearsal Guide

> [!important] The brutal truth
> A 10-minute talk is mostly cadence, not content. You wrote it, you understand it. The risk now is just running long, mumbling the handoff, or freezing on a question. The schedule below is calibrated to fix exactly those three things.

### One week before
- [ ] Both partners read the verbatim paper end-to-end (not just the slides — the slides hide nuance you'll get asked about).
- [ ] Each does a solo timed run of their half. Targets: Abdul ≤ 5:00, Maria ≤ 5:00. If you go over, *cut*, don't speed up.
- [ ] Highlight any slide whose script you can't read at a calm pace inside its budget. Rewrite that one slide's script tonight.
- [ ] Both read this Q&A file once.

### Three days before
- [ ] Joint dress rehearsal #1 with a phone timer in front of you.
- [ ] After the run-through, swap roles: Maria asks Abdul his half's questions cold. Abdul asks Maria hers. Use this Q&A list. No peeking — this rehearses the *reading-aloud* of the script under pressure.
- [ ] Adjust slide content if needed. Rule: cut, don't add. Adding content this close to the date is how you blow the time budget.
- [ ] Confirm the handoff line is rehearsed. Abdul says it; Maria physically steps forward when she hears the words "Maria, over to you."

### Day before
- [ ] Joint dress rehearsal #2 — full run, no edits after this point. If a slide still feels rough, just slow your reading, don't rewrite.
- [ ] Test the slides on the venue's projector, or at least an external monitor at home — fonts and colours can shift.
- [ ] Print this Q&A guide as a backup in case your laptop dies during Q&A.
- [ ] Sleep. Cramming the morning of will hurt you more than it helps.

### Day of
- [ ] Arrive 10 minutes early.
- [ ] Two copies of the deck on you: USB stick + cloud (Drive or OneDrive link bookmarked on phone).
- [ ] Water bottle within reach (anxiety dries the mouth — you will need it).
- [ ] Quick pre-talk run of the handoff cue out loud, even if just whispered. This is the single moment most likely to wobble.
- [ ] Phone on silent, not vibrate. A buzz mid-Q&A breaks concentration.

---

## Stage directions

**Body language**
- Stand at slight angle to the screen, never with your back fully to the audience. Glance at the slide, talk to the room.
- Hands: out of pockets, not crossed. If you don't know what to do with them, hold the pointer / clicker in one and let the other rest.
- Feet planted. No swaying or pacing during your script — pacing reads as nervous. Move only when you swap speakers.

**Eye contact**
- Find three friendly faces in the audience — left, centre, right. Rotate between them every ~10 seconds. Don't lock onto one person; that makes them and you uncomfortable.
- Do NOT stare at the laptop screen the whole time. Glance at it for transitions, then back up.

**Pacing**
- Read each script at a pace that lets you finish each slide in its allocated time. If you finish 10 seconds early, that's fine — pause, breathe, then transition. *Silence is not failure.*
- If you finish 15 seconds late, do NOT speed up the next slide. Cut a sentence instead. The audience won't notice; the timer will.

**Handoff position (slide 5 → slide 6)**
- Abdul, at the start of slide 5, position yourself slightly stage-left of the screen.
- When Abdul says "Maria, over to you," Abdul takes one step back, Maria steps forward to roughly centre. The clicker passes between you in that motion. Practise this at least twice.

**If the timer runs short**
- You're at slide 8 and you have 3 minutes left instead of 2. Slow down. Repeat one key number ("32.06 dB — basically indistinguishable from the original"). Take questions earlier if you finish at 9:00.

**If the timer runs long**
- You're at slide 7 and only 2 minutes are left. On slide 8, drop the speed sentence and just say PSNR is 32 dB versus 27. On slide 9, list the four checks without elaboration. On slide 10, just read the take-home line — skip the limitation if needed.

**Q&A handling**
- If a question is for "the team," whoever is more confident takes it. Default: Abdul handles motivation/pipeline questions; Maria handles math/results/security questions.
- If you don't know an answer, say "That's a good question — the paper doesn't address that directly, but my best guess based on the methodology is..." Honesty beats a fake answer every time, especially with Dr. Nacakli, who'll see through it.
- If the instructor asks something brutally specific, glance at this guide. It's allowed.

---

## Common student mistakes to avoid (specific to this paper)

- **Don't try to derive Equation 10's nine cases on the fly.** Just say "this rule decides which direction each pixel slides — bigger means add the offset, smaller means subtract, equal means stay." If pushed, point to Section 4.1.2 and move on.
- **Don't claim AES is worse.** It's not. The paper's pitch is integrated compression + encryption, not 'better encryption than AES'. Saying AES is weak will get destroyed in Q&A.
- **Don't say the paper proves cryptographic security.** It demonstrates *empirical* security via NIST, NPCR, UACI, IE — those are statistical tests, not formal proofs. The distinction matters and Dr. Nacakli will know it.
- **Don't read 32.0601 dB precisely.** Round to 32 dB or 32.06 dB. Reading four decimal places aloud sounds robotic and wastes time.
- **Don't oversell the key space.** The paper says "at least 2^100." Don't invent a bigger number. If asked, say "at least 2^100, with the actual composite key larger because of plaintext-derived parameters."
- **Don't skip the handoff line.** A clean handoff is what makes a two-person talk look professional. Rehearse it more than any single slide.

---

## One-line summary you can read if everything goes wrong

> "This paper combines DWT compression with a 3D chaotic map to encrypt multiple color images of different sizes in a single cube, achieving 32 dB PSNR reconstruction and entropy of 7.9994 — compression and encryption in one pipeline."

Memorise that. If you blank, that sentence buys you 10 seconds to recover.

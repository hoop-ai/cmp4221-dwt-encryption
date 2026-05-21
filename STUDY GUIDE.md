---
sticker: emoji//1f4d6
tags:
  - course
  - multimedia
  - project
  - study
  - master
---
# STUDY GUIDE — DWT Encryption, slide by slide

> **For when you have no clue and need to learn the paper from scratch.**
> Read this top to bottom with the 16-slide deck open beside you. Each chapter below corresponds to one slide. By the time you finish reading, you'll know what to say, why it matters, and how to handle questions.

---

## Panic-mode summary — 5 minutes of reading

If the presentation is tomorrow and you've read nothing, read just this section.

### The paper in three sentences

The authors want to send a batch of color photos across a network. Sending photos is slow (color images are huge) AND unsafe (anyone tapping the wire can read them). They solved both at once: shrink every image with the wavelet transform, stack the shrunk images into a single 3D block they call a *cube*, and scramble that cube with a chaotic system in one encryption pass. So instead of compressing-and-encrypting each image separately, you do both jobs on the whole batch at once.

### The two tools you need to know

1. **DWT (Discrete Wavelet Transform).** A signal transform. You point it at an image and it gives you back four versions: LL, LH, HL, HH. LL is a smaller blurry version of the image (low frequencies). LH/HL/HH are edge details. The paper keeps LL and throws the rest away. That alone shrinks every image to one quarter of its original size, because LL has half the height and half the width.

2. **3D chaotic map.** A math function that you keep iterating. You put in three numbers (x, y, z), and three new numbers come out. You feed those back in, get new ones, repeat. The output looks completely random but it's deterministic — same starting numbers, same sequence, every time. Those starting numbers are the encryption key.

### The encryption pipeline in one breath

1. Run DWT on each image, keep only LL.
2. Stack all the LL blocks into a 3D cube called C.
3. **Confusion** — use chaos to scramble pixel POSITIONS in the cube.
4. **Diffusion** — use chaos to flip pixel VALUES with XOR, chaining each output to the previous one.
5. The result is the cipher cube D, which is what gets transmitted.

Receiver runs everything in reverse to recover the original images.

### Numbers to memorise (you will be asked)

- **PSNR = 32.06 dB.** Image quality after compression + encryption + decryption. The 30 dB threshold is "looks the same as the original." We are past it. Prior work is below it.
- **NPCR = 99.65 %.** Differential attack test. Ideal target is 99.6094 %. We're dead on.
- **UACI = 33.49 %.** Same test, intensity version. Ideal is 33.4635 %. Dead on.
- **Information entropy = 7.9994 / 8.** The cipher is statistically indistinguishable from random noise.
- **NIST = 15 / 15.** Every randomness test passes.

### The one limitation to admit

When images in the batch have different sizes, the cube has to be padded with zeros. That wastes space. The authors call it future work. **Always admit this in Q&A — don't try to defend it. Honesty about limitations scores points.**

---

## Mental model — the cube idea, as a story

Before we go slide by slide, imagine this scenario. You're a hospital sending 10 patient X-rays to another hospital across the country. Two problems:

1. Each X-ray is huge. Sending 10 at full resolution is slow and expensive.
2. The data is sensitive. You can't let anyone on the network see it.

The standard fix is:
- Compress X-ray 1, encrypt X-ray 1, send X-ray 1.
- Compress X-ray 2, encrypt X-ray 2, send X-ray 2.
- ... 10 times.

This paper does it differently. You:

- Compress every X-ray first (DWT, keep LL).
- Stack the 10 compressed X-rays on top of each other, like a deck of cards. That stack is a 3D block — width, height, depth. The paper calls this the **cube**.
- Encrypt the whole cube as one object using chaos. One pass.
- Send the encrypted cube.
- The receiving hospital, who knows the key, runs the whole thing in reverse and recovers all 10 X-rays.

That's it. That's the paper. **Stack the batch into a cube, encrypt the cube.** Everything else is just the details of how the encryption inside the cube works.

---

## Slide 1 — Title

### What's on screen
The paper's title, the authors (Xu, Gao, Cao, Mou), the journal (ACM TOMM, March 2026), the DOI, your names.

### What to say
"Hi everyone, I'm Abdul, and this is Maria. We picked a paper from this March's ACM Transactions on Multimedia, by Xu, Gao, Cao, and Mou. The paper is about encrypting multiple color images at once, using two ideas we've already met in class. I'll do the first half — the problem, the tools, and what's actually new. Maria will take the algorithm details and the results."

### Why this matters
You're satisfying the grading criteria right here: it's a 2026 paper, in one of the two journals the professor required (ACM TOMM or IEEE TMM), and you've shown the title, authors, venue and DOI. **The professor explicitly checks this.**

### If you blank
Just say the title and your names. Move on.

---

## Slide 2 — The paper in one breath

### What's on screen
The one-sentence thesis: *"Take a batch of color images. Shrink each one with the wavelet transform. Stack the shrunken images into one cube. Scramble the cube with chaos."* Plus a small visual showing batch → cube → cipher.

### What to know
This is the slide that anchors the entire talk. It's the elevator pitch. Everything else is a detail under this umbrella.

### What to say
"Before we get into the details, here's the entire paper in one breath. The authors take a batch of color photos, shrink them all with the wavelet transform, stack the shrunken images into a single 3D block they call a cube, and then scramble the whole cube using a chaotic system. So in one pipeline, you get compression AND encryption, AND it works on a whole batch instead of one image at a time. If you remember nothing else from the next ten minutes, remember that one sentence."

### Common audience confusion
- **"What's a cube?"** A 3D block of numbers. Width × Height × Depth. The width and height come from each image's dimensions, the depth comes from how many images you have.
- **"Why stack them?"** Because then you can encrypt all of them in one pass, instead of running encryption N times.

### Memory anchor
**"Shrink. Stack. Scramble."** Three words. If you blank, those three words are the entire paper.

---

## Slide 3 — Color images are HEAVY

### What's on screen
The number 786,432, with the breakdown 512 × 512 × 3. A second number ≈ 7.8 million for a batch of 10. A visual of a stacked batch.

### What to know
A color image isn't just pixels — it's pixels times three channels (red, green, blue). So a 512 × 512 image isn't 262,144 numbers, it's 786,432 numbers. For a batch of 10, that's 7.8 million numbers. Each number is one byte, so a batch of 10 raw uncompressed color images is about 7.5 MB. Multiply by 100 images for a real medical use case, and you're at 75 MB before compression. That's a lot to push across a network, especially over wireless or constrained links.

### What to say
"Okay so the first problem the paper is attacking is bandwidth. Color images are HEAVY. A single 512-by-512 photo already has almost 800 thousand pixel values — that's height times width times three channels for red, green, and blue. Now think about real use cases — medical scans across hospitals, surveillance cameras across cities, satellite frames. You're never sending one image, you're sending dozens. Each one eats bandwidth. So before you even worry about security, transmission is slow and expensive. That's reason one why this paper exists."

### If you get asked the math
512 × 512 = 262,144 pixels. Each pixel has 3 channel values (R, G, B). 262,144 × 3 = 786,432. That's just one image.

### Why this matters for the paper
Because compression has to be part of the solution. You can't just encrypt — you'd be encrypting a giant file. The paper bakes compression INTO the encryption pipeline.

---

## Slide 4 — The wire is not safe

### What's on screen
A small diagram showing SENDER → wire → RECEIVER, with an ATTACKER tapping into the middle of the wire. Body text explaining the threat. A bottom strip saying "Slow AND unsafe — the paper attacks both at once."

### What to know
The wire (or wireless link) connecting sender to receiver passes through many nodes — your router, your ISP, transit networks, the receiver's ISP, and so on. Any of those nodes can copy the bytes. If the bytes are an unencrypted image, the attacker has the image. For medical, financial, military or surveillance content, this is unacceptable.

So encryption is mandatory. Historically, the standard practice is: compress the image first, encrypt the result, send it. That's two costs, two steps, repeated N times for N images. The paper's argument is that this is wasteful — you're paying for compression AND encryption separately, and you're not using the fact that you have multiple images to your advantage.

### What to say
"Second problem — the wire is not safe. Once an image leaves your device, anyone who taps the connection can read it. That's true for medical records, surveillance footage, personal photos, anything. Encryption fixes this, but historically encryption is treated as a SECOND step, done AFTER compression. So you're paying two costs separately, once per image. The paper's claim is that this is wasteful — both jobs should fold into one pipeline."

### Common audience confusion
- **"Couldn't you just use HTTPS?"** Yes, in practice you would use TLS/HTTPS for transit. But HTTPS encrypts the transport — once the data is at the receiver, it's decrypted. Image-level encryption keeps the image encrypted at rest. Plus, the paper's contribution is the combination of compression and encryption for batches, which TLS doesn't do.

---

## Slide 5 — Two tools, both from class

### What's on screen
Two boxes side by side. Left box: "Tool A — Discrete Wavelet Transform (DWT)." Right box: "Tool B — Chaotic Pseudo-Random Map."

### What to know
This is a transition slide. You're previewing the two tools before going deep on each. The audience needs to know:
- DWT does compression (you've seen it in class for image processing).
- Chaos does encryption (a deterministic function that looks random).

### What to say
"To do compression and encryption together, the paper uses two tools we've already touched in class. The first is the Discrete Wavelet Transform — DWT — which we used for image processing. The second is a chaotic map, which is a fancy term for a deterministic function that LOOKS random. The next three slides explain each of these tools, because once you understand them, the rest of the paper is just plumbing on top."

### Why this slide exists
Because if you jump straight into DWT mathematics, the audience drowns. This slide tells them: "two tools coming up, here's what they do at a high level, then I'll go deep on each."

---

## Slide 6 — DWT splits an image into 4 sub-bands

### What's on screen
The four sub-bands shown as a 2×2 grid: LL (top-left, highlighted in red), LH (top-right), HL (bottom-left), HH (bottom-right). Body text explaining what DWT does.

### What to know
You've seen frequency transforms before. In class we covered Fourier and the cosine transform (DCT), which JPEG uses. Both of those break a signal into frequencies, but they look at the whole image at once. The wavelet transform does the same thing — break into frequencies — except wavelets are LOCALIZED. Each wavelet captures features in a specific region of the image, not the whole image at once.

When you apply DWT to a 2D image, you get four outputs called sub-bands:

- **LL** = low frequencies in both directions. This is the "approximation" — a smaller, blurrier version of the original image.
- **LH** = low frequencies horizontally, high frequencies vertically. This captures horizontal edges.
- **HL** = high frequencies horizontally, low frequencies vertically. This captures vertical edges.
- **HH** = high frequencies in both. This captures diagonal edges and fine texture.

Each sub-band is half the height and half the width of the original. So the four sub-bands together still total the same number of pixels as the original (½ × ½ × 4 = 1).

### What to say
"So DWT first. In lecture we saw Fourier and the cosine transform — both of those break a signal into frequency components. DWT does the same thing, except wavelets are LOCAL — they catch features in a specific region of the image, not the whole image at once. When you apply DWT to an image, it returns four sub-bands, called LL, LH, HL, and HH. LL is a smaller, blurrier version of the image — the low frequencies. LH, HL, HH carry edge details — horizontal, vertical, diagonal. That's all DWT does."

### Common audience confusion
- **"What's a wavelet?"** A small wave-shaped function that's zero outside a certain region. Picture a single ripple. You slide it across the image and check how well it matches each spot. That's how DWT extracts local frequency information.
- **"Is DWT lossy?"** DWT itself is reversible — apply DWT, then apply inverse DWT, you get the exact original back. The compression comes from THROWING AWAY some of the sub-bands.

---

## Slide 7 — Keep LL. Throw the rest. Image is ¼ size

### What's on screen
On the left, the explanation paragraph. On the right, a diagram: the original image (large square, labeled h × w × 3) with a red downward arrow leading to a smaller square labeled "h/2 × w/2 × 3, ¼ size."

### What to know
This is where the compression actually happens. After DWT, the paper just keeps the LL sub-band and discards LH, HL, HH.

- LL has half the height and half the width of the original. So its area is ¼ of the original area. Image is now ¼ the size.
- You lose all the edge detail (LH, HL, HH). The recovered image will be slightly blurry compared to the original.

The reason this is acceptable: most of what your eye perceives in an image lives in the low frequencies — the broad shapes and colors. The high-frequency detail bands (sharp edges, textures) contribute to fidelity, but you can lose them and the image still looks "essentially the same." Specifically, the recovered image has PSNR > 30 dB, which is the visual quality threshold.

So yes, it's lossy compression. But it's acceptable, AND the results section proves the quality is high enough (32.06 dB after the full encrypt-decrypt round trip).

### What to say
"And here's the actual compression trick. The paper just keeps the LL sub-band and throws LH, HL, and HH away. That alone shrinks the image to ONE QUARTER the original size, because LL has half the height and half the width. Why is that OK? Because most of what your EYE actually perceives lives in the low frequencies — the broad shapes and colors. The detail bands matter a little, but you can lose them and the image still looks essentially the same. So it's lossy, but acceptable."

### Common audience confusion
- **"Why not also keep some detail bands?"** You could. The paper's tradeoff is maximum compression (¼ size) at acceptable quality. Keeping more bands gives better quality but less compression.
- **"How is this different from JPEG?"** JPEG uses DCT (a similar frequency transform) and quantizes the high frequencies more aggressively, but it doesn't throw them out entirely. The paper's approach is more aggressive on compression but simpler.

---

## Slide 8 — Chaos: deterministic, but looks random

### What's on screen
Left side: explanation. Right side: a chaos trajectory visual (dots connected by thin lines, jumping around erratically). Below that, the paper's key parameters: a, b, c, d, k₁, k₂ = 0.3, 0.94, 0.9, 1.6, -1.8, -1.8.

### What to know
A chaotic map is just a math function you iterate. The paper uses a 3D map — meaning it takes three numbers in, gives three numbers out.

Picture this:
- Start: (x₀, y₀, z₀) = (0.1, 0.1, 0.1).
- Step 1: feed into the function, get (x₁, y₁, z₁).
- Step 2: feed (x₁, y₁, z₁) back in, get (x₂, y₂, z₂).
- Step 3: feed (x₂, y₂, z₂) back in, get (x₃, y₃, z₃).
- Repeat thousands of times.

The sequence of (x, y, z) values you produce is the chaotic stream. It looks completely random — no pattern, no period, no visible structure. BUT it's deterministic. If you start from the exact same (x₀, y₀, z₀) and use the exact same parameters (a, b, c, d, k₁, k₂), you get the exact same sequence every time.

That's why it's perfect for encryption:
- You and the receiver agree on the starting numbers and parameters (your shared key).
- You both generate the same sequence.
- You XOR your image with the sequence to encrypt.
- The receiver XORs the cipher with the same sequence to decrypt.
- An attacker, not knowing the starting numbers, sees the cipher as noise.

The key property is *extreme sensitivity*: change any starting number by 10⁻¹⁵ — basically a rounding error — and the entire sequence diverges. So an attacker can't approximate the key.

### What to say
"Now the second tool — a chaotic map. Imagine a function that takes three numbers in, and spits three new numbers out. You feed those back in, get new ones, feed them back, on and on. The output LOOKS completely random — no pattern, no period, no structure you can see. BUT it's deterministic — same starting numbers, same sequence, every time. The trick is — those starting numbers become your secret key. The receiver knows the key and can reproduce the exact sequence to decrypt. An attacker without the key sees noise. Maria, take it from here."

### Common audience confusion
- **"Why not just use a regular random number generator?"** Two reasons. First, regular pseudo-random generators have periods — eventually the sequence repeats. Chaos doesn't (effectively). Second, chaos has the extreme sensitivity property, which makes the key space huge.
- **"Why 3D?"** Because the paper uses a 3D data structure (the cube). A 3D chaos map matches the 3D data naturally. You get three independent chaotic streams from one iteration, which the algorithm uses for the three axes (i, j, k).

### Memory anchor
**"Same key, same stream. Different key, different stream."**

This is also where Abdul hands off to Maria. Practice the handoff: Abdul says *"Maria, take it from here."* Maria physically steps forward.

---

## Slide 9 — Novelty: encrypt the cube, not the images

### What's on screen
Two columns side by side. **Left column** (grey, muted): "THE OLD WAY — One image at a time." Numbered list: 1. Compress image 1. 2. Encrypt image 1. 3. Send image 1. 4. Compress image 2. 5. Encrypt image 2. 6. Send image 2. ... repeat for every image. **Right column** (red-bordered, accented): "THE NEW WAY · THIS PAPER — Whole batch at once." Numbered list: 1. Compress EVERY image (DWT, keep LL). 2. STACK them into a single 3D cube. 3. Encrypt the cube ONCE. 4. Send the cipher cube. Plus a "ONE PIPELINE. ONE PASS." stamp.

### What to know
**This is THE slide. This is what makes the paper publishable. This is what the professor is checking for when she grades "novelty."**

Old approaches treat compression and encryption as two separate steps, applied to one image at a time. If you have 10 images, you compress 10 times, encrypt 10 times, send 10 times. That's 20 separate processing steps total.

The new approach folds compression and encryption into a single pipeline that operates on the whole batch at once. For 10 images, you compress all 10 (10 steps), stack into a cube (1 step), encrypt the cube (1 step), send the cipher cube (1 step). 13 steps total instead of 20.

More importantly: the encryption operates on the WHOLE BATCH as one mathematical object. The chaotic offsets and XOR streams move pixels and flip bits ACROSS images, not just within each image. That's what gives the security analysis its strength — the cipher cube has properties (entropy, NPCR, UACI) that hold for the whole batch, not per-image.

### What to say
"Thanks Abdul. So here's the actual novelty — the one slide to remember. The OLD WAY is: encrypt each image one at a time. If you've got ten photos, you run encryption ten times. Compression and encryption are two distinct steps applied independently. The NEW WAY this paper proposes is: shrink every image first with DWT, stack them all on top of each other into a single 3D block they call a cube, and run encryption ONCE on the whole cube. Encryption happens once instead of ten times. Compression happens first, so the cube is already small. That's the contribution."

### Memory anchor
**"Old way ten times. New way once."**

### Common audience confusion
- **"How can chaos encrypt all the images at once? Don't you need a key per image?"** No. The cube is one object. One key generates one chaotic stream. The stream covers every pixel of the cube, regardless of which image that pixel originally came from.
- **"Doesn't stacking expose images to each other?"** No. The encryption operates on the whole cube. After encryption, you can't tell which pixel belonged to which image — it's all noise.

---

## Slide 10 — The pipeline at a glance

### What's on screen
Four numbered columns: 01 DWT compress, 02 Stack cube C, 03 Confusion, 04 Diffusion. Connected by arrows. Below, an "OUTPUT — Cipher cube D" strip.

### What to know
This is the methodology overview. Stages 1 and 2 build the cube. Stages 3 and 4 encrypt it. Then transmit. Receiver runs the inverse.

The next three slides go deep on stages 1+2 (one slide), stage 3 (one slide), and stage 4 (one slide). This slide is the map.

### What to say
"So how does this actually flow end to end? Four stages, in order. Stage one: compress each image with DWT. Stage two: stack the compressed images into the cube C. Those two stages are the setup half. Stage three: confusion — chaos scrambles pixel POSITIONS inside the cube. Stage four: diffusion — chaos changes pixel VALUES. End result is the cipher cube D, which is what gets transmitted. The receiver runs all four stages in reverse and recovers the original images. Let's walk through each stage."

### Memory anchor
**"DWT, stack, confusion, diffusion."** Four words. In order.

---

## Slide 11 — Stages 1 + 2: Compress and stack

### What's on screen
Left side: pseudocode describing stage 1 (per image: split RGB, run DWT, keep LL) and stage 2 (stack into cube, dimensions from largest image, pad smaller with zeros). Right side: diagram showing N color images → DWT → Cube C.

### What to know
**Stage 1 — compression.** For each color image:
1. Split it into three channels: R, G, B.
2. Run DWT on each channel separately. You get LL, LH, HL, HH for each channel.
3. Keep only LL. Discard the rest.
4. Each channel is now ¼ size. The whole image is now ¼ size.

**Stage 2 — stacking.** Take all the LL data from all your images and arrange them into a 3D cube:
- Width of the cube = max(h_i / 2) across all images. (The biggest image, halved.)
- Height of the cube = max(w_i / 2).
- Depth of the cube = N, the number of images you have.

If smaller images don't fill the cube's width/height, you pad with zeros. (This is the limitation flagged on the last slide.)

### What to say
"Stages one and two — the setup. Stage one: for each color image, split it into red, green, and blue channels, run DWT on each channel, and keep only the LL sub-band. Every image is now a quarter of its original size. Stage two: take all those LL blocks and stack them into a single 3D cube. The width and height of the cube come from the BIGGEST image in the batch divided by two. The depth is the number of images. If smaller images don't fill the cube, you pad with zeros. Setup done."

### Worked example
Say you have 3 images: a 512×512, a 256×256, and a 384×384.
- After DWT and LL-only: 256×256, 128×128, 192×192.
- Largest is 256×256. So the cube is 256 (width) × 256 (height) × 3 (depth).
- The 256×256 fills its slice. The 128×128 and 192×192 are placed in their slices and padded with zeros.

---

## Slide 12 — Confusion: scramble pixel POSITIONS

### What's on screen
Definition strip at top. Left: ANALOGY (Scrabble tiles) + numbered ALGORITHM. Right: BEFORE/AFTER pixel grids. Below: "WHY IT'S CLEVER" note about plaintext-awareness.

### What to know
**Cryptographic confusion** means changing where information is, without changing what it is. Pixel values stay exactly the same — only the positions where they sit in the cube change.

**The Scrabble analogy:** imagine the letters of a sentence laid out on a Scrabble board. Confusion is what happens when you pick up all the tiles and put them back in random positions. The same letters are still on the board, but the sentence is now nonsense.

**How the algorithm works:**
1. Iterate the chaotic map once per cube pixel. (Total iterations = M_h × M_w × z, where M_h × M_w is the cube's width × height and z is the depth.)
2. From each iteration, take the three output values (x, y, z), apply floor and modulo operations to convert them into integer offsets in the right range. These become S₁, T₁, U₁ — one offset per axis of the cube.
3. For every pixel at position (i, j, k):
   - Compare i with S₁: is i greater than, less than, or equal to S₁?
   - Compare j with T₁: greater than, less than, or equal to?
   - Compare k with U₁: greater than, less than, or equal to?
   - These three comparisons give you nine possible combinations. Each combination dictates a specific swap operation (move the pixel by a specific amount along each axis).
4. After running this for every pixel in the cube, you have the confusion cube C'.

**Why it's clever:** The offsets S₁, T₁, U₁ are computed from the chaotic state that itself depends on the plaintext. So encrypting two different plaintext images with the same key gives two completely different cipher cubes. This is called *plaintext-awareness* — a known good property in modern encryption design.

### What to say
"Stage three — confusion. In cryptography, confusion means: change WHERE the information is, but don't change WHAT it is. Think of it like shuffling Scrabble tiles on a board — same letters, but the board looks like nonsense. How does it work here? The chaotic map is iterated to produce three integer offsets, S₁, T₁, U₁ — one for each axis of the cube. Then for every pixel at position (i, j, k), the algorithm compares each coordinate with its offset, and based on bigger, smaller, or equal, the pixel swaps to a new position."

### Common audience confusion
- **"What are the nine cases?"** Three axes, each with three possible comparisons (>, <, =). 3 × 3 = 9. You don't need to memorise them. Just know there ARE nine and they're enumerated in Section 4.1.2 of the paper.

### Memory anchor
**"Same pixels, different positions."**

---

## Slide 13 — Diffusion: flip pixel VALUES, chain to previous

### What's on screen
Definition strip at top. Hero formula: **D[k] = V[k] ⊕ chaos[k mod 3] ⊕ D[k−1]**. Below it, symbol legend (V[k], chaos[k mod 3], D[k−1], D[k]). Bottom: "WHY THE CHAIN MATTERS" — avalanche effect note.

### What to know
**Cryptographic diffusion** means changing what each pixel is, not where. After confusion (which moved pixels around), diffusion now scrambles their values.

**The algorithm:**
1. Take the confusion cube C' and flatten it into a 1-dimensional vector V. So now you have a long list of pixel values, indexed 0, 1, 2, ..., N−1.
2. Iterate the chaotic map again (independently from confusion) to produce three new streams: X₂, Y₂, Z₂.
3. For the very first pixel V[0]: XOR it with a chaotic seed value to produce D[0].
4. For every later pixel V[k] (k ≥ 1):
   - Compute k mod 3. This gives 0, 1, or 2.
   - Use the result to pick one of the three streams: X₂, Y₂, or Z₂.
   - Take the value at index k from that stream: chaos[k mod 3, k].
   - Compute D[k] = V[k] XOR chaos[k mod 3, k] XOR D[k−1].
5. After processing the whole vector, reshape it back into a cube. That's the final cipher cube D.

**The chain matters because of the avalanche effect.** Each cipher pixel D[k] depends on D[k−1]. So if you flip a single bit at D[0], it changes D[1] (because D[1] uses D[0] in its computation), which changes D[2], which changes D[3], and so on. One bit change at the start cascades through the entire image. That's exactly what good encryption should do — small input change, huge cipher change. It's also what makes the NPCR and UACI metrics on the next slide hit such high values.

### What to say
"Stage four — diffusion. Diffusion changes the pixel VALUES. First, flatten the confusion cube into a 1D vector V. Then iterate chaos again, getting three new streams. For each pixel in V, the algorithm picks one of those streams based on index mod 3, and XORs the pixel with that chaos value. The critical part — each output pixel ALSO XORs with the previous output. That makes the encryption a chain. Flip one bit at the start and every later pixel breaks. Reshape the vector back into a cube and you have the final cipher cube D."

### Worked example
Say V = [42, 100, 200, ...] and the chaos sequence is [17, 33, 91, ...] and the initial seed is 5.
- D[0] = 42 XOR 17 XOR 5 = ?  (XOR is bitwise; you'd convert to binary and flip bits where they don't match)
- D[1] = 100 XOR 33 XOR D[0]
- D[2] = 200 XOR 91 XOR D[1]
- And so on.

You don't need to do the XOR math live in the presentation — just know that's what's happening.

### Memory anchor
**"Each output glued to the previous one."**

---

## Slide 14 — PSNR 32.06 dB · past the visual threshold

### What's on screen
Top: explanation of PSNR. Left hero number: 32.06 dB. Right: bar chart with this paper (red bar, longest) vs four prior schemes (black bars, shorter), with a vertical 30 dB threshold marker.

### What to know
**PSNR** = Peak Signal-to-Noise Ratio. It measures how close a recovered image is to the original. Higher is better. The formula involves the mean squared error between original and recovered pixels, normalised by the maximum possible pixel value (255 for 8-bit images), inside a log:

PSNR = 10 · log₁₀(255² / MSE)

You don't need the formula in the talk. You need:
- It's measured in decibels (dB).
- It's logarithmic — each +3 dB roughly doubles the signal-to-noise ratio.
- ~30 dB is the visual quality threshold. Above that, the average viewer can't distinguish recovered from original.
- 40 dB or higher is essentially perfect reconstruction.

**The paper's result: 32.06 dB.** This is after lossy DWT compression (you threw away three sub-bands) AND a full encrypt-decrypt round trip. So the recovered image is past the visual threshold even after all that processing.

**Prior work comparison:**
- Ref. [22]: 27.69 dB
- Ref. [19]: 27.49 dB
- Ref. [46]: 27.34 dB
- Ref. [8]:  26.29 dB

All four are below 30 dB. The paper is 4 to 6 dB better, which on the log scale is a meaningful jump.

### What to say
"Okay — so does it actually work? Reconstruction quality is measured with PSNR, peak signal-to-noise ratio, in decibels. Quick rule: anything around 30 dB is visually good — the recovered image looks essentially the same as the original. This paper hits 32.06 dB on average, which is PAST the threshold, even after lossy DWT compression PLUS a full encrypt-and-decrypt round trip. The four prior schemes the authors benchmark against land between 26.3 and 27.7 dB — BELOW the visual threshold. So this paper is the difference between looks-the-same and looks-degraded."

### Common audience confusion
- **"Why is logarithmic important?"** Because the difference between 27 dB and 32 dB isn't 5 units of "a bit better" — it's 5 dB = ~3× improvement in signal-to-noise ratio. Logarithmic scales make small numerical differences meaningful.
- **"Where does the 30 dB threshold come from?"** It's an empirical rule from image quality research. Above 30 dB, most viewers in subjective tests can't tell the difference between original and recovered.

---

## Slide 15 — Security: four checks, all pass

### What's on screen
A table with five rows: NIST randomness, NPCR, UACI, Entropy, Key space. Each row has the check name, what it tests, the paper's result, and a red PASS stamp. Verdict line at bottom.

### What to know
Each security test attacks the cipher in a different way. The paper passes all of them.

**1. NIST randomness battery.** Fifteen statistical tests applied to the chaotic sequence used as the encryption key stream. Each test asks: "does this sequence look like genuine random noise?" Pass condition for each test: p-value ≥ 0.01 AND pass rate above a threshold. The paper reports all 15 tests pass.

**2. NPCR (Number of Pixels Change Rate).** Differential attack test. Take an image, encrypt it. Take the same image, flip ONE pixel, re-encrypt. Compare the two cipher images. NPCR is the percentage of pixels that differ between them. The ideal target is **99.6094 %** — meaning a one-pixel change in input should change 99.6094 % of pixels in output. The paper reports **99.6533 %** — slightly above ideal, which means even better.

**3. UACI (Unified Average Changing Intensity).** Same setup as NPCR, but instead of "did the pixel change yes/no," it measures the average magnitude of the change. Ideal target: **33.4635 %**. Paper hits **33.4887 %** — again, dead on.

**4. Information entropy.** A measure of how uniformly distributed the pixel values are in the cipher image. For 8-bit pixels, the theoretical maximum entropy is exactly **8.0** (meaning all 256 possible pixel values appear with equal probability). The paper reports **7.9994** — essentially indistinguishable from uniform random noise.

**5. Key space.** How many possible keys exist. The paper's key space is determined by the precision of the chaotic parameters. With six parameters and three initial values, each at 10⁻¹⁵ precision, the key space is around 10¹³⁵, or roughly 2⁴⁵⁰. Brute-forcing a 2⁴⁵⁰ key space requires more energy than exists in the observable universe. So brute force is not a threat.

### What to say
"Now security — four checks, all pass. One: the chaotic sequence goes through the NIST randomness battery, 15 statistical tests. Every one passes. Two: differential attack — flip one pixel of the input, measure how much the cipher changes. NPCR target is 99.6094, paper hits 99.65. UACI target is 33.46, paper hits 33.49. Dead on the ideals. Three: information entropy of the cipher is 7.9994 out of a theoretical max of 8 — indistinguishable from uniform noise. Four: the key space is enormous, way beyond brute force. Statistical, differential, brute force — all blocked."

### Common audience confusion
- **"What's a differential attack?"** An attack where you have access to encrypt arbitrary plaintexts and you study how small input changes affect the output. If small input changes only cause small output changes, the cipher is weak.
- **"Why are NPCR and UACI specific numbers?"** They come from a statistical model. For an 8-bit image cipher behaving like random noise, the expected NPCR is 99.6094 % and expected UACI is 33.4635 %. Hitting those numbers means the cipher is statistically indistinguishable from random.

---

## Slide 16 — Limitation, take-home, questions

### What's on screen
Three hero numbers at top: 32 dB (PSNR), 7.9994 (entropy), 99.65 % (NPCR). LIMITATION and TAKE-HOME paragraphs. A big "Questions?" at the bottom.

### What to know
**The honest limitation:** when the images in a batch have different sizes, the cube has to be padded with zeros. That wastes space — you're carrying around empty cells just to fit the dimensions. The authors openly flag this in their paper as future work. Always admit this limitation if asked.

**The take-home:** by combining DWT and a 3D chaotic map, you get compression AND encryption in a single pipeline, applied to a whole batch of images at once. Reconstruction quality is past the visual threshold, security passes all standard tests, and the limitation is openly documented. That's a clean contribution.

### What to say
"One honest limitation, which the authors flag themselves — when the images in a batch have different sizes, the cube has to be padded with zeros, and that wastes space. They mark it as future work. Take-home in one breath: by combining DWT compression with a 3D chaotic map, you get encryption AND compression in a single pipeline, for a whole batch of images, with reconstruction quality above the visual threshold and security all green. Thanks for listening — we're happy to take questions."

---

## Q&A defense — anticipated questions with full answers

### Q1: Is this lossless?
**No.** DWT keeping only the LL sub-band is lossy compression — you throw away three of the four sub-bands. The recovered image will be slightly blurry compared to the original. However, the loss is small enough that PSNR after the full round trip is 32 dB, which is past the visual quality threshold. So it's lossy on paper, but visually it's effectively lossless.

### Q2: Why a cube? Why not just encrypt each image separately?
Encrypting each image separately works, but you have to run encryption N times for N images. The cube approach encrypts all of them in one pass. More importantly, the chaotic encryption operates ACROSS images, not just within each — so the cipher's statistical properties (entropy, NPCR, UACI) hold for the whole batch as one unit. That's a stronger security guarantee than per-image encryption.

### Q3: What's the main limitation?
Zero-padding wastes space when batch images have different sizes. If you have one 512×512 image and one 64×64 image, the cube has to be 256×256 (after DWT halving), and the 64×64 image's slice will be mostly empty. The authors flag this as future work.

### Q4: Is chaos alone enough for security?
No. Chaos provides the pseudo-random stream, but the security comes from combining three things: confusion (position scrambling), diffusion (value flipping with cascade), and the fact that the chaotic offsets depend on the plaintext (plaintext-awareness). Plus, the chaotic stream itself is validated by the NIST randomness battery. Chaos alone, without the algorithm structure, would not be secure.

### Q5: What's the strongest result?
PSNR 32.06 dB AND entropy 7.9994 AND NPCR 99.65 % all simultaneously. Any one of these alone is good. Together, they mean the scheme is lossy enough to compress 4× but recoverable past the visual threshold, AND statistically indistinguishable from random noise, AND robust against differential attacks. That combination is the contribution.

### Q6: How does it compare to AES?
AES is a general-purpose block cipher — it doesn't care if the data is an image, a text file, or a video. It's fast and well-vetted. This paper is image-specific: it bakes in compression (which AES doesn't do) and operates on a batch of images at once (which AES would require special modes to do). So AES is more general; this paper is more specialized for the multi-image case.

### Q7: How does it compare to JPEG?
JPEG uses DCT (a similar transform to DWT) and applies quantization to compress. This paper uses DWT and keeps only LL — more aggressive compression but simpler. JPEG also doesn't encrypt; you'd combine JPEG with AES separately. This paper does compression and encryption in one pipeline.

### Q8: Could you scale this to video?
In principle yes — a video is a sequence of frames, and you could stack frames into a cube similar to how the paper stacks images. Some adjustments would be needed for temporal redundancy. The paper doesn't address video; it's a possible extension.

### Q9: What if an attacker captures the cipher cube and tries every key?
The key space is roughly 2⁴⁵⁰ (based on the precision of the chaotic parameters). Brute-forcing 2⁴⁵⁰ keys is infeasible — it would require more energy than exists in the observable universe. So brute force is not a practical attack.

### Q10: Why DWT specifically and not DCT?
DWT is localized (each wavelet covers a region) while DCT is global (each basis function covers the whole image). For image compression, DWT tends to handle edges and sharp features better. JPEG 2000 uses DWT; older JPEG uses DCT. The paper picks DWT for its locality property.

---

## Defense moves — what to say if you blank during the talk

### If you blank during your half
Say the one-sentence thesis slowly: *"This paper combines DWT compression with a 3D chaotic map to encrypt multiple color images of different sizes in a single cube, reaching 32 dB PSNR and entropy 7.9994."* That sentence buys you 8-10 seconds to recover.

### If you forget what DWT stands for
Say *"the wavelet transform we saw in class."* The professor will recognize it.

### If a number escapes you
Round. *"Around 32 decibels"* is fine for PSNR. *"About 99.65 percent"* is fine for NPCR. Don't say a wrong number with confidence — say a rough number with a hand-wave.

### If you're asked a question you don't know
*"That's a good question. The paper doesn't address that directly, but I'd guess [reasonable guess]. Maria, do you have a thought on that?"* (And vice versa.) Honest "I don't know but here's my best guess" beats fake confidence.

### If you're asked something genuinely outside the paper
*"That's outside the scope of this paper — it's something we'd want to look up. Happy to follow up after the talk if you'd like."*

---

## How to study with this guide

**Plan A (you have a day):**
1. Read the panic-mode summary at the top. (5 minutes.)
2. Read the mental model story. (5 minutes.)
3. Open the deck PDF beside this document. Go through it slide by slide, reading the chapter for each slide. (90 minutes.)
4. Read the Q&A defense bank. (15 minutes.)
5. Do one full out-loud rehearsal of your half. Time it. (5 minutes for your half.)

**Plan B (you have an hour):**
1. Panic-mode summary. (5 min.)
2. Mental model story. (5 min.)
3. Skim the chapters for slides 1-8 if you're Abdul, or 9-16 if you're Maria. Focus on "What to say." (30 min.)
4. Read the Q&A defense bank. (10 min.)
5. One rehearsal. (10 min.)

**Plan C (you have 20 minutes before the talk):**
1. Panic-mode summary. (5 min.)
2. Memory anchors only — find the bold *"Memory anchor"* lines in each slide chapter. (10 min.)
3. Read the "Defense moves" section. (5 min.)

You'll be fine.

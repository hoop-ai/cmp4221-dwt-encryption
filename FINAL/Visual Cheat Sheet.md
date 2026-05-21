---
sticker: emoji//1f3a8
tags:
  - course
  - multimedia
  - project
  - diagrams
---
# Visual Cheat Sheet

> Every concept in the paper, as a diagram. About 15 minutes to scan.

---

## §1. The whole paper, in one picture

```
                         THE WHOLE PAPER

      ┌────────────┐       ┌────────────┐       ┌────────────┐
      │            │       │            │       │            │
      │  BATCH OF  │ ────▶ │   3D CUBE  │ ────▶ │   CIPHER   │
      │   COLOR    │  DWT  │  (stacked  │ CHAOS │    CUBE    │
      │   IMAGES   │       │    LLs)    │       │            │
      │            │       │            │       │            │
      └────────────┘       └────────────┘       └────────────┘

         shrink                stack                scramble
        each one              the batch          (one encryption
        with DWT             into one block       on whole cube)
```

That's the entire paper. Read left to right.

---

## §2. A color image, exploded

A single color image is not one grid of pixels. It's three grids stacked on top of each other:

```
                  ┌───────────────────┐
                 ╱                   ╱│
                ╱        RED        ╱ │
               ╱___________________╱  │
               │                   │  │
               │       GREEN       │  │  ← three "channels"
               │                   │  │
               │                   │  ╱
               │       BLUE        │ ╱
               │___________________│╱

           Width × Height × 3 = pixel values

           A 512 × 512 color image holds
           512 × 512 × 3 = 786,432 values.
```

This is why color images are heavy.

---

## §3. What DWT does to one channel

Take just the RED channel (or any single channel). DWT splits it into four smaller pieces:

```
       ORIGINAL CHANNEL              AFTER DWT
        (W × H pixels)            (W × H pixels total,
                                   split into 4 sub-bands)

      ┌─────────────────┐        ┌────────┬────────┐
      │                 │        │   LL   │   LH   │
      │                 │        │ approx │  horiz │
      │                 │        │        │ edges  │
      │       ALL       │  DWT   ├────────┼────────┤
      │       THE       │ ────▶  │   HL   │   HH   │
      │       PIXELS    │        │  vert  │  diag  │
      │                 │        │  edges │  edges │
      │                 │        │        │        │
      └─────────────────┘        └────────┴────────┘

                                  Each sub-band is
                                  ½ width × ½ height
```

DWT itself is reversible. If you keep all four sub-bands and apply inverse DWT, you get the exact original back.

---

## §4. The compression trick — keep ONLY LL

```
       AFTER DWT                          KEPT BY PAPER

      ┌────────┬────────┐                ┌────────┐
      │ ✓ LL   │ ✗ LH   │                │   LL   │
      │ keep   │ drop   │                │ approx │
      │        │        │                │        │
      ├────────┼────────┤    ─────▶      └────────┘
      │ ✗ HL   │ ✗ HH   │
      │ drop   │ drop   │                ¼ of the
      │        │        │                original area
      └────────┴────────┘

         Lossy compression.
         Quality survives because most of what
         your eye sees lives in LL.
```

---

## §5. Stacking — how the cube is built

```
     N COLOR IMAGES                  STACKED INTO ONE CUBE

      ┌───┐                                ┌───────┐
      │   │ image 1                       ╱        ╱│
      └───┘                              ╱        ╱ │
        │                               ╱        ╱  │
        ▼                              ┌────────┐   │
       DWT                             │        │   │   ← each LL block
       keep LL                         │ CUBE C │   │     becomes one
        │                              │        │   ╱     "slice" in
        ▼                              │ (W × H │  ╱      the cube
      ┌─┐                              │  × N)  │ ╱
      │ │ ¼ size                       │        │╱
      └─┘                              └────────┘

      ┌───┐                                width × height
      │   │ image 2                        comes from largest image
      └───┘                                depth = N (image count)
        │
        ▼
       DWT
       keep LL ──────────────▶ stack into cube
        │
        ▼
      ... repeat for all N images
```

---

## §6. The 4-stage pipeline

```
   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
   │   01    │    │   02    │    │   03    │    │   04    │
   │         │    │         │    │         │    │         │
   │   DWT   │───▶│  STACK  │───▶│CONFUSION│───▶│DIFFUSION│
   │compress │    │cube  C  │    │ scramble│    │  XOR +  │
   │   LL    │    │         │    │positions│    │  chain  │
   │         │    │         │    │         │    │         │
   └─────────┘    └─────────┘    └─────────┘    └─────────┘
                                                       │
                                                       ▼
                                                 ┌─────────┐
                                                 │ CIPHER  │
                                                 │ CUBE D  │
                                                 │ (sent)  │
                                                 └─────────┘

   ◄─────── setup half ───────▶   ◄────── encryption half ──────▶

   Receiver runs the entire chain in reverse to recover
   the original images.
```

---

## §7. Confusion — same pixels, different positions

Confusion changes WHERE pixels sit, not WHAT they are.

```
        BEFORE CONFUSION                    AFTER CONFUSION

      ┌───┬───┬───┬───┬───┐                ┌───┬───┬───┬───┬───┐
      │   │   │   │   │   │                │   │   │   │   │ B │
      ├───┼───┼───┼───┼───┤                ├───┼───┼───┼───┼───┤
      │   │ A │   │   │   │                │   │   │   │   │   │
      ├───┼───┼───┼───┼───┤    chaos       ├───┼───┼───┼───┼───┤
      │   │   │   │   │   │   shuffles     │   │   │   │   │   │
      ├───┼───┼───┼───┼───┤   positions    ├───┼───┼───┼───┼───┤
      │   │   │   │ B │   │  ─────────▶    │ A │   │   │   │   │
      ├───┼───┼───┼───┼───┤                ├───┼───┼───┼───┼───┤
      │   │   │   │   │   │                │   │   │   │   │   │
      └───┴───┴───┴───┴───┘                └───┴───┴───┴───┴───┘

         pixel A at (1, 1)                  pixel A now at (3, 0)
         pixel B at (3, 3)                  pixel B now at (0, 4)
         values unchanged                   values unchanged

      Analogy: Scrabble tiles on a board. Pick up every tile
      and put it back in a random spot. Same letters. Looks
      like nonsense now.
```

---

## §8. Diffusion — flip values, chained to previous

Diffusion changes the values, AND links every output to the previous one.

```
                  D[k]  =  V[k]  ⊕  chaos[k mod 3]  ⊕  D[k-1]


   ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐
   │V[0] │    │V[1] │    │V[2] │    │V[3] │    │V[4] │     ◀── input (from confusion)
   └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘
      ▼          ▼          ▼          ▼          ▼
   ┌──┴──┐    ┌──┴──┐    ┌──┴──┐    ┌──┴──┐    ┌──┴──┐
   │seed │ ⊕  │ X₂  │ ⊕  │ Y₂  │ ⊕  │ Z₂  │ ⊕  │ X₂  │     ◀── chaos stream
   └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘        (cycle X₂/Y₂/Z₂
      ▼          ▼          ▼          ▼          ▼            via index mod 3)
   ┌──┴──┐ ─▶ ┌──┴──┐ ─▶ ┌──┴──┐ ─▶ ┌──┴──┐ ─▶ ┌──┴──┐
   │D[0] │    │D[1] │    │D[2] │    │D[3] │    │D[4] │     ◀── cipher (chained)
   └─────┘    └─────┘    └─────┘    └─────┘    └─────┘
              ↑ uses    ↑ uses     ↑ uses     ↑ uses
                D[0]      D[1]       D[2]       D[3]

   ⊕ = XOR (bitwise flip)
   Chain forces avalanche: one bit change at D[0] breaks
   every later D[k].
```

---

## §9. Why chaining matters — the avalanche effect

```
     INPUT IMAGE A          INPUT IMAGE A′ (one pixel flipped)

      ┌───┬───┬───┬───┐         ┌───┬───┬───┬───┐
      │ 5 │ 2 │ 8 │ 1 │         │ 6 │ 2 │ 8 │ 1 │  ← only this differs
      └───┴───┴───┴───┘         └───┴───┴───┴───┘
              │                          │
              ▼ encrypt                  ▼ encrypt
      ┌───┬───┬───┬───┐         ┌───┬───┬───┬───┐
      │ a │ b │ c │ d │         │ x │ y │ z │ w │  ← EVERY pixel differs
      └───┴───┴───┴───┘         └───┴───┴───┴───┘

      ▲ THIS is what NPCR (99.65 %) measures: ▲
      "what % of cipher pixels change when ONE input pixel changes?"
      Ideal is 99.6094 %. Paper: 99.6533 %. Dead on.
```

---

## §10. PSNR — is the recovered image any good?

```
            ◀──── worse ────                ──── better ────▶

    0 dB                     30 dB                          ∞
    │     │     │     │     │  ←threshold  │     │     │     │
    ────────────────────────────────────────────────────────────
                                  │
        Ref. [8]  Ref. [46]      │     32.06  ◀── this paper
        26.29 dB  27.34 dB       │     dB
                                  │
                  Ref. [22]       │
                  27.69 dB        │
                                  │
                  Ref. [19]       │
                  27.49 dB        │
                                  │
                                 30 dB
                          ════════════════════
                          visual threshold:
                          above this, the
                          average viewer can't
                          tell from original

    Prior work: below threshold (looks degraded).
    This paper: above threshold (looks identical).
    Logarithmic scale — each +3 dB doubles SNR.
```

---

## §11. The four security tests, all green

```
   ┌────────────────────┬───────────────────┬─────────────────┬──────┐
   │ TEST               │ TARGET            │ PAPER RESULT    │      │
   ├────────────────────┼───────────────────┼─────────────────┼──────┤
   │ NIST randomness    │ 15-test battery   │ 15 / 15 passed  │ PASS │
   │ NPCR               │ 99.6094 %         │ 99.6533 %       │ PASS │
   │ UACI               │ 33.4635 %         │ 33.4887 %       │ PASS │
   │ Entropy            │ max = 8.0         │ 7.9994          │ PASS │
   │ Key space          │ brute-force proof │ > 2¹⁵⁰          │ PASS │
   └────────────────────┴───────────────────┴─────────────────┴──────┘

   What each one means in one line:

   NIST       — "is the chaos truly random?"        Yes, all 15 tests.
   NPCR       — "if I flip 1 input pixel,           99.65 % of cipher
                 how much of the cipher changes?"   pixels change.
   UACI       — "by how much do they change?"       33.49 % avg intensity.
   Entropy    — "is the cipher = pure noise?"       7.9994 / 8 → yes.
   Key space  — "can brute force find the key?"     No, way too large.
```

---

## §12. The OLD WAY vs NEW WAY — the actual contribution

```
   ┌──────────────────────────────┐   ┌──────────────────────────────┐
   │      THE OLD WAY             │   │  THE NEW WAY (this paper)    │
   │   one image at a time        │   │     whole batch at once      │
   ├──────────────────────────────┤   ├──────────────────────────────┤
   │                              │   │                              │
   │   1.  compress  image 1      │   │   1.  compress EVERY image   │
   │   2.  encrypt   image 1      │   │       (DWT, keep LL)         │
   │   3.  send      image 1      │   │                              │
   │                              │   │   2.  STACK them all into    │
   │   4.  compress  image 2      │   │       a single 3D cube       │
   │   5.  encrypt   image 2      │   │                              │
   │   6.  send      image 2      │   │   3.  encrypt the cube ONCE  │
   │                              │   │                              │
   │   ...repeat N times...       │   │   4.  send the cipher cube   │
   │                              │   │                              │
   │   2 × N processing steps     │   │   ~3 processing steps total  │
   │   N separate encryptions     │   │   1 encryption on a batch    │
   │                              │   │                              │
   └──────────────────────────────┘   └──────────────────────────────┘
              wasteful                       one pipeline, one pass
```

---

## §13. Memory anchors per slide

```
   ┌────┬────────────────────────────────────────────────────────┐
   │ #  │ Memory anchor (3 words or less)                        │
   ├────┼────────────────────────────────────────────────────────┤
   │  1 │ "Shrink. Stack. Scramble."                             │
   │  2 │ "Slow AND unsafe."                                     │
   │  3 │ "DWT plus chaos."                                      │
   │  4 │ "Old way ten times. New way once."                     │
   │  5 │ "DWT, stack, confusion, diffusion."                    │
   │  6 │ "Same pixels, different positions."                    │
   │  7 │ "Each output glued to the previous one."               │
   │  8 │ "Past the visual threshold."                           │
   │  9 │ "Four checks, all green."                              │
   │ 10 │ "One pipeline. Padding is the limitation."             │
   └────┴────────────────────────────────────────────────────────┘
```

---

**Next read:** [STUDY GUIDE](STUDY%20GUIDE.md) — slide-by-slide deep dive, with worked examples and Q&A defense.

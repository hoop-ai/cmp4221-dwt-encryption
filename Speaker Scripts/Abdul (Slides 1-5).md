---
sticker: emoji//1f399
tags:
  - speaker
  - script
  - abdul
  - presentation
---
# Speaker script - Abdul (slides 1-5)

Target: about 5 minutes. Read it out loud at a calm pace. The pauses matter.

## Slide 1 - Title (0:45)

**On-screen:** Encrypt a batch, not one image.

**Script**

> Hi everyone. I'm Abdul, and this is Maria. [pause]
>
> Our paper solves a practical problem: image batches are large, and they still need privacy.
>
> The authors combine DWT compression with a chaotic encryption stream.
>
> The result is one pipeline: shrink the images, stack them into a cube, then encrypt the cube.
>
> I'll cover the problem, the two tools, and the overall pipeline. Maria will cover the algorithm details and results.

**Delivery cue:** Slow start. Make eye contact before "one pipeline."

## Slide 2 - Problem (1:00)

**On-screen:** Image batches are big and exposed.

**Script**

> Start with the problem.
>
> A color image is not one grid. It is three grids: red, green, and blue.
>
> A 512 by 512 image has 786 thousand pixel values. [pause]
>
> Now send ten images, or a medical scan batch, or frames from several cameras.
>
> The bandwidth problem grows fast.
>
> The privacy problem is separate. If someone intercepts raw pixels, they see the image.
>
> The paper tries to handle both problems together.

**Delivery cue:** Do not rush the number. Let 786 thousand land.

## Slide 3 - Two tools (1:05)

**On-screen:** DWT and chaos.

**Script**

> The first tool is DWT, the Discrete Wavelet Transform.
>
> For each color channel, DWT splits the image into four bands.
>
> The LL band keeps the rough visual content, at half the width and half the height.
>
> So LL alone is one quarter of the original area. [pause]
>
> The second tool is chaos.
>
> It looks random, but the same starting key always produces the same stream.
>
> That stream drives the encryption.

**Delivery cue:** Say "DWT" slowly the first time. Same for "chaos."

## Slide 4 - Novelty (0:55)

**On-screen:** One cube. One encryption pass.

**Script**

> Here is the actual novelty. [pause]
>
> The older pattern is one image, one encryption run.
>
> This paper does something cleaner.
>
> It DWT-compresses every image first, keeps the LL bands, and stacks those bands into one cube.
>
> Then it encrypts the cube once.
>
> Different image sizes still fit because smaller images get zero padding.
>
> That padding is useful, but it is also the main limitation.

**Delivery cue:** Pause after "actual novelty." This is the slide the instructor needs to remember.

## Slide 5 - Pipeline and handoff (1:05)

**On-screen:** DWT, stack, confuse, diffuse.

**Script**

> The pipeline has four stages.
>
> First, DWT compression keeps the LL bands.
>
> Second, those bands are stacked into cube C.
>
> Third, confusion moves pixel positions inside the cube.
>
> Fourth, diffusion changes the pixel values with XOR and chaotic streams.
>
> The transmitted object is not a normal image. It is cipher cube D. [pause]
>
> Maria, over to you.

**Delivery cue:** Count the four stages with your hand. On the handoff, step back and pass the clicker.

## If you are running long

- Slide 2: cut the examples after "ten images."
- Slide 3: cut "rough visual content."
- Slide 4: cut the padding sentence and leave it for Maria.

## Memorize exactly

1. "Here is the actual novelty."
2. "Then it encrypts the cube once."
3. "Maria, over to you."

## Likely Q&A for Abdul

- Why DWT, not DCT?
- Why does LL save space?
- What is the cube?
- What happens with different image sizes?

Use [[../06 - Q&A and Rehearsal|Q&A and Rehearsal]] for full answers.

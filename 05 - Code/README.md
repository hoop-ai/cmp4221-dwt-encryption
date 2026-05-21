---
sticker: emoji//1f4bb
tags:
  - code
  - implementation
---
# Code Folder — README

> Python implementations of every algorithm in the paper. **You don't need to run these.** They exist so you can read them and understand the algorithms concretely. Code is often clearer than equations.

> **For the talk:** the prof did NOT ask for code. If asked *"have you implemented this?"*, say: *"No, we haven't implemented it for grading — we wrote reference implementations as study material to make sure we understood the algorithms."*

---

## What's in this folder

| File | What it implements |
|---|---|
| [chaotic_map.py](chaotic_map.py) | The 3D chaotic map iteration + quantization |
| [dwt_compress.py](dwt_compress.py) | DWT compression (image → LL sub-band) + reconstruction |
| [encrypt_decrypt.py](encrypt_decrypt.py) | Full confusion + diffusion pipeline (encrypt + decrypt) |
| [Code Walkthrough.md](Code%20Walkthrough.md) | Line-by-line explanation of all three files |

---

## Reading order

1. **[Code Walkthrough.md](Code%20Walkthrough.md)** — read this first; it explains everything below in plain English.
2. **[chaotic_map.py](chaotic_map.py)** — the simplest file; sets up the random sequences.
3. **[dwt_compress.py](dwt_compress.py)** — DWT compression on its own.
4. **[encrypt_decrypt.py](encrypt_decrypt.py)** — puts it all together.

---

## If you want to actually run these

You'll need Python 3.10+ and these packages:

```powershell
pip install numpy pillow pywavelets
```

Then from this folder:

```powershell
python encrypt_decrypt.py
```

This will:
1. Load a sample image (any 256×256 PNG in this folder, or generate a test pattern).
2. DWT-compress it.
3. Encrypt with confusion + diffusion.
4. Decrypt.
5. Save plaintext / cipher / recovered images side-by-side.

---

## Disclaimer

These implementations are **for educational reading only**. They are NOT:
- Cryptographically reviewed.
- Tested against the paper's exact equation forms (some details — like the body of Equation 1 — live in figures we don't have).
- Optimized for speed.
- Tested for correctness against the paper's reference PSNR / NPCR numbers.

The algorithm structure matches the paper. The exact chaotic-map equation is approximated with a plausible 3-variable map (Hénon-like generalization). If the prof asks: *"This is our study implementation — we used a 3-variable map as a stand-in for the paper's Equation 1 since the exact form was in a figure rather than the prose."*

---

## What you should be able to do after reading this folder

- Explain **in pseudo-code** how to compute LL from an image and reconstruct the image from LL alone.
- Explain **the loop structure** of confusion (per-pixel comparison + swap).
- Explain **the chaining structure** of diffusion (`V'(n) = V(n) XOR keystream XOR V'(n-1)`).
- Explain **why decryption uses the exact same XOR**.

If you can do all four, you understand the algorithms well enough to defend any methodology question.

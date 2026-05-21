---
sticker: emoji//269c
tags:
  - concept
  - xor
  - cipher
  - cryptography
---
# Concept 05 — XOR Cipher

> What XOR is, why it's the universal building block of encryption, and how the paper uses it.

---

## What is XOR?

**XOR (exclusive OR)** is a bitwise operation that returns 1 if the two input bits are **different**, and 0 if they're the **same**.

Truth table:

| A | B | A XOR B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

For multi-bit values (like a byte), XOR is applied to each pair of bits independently:

```
  1 0 1 1 0 1 0 0     ← byte A (180 in decimal)
^ 0 1 1 0 1 0 1 1     ← byte B (107 in decimal)
─────────────────
  1 1 0 1 1 1 1 1     ← A XOR B (223 in decimal)
```

In Python: `180 ^ 107 == 223`.

---

## The magic property: XOR is its own inverse

```
A XOR B XOR B == A
```

If you XOR a value with `B`, then XOR the result with `B` again, you get the original value back.

Proof:
- `A XOR B XOR B = A XOR (B XOR B) = A XOR 0 = A`

This is the **only** reason XOR is the universal cipher building block. Encryption and decryption use exactly the same operation. No need for a separate "decrypt" function.

---

## The simplest XOR cipher (one-time pad)

The **one-time pad** is the only cipher that is mathematically proven unbreakable:

- Generate a truly random key as long as the message.
- XOR the message with the key → ciphertext.
- Receiver XORs ciphertext with the same key → original message.

```python
# Encrypt
message = b"HELLO"
key     = b"\x37\xA1\xC4\x09\x5F"  # random bytes
cipher  = bytes(m ^ k for m, k in zip(message, key))

# Decrypt
recovered = bytes(c ^ k for c, k in zip(cipher, key))
assert recovered == message
```

This is unbreakable if and only if:
1. The key is **truly random**.
2. The key is **as long as the message**.
3. The key is **used only once**.

In practice these conditions are hard to meet (sharing huge keys is hard, true randomness is hard, key reuse is tempting). So real systems use **pseudo-random key streams** instead — derived from a small secret key.

---

## The paper's variant: XOR with a chaotic stream + chaining

The paper's diffusion step is:

```
V'(0) = V(0) XOR seed                       # first pixel
V'(n) = V(n) XOR keystream(n) XOR V'(n-1)   # all subsequent pixels
```

Where `keystream(n)` is from the chaotic map's output.

Three things are happening at once:

### 1. XOR with chaotic stream (replaces one-time pad)

`V(n) XOR keystream(n)` is the standard "stream cipher" pattern. The chaotic map provides a long pseudo-random `keystream` from a tiny key (the 9 chaotic parameters), avoiding the one-time pad's key-distribution problem.

### 2. XOR with previous encrypted pixel (chaining)

`XOR V'(n−1)` is the chaining trick. It makes every output depend on every previous output. This is why a single bit change at pixel 0 cascades to change every pixel after it. (See [Avalanche effect in `04 - Confusion and Diffusion.md`](04%20-%20Confusion%20and%20Diffusion.md#the-avalanche-effect-why-chaining-matters).)

This pattern is called **Cipher Block Chaining (CBC)** in traditional cryptography. The paper applies a CBC-like structure at the pixel level.

### 3. Three different streams (cycled by n mod 3)

Instead of one chaotic stream, the paper has three (`X2, Y2, Z2`). For pixel `n`, it picks one of them based on `n mod 3`. This cycles through all three streams in a deterministic order.

Why? More variety in the keystream pattern. An attacker who somehow figured out one stream still wouldn't know what's happening at the other 2/3 of pixels.

---

## Why XOR and not addition/multiplication?

You could in theory do `cipher_pixel = plain_pixel + keystream_pixel mod 256` instead of XOR. Why doesn't the paper?

| Property | XOR | Addition mod 256 | Multiplication mod 256 |
|---|---|---|---|
| Self-inverse | Yes (same op for enc/dec) | No (need to subtract) | No (need modular inverse) |
| Bit-level mixing | Yes (every bit independent) | No (carry bits couple) | No (carry bits couple) |
| Speed | 1 CPU instruction | 1 instruction (but needs mod) | Slow (mod inverse) |
| Symmetry | Perfect | Asymmetric | Asymmetric |
| Distribution if keystream is uniform | Perfect (output uniform) | Mostly uniform | Distorted |

XOR is the obvious choice for stream-cipher-style encryption. The paper picks XOR for **standard reasons** — speed, self-inverse, perfect mixing.

---

## XOR worked example (with actual numbers)

Let's encrypt a 4-pixel mini-vector using the paper's pattern.

**Setup:**
- `V = [120, 200, 50, 175]` (plaintext pixel values 0-255)
- `keystream = [88, 13, 222, 91]` (from chaotic map)
- `seed = 42` (from chaotic map's first value)

**Encryption:**

```
V'(0) = V(0) XOR seed
       = 120 XOR 42
       = 82                                  ← first cipher pixel

V'(1) = V(1) XOR keystream(1) XOR V'(0)
       = 200 XOR 13 XOR 82
       = 219                                 ← second cipher pixel

V'(2) = V(2) XOR keystream(2) XOR V'(1)
       = 50 XOR 222 XOR 219
       = 35                                  ← third

V'(3) = V(3) XOR keystream(3) XOR V'(2)
       = 175 XOR 91 XOR 35
       = 199                                 ← fourth
```

Cipher: `[82, 219, 35, 199]`.

**Decryption** (run in reverse, last pixel first):

```
V(3) = V'(3) XOR keystream(3) XOR V'(2)
      = 199 XOR 91 XOR 35
      = 175 ✓

V(2) = V'(2) XOR keystream(2) XOR V'(1)
      = 35 XOR 222 XOR 219
      = 50 ✓

V(1) = V'(1) XOR keystream(1) XOR V'(0)
      = 219 XOR 13 XOR 82
      = 200 ✓

V(0) = V'(0) XOR seed
      = 82 XOR 42
      = 120 ✓
```

Notice decryption uses **exactly the same XOR operation** as encryption. That's the self-inverse property at work.

---

## Common student misconceptions

### "XOR is weak."

XOR by itself with a *repeating* key is weak (you can break it with frequency analysis). XOR with a *long, random-looking* keystream — like a chaotic sequence — is exactly the basis of stream ciphers like ChaCha20, and the security depends entirely on the keystream's unpredictability.

### "Why not just hash the key?"

A hash is one-way — you can't recover the plaintext from `hash(key, plaintext)`. XOR is reversible, which is what you need for symmetric encryption.

### "XOR is insecure because it's linear."

XOR is indeed linear. The non-linearity in the paper's scheme comes from the **chaotic map** (which is highly nonlinear) generating the keystream, and from the **9 confusion cases** in Equation 10 (which are conditional logic, not linear arithmetic). XOR is just the final mixing operation — the security comes from what feeds into it.

---

## What to remember for the talk

1. **XOR is its own inverse:** `A XOR B XOR B = A`. Encryption and decryption use the same operation.
2. The paper's diffusion = **XOR with chaotic keystream + XOR with previous encrypted pixel** (chaining).
3. **Chaining is the avalanche source** — a single-bit input change ripples through the rest of the cipher.
4. Three chaotic streams are cycled through (`n mod 3`) for extra unpredictability.
5. XOR is picked over addition/multiplication because it's **self-inverse, bit-level, and one CPU instruction**.

---

## If asked: "Why XOR over modular addition?"

> *"Three reasons. First, XOR is its own inverse — encryption and decryption are the same operation, no need for a separate decrypt routine. Second, XOR operates bit-by-bit with no carry, so the keystream's randomness affects every bit independently. Third, it's one CPU instruction. Modular addition would also work but you'd need a separate subtraction for decryption and you'd lose the bit-level independence."*

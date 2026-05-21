"""
Full encrypt / decrypt pipeline: confusion + diffusion on the plaintext cube.

This puts together chaotic_map.py and dwt_compress.py to implement the paper's
end-to-end scheme. Read Code Walkthrough.md alongside this file.

Reference: Xu, Gao, Cao, Mou (2026), Sections 4.1.2, 4.1.3, 4.2.
"""

from __future__ import annotations

import numpy as np

from chaotic_map import (
    make_keystream_byte,
    make_offset_sequences,
)
from dwt_compress import (
    dwt_compress_image,
    dwt_decompress_image,
    stack_into_cube,
)


# -----------------------------------------------------------------------------
# Confusion (Section 4.1.2)
# -----------------------------------------------------------------------------


def confusion_encrypt(cube: np.ndarray, S1: np.ndarray, T1: np.ndarray, U1: np.ndarray) -> np.ndarray:
    """Scramble pixel positions in the cube using the chaotic offsets.

    Implements the 9-case swap rule from Equation 10 of the paper:
      - i > S1(k), j > T1(k), k > U1(k): swap with (i+S1, j+T1, k+U1)
      - i < S1(k), j < T1(k), k < U1(k): swap with (|i-S1|, |j-T1|, |k-U1|)
      - other 7 mixed cases: swap each coordinate by its own rule

    Pixel VALUES are unchanged -- only POSITIONS move.
    """
    M_h, M_w, M_d = cube.shape
    out = cube.copy()
    for k in range(M_d):
        s, t, u = S1[k], T1[k], U1[k]
        for i in range(M_h):
            for j in range(M_w):
                # New position from the 3 per-coordinate rules.
                ni = (i + s) % M_h if i > s else (abs(i - s) if i < s else i)
                nj = (j + t) % M_w if j > t else (abs(j - t) if j < t else j)
                nk = (k + u) % M_d if k > u else (abs(k - u) if k < u else k)
                # Swap the pixel pair.
                out[i, j, k], out[ni, nj, nk] = out[ni, nj, nk], out[i, j, k]
    return out


def confusion_decrypt(cube: np.ndarray, S1: np.ndarray, T1: np.ndarray, U1: np.ndarray) -> np.ndarray:
    """Inverse of confusion: walk in REVERSE order and undo each swap.

    Because each swap is its own inverse, we just iterate backwards.
    """
    M_h, M_w, M_d = cube.shape
    out = cube.copy()
    for k in reversed(range(M_d)):
        s, t, u = S1[k], T1[k], U1[k]
        for i in reversed(range(M_h)):
            for j in reversed(range(M_w)):
                ni = (i + s) % M_h if i > s else (abs(i - s) if i < s else i)
                nj = (j + t) % M_w if j > t else (abs(j - t) if j < t else j)
                nk = (k + u) % M_d if k > u else (abs(k - u) if k < u else k)
                out[i, j, k], out[ni, nj, nk] = out[ni, nj, nk], out[i, j, k]
    return out


# -----------------------------------------------------------------------------
# Diffusion (Section 4.1.3)
# -----------------------------------------------------------------------------


def diffusion_encrypt(cube: np.ndarray, keystream: np.ndarray, seed: int) -> np.ndarray:
    """XOR each pixel with chaos + previous output (chaining = avalanche).

    Implements Equations 12-13 of the paper:
      V'(0) = V(0) XOR seed
      V'(n) = V(n) XOR keystream(n) XOR V'(n-1)

    The XOR with V'(n-1) is what gives the scheme its avalanche property:
    a single-bit change at the start cascades to every subsequent pixel.
    """
    shape = cube.shape
    V = cube.flatten().astype(np.uint8)
    V_prime = np.zeros_like(V)

    V_prime[0] = V[0] ^ np.uint8(seed)
    for n in range(1, len(V)):
        V_prime[n] = V[n] ^ keystream[n] ^ V_prime[n - 1]
    return V_prime.reshape(shape)


def diffusion_decrypt(cube: np.ndarray, keystream: np.ndarray, seed: int) -> np.ndarray:
    """Inverse of diffusion: same XORs (XOR is self-inverse), reverse order.

    Implements Equations 14-15 of the paper:
      V(n) = V'(n) XOR keystream(n) XOR V'(n-1)   for n > 0
      V(0) = V'(0) XOR seed
    """
    shape = cube.shape
    V_prime = cube.flatten().astype(np.uint8)
    V = np.zeros_like(V_prime)

    # Walk from the END so V'(n-1) is the original cipher value, not the recovered one.
    for n in range(len(V_prime) - 1, 0, -1):
        V[n] = V_prime[n] ^ keystream[n] ^ V_prime[n - 1]
    V[0] = V_prime[0] ^ np.uint8(seed)
    return V.reshape(shape)


# -----------------------------------------------------------------------------
# End-to-end pipeline
# -----------------------------------------------------------------------------


def encrypt_pipeline(plaintext_images: list[np.ndarray]) -> tuple[np.ndarray, dict]:
    """Full encryption: images -> DWT-compressed cube -> cipher cube.

    Returns the cipher cube + metadata needed for decryption (cube shape, etc.).
    """
    # Stage 1: DWT-compress each image.
    compressed = [dwt_compress_image(img) for img in plaintext_images]

    # Stage 2: stack into one cube.
    cube_C = stack_into_cube(compressed)
    M_h, M_w, M_d = cube_C.shape
    n_pixels = M_h * M_w * M_d

    # Stage 3: confusion (scramble positions).
    S1, T1, U1 = make_offset_sequences(M_h, M_w, M_d)
    cube_Cprime = confusion_encrypt(cube_C, S1, T1, U1)

    # Stage 4: diffusion (XOR values with chaining).
    keystream = make_keystream_byte(n_pixels)
    cipher_cube = diffusion_encrypt(cube_Cprime, keystream, seed=int(keystream[0]))

    metadata = {
        "cube_shape": cube_C.shape,
        "original_shapes": [img.shape for img in plaintext_images],
    }
    return cipher_cube, metadata


def decrypt_pipeline(cipher_cube: np.ndarray, metadata: dict) -> list[np.ndarray]:
    """Full decryption: cipher cube -> plaintext images.

    The key (chaotic parameters + initial values) is implicit in the imports
    of make_offset_sequences and make_keystream_byte -- they use the same
    defaults. In a real system, you'd pass the key explicitly.
    """
    M_h, M_w, M_d = metadata["cube_shape"]
    n_pixels = M_h * M_w * M_d

    # Stage 4 inverse: diffusion undo.
    keystream = make_keystream_byte(n_pixels)
    cube_Cprime = diffusion_decrypt(cipher_cube, keystream, seed=int(keystream[0]))

    # Stage 3 inverse: confusion undo.
    S1, T1, U1 = make_offset_sequences(M_h, M_w, M_d)
    cube_C = confusion_decrypt(cube_Cprime, S1, T1, U1)

    # Stages 2 + 1 inverse: unstack and inverse-DWT each image.
    recovered_images = []
    layer = 0
    for orig_shape in metadata["original_shapes"]:
        h, w, _ = orig_shape
        compressed = np.zeros((h // 2, w // 2, 3), dtype=np.uint8)
        for c in range(3):
            compressed[:, :, c] = cube_C[: h // 2, : w // 2, layer]
            layer += 1
        recovered = dwt_decompress_image(compressed)
        recovered_images.append(recovered)
    return recovered_images


if __name__ == "__main__":
    print("End-to-end pipeline demo")
    print("=" * 60)

    # Make two test images.
    img1 = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)
    img2 = np.random.randint(0, 256, (128, 128, 3), dtype=np.uint8)

    print(f"Input: 2 images of shape {img1.shape}")
    cipher, meta = encrypt_pipeline([img1, img2])
    print(f"Cipher cube shape: {cipher.shape}")
    print(f"Cipher pixel range: [{cipher.min()}, {cipher.max()}]")

    recovered = decrypt_pipeline(cipher, meta)
    print(f"Recovered: {len(recovered)} images")

    # PSNR check on each recovered image.
    for i, (orig, rec) in enumerate(zip([img1, img2], recovered)):
        mse = np.mean((orig.astype(np.float64) - rec.astype(np.float64)) ** 2)
        psnr = 10 * np.log10(255**2 / mse) if mse > 0 else float("inf")
        print(f"Image {i+1}: PSNR = {psnr:.2f} dB (paper avg: 32.06 dB on natural images)")

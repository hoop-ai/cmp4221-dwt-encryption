"""
DWT compression: image -> LL sub-band -> reconstruction.

Uses PyWavelets' Haar wavelet, the simplest DWT basis. The paper doesn't
specify which wavelet family it uses; Haar gives the cleanest illustration.

Reference: Xu, Gao, Cao, Mou (2026), Section 4.1.1.
"""

from __future__ import annotations

import numpy as np
import pywt


def dwt_compress_channel(channel: np.ndarray) -> np.ndarray:
    """Apply one-level DWT to a single channel; return only the LL sub-band.

    Input:  H x W array, dtype float or uint8.
    Output: (H/2) x (W/2) array.

    This is the 'compress to 1/4 size' step from Equation 4 of the paper:
    the channel is split into LL, LH, HL, HH; only LL is kept.
    """
    channel_f = channel.astype(np.float64)
    LL, (LH, HL, HH) = pywt.dwt2(channel_f, "haar")
    # Discard LH, HL, HH -- these are the 3/4 of data being thrown away.
    return LL


def dwt_decompress_channel(LL: np.ndarray) -> np.ndarray:
    """Reconstruct a channel from its LL sub-band, using zeros for LH/HL/HH.

    Input:  (H/2) x (W/2) array.
    Output: H x W array.

    Because LH, HL, HH were thrown away in compression, we substitute zeros
    here. This is the lossy half of the round trip -- recovered image is
    visually close but not pixel-perfect (the paper measures this as PSNR 32.06 dB).
    """
    zeros = np.zeros_like(LL)
    reconstructed = pywt.idwt2((LL, (zeros, zeros, zeros)), "haar")
    return np.clip(reconstructed, 0, 255).astype(np.uint8)


def dwt_compress_image(image_rgb: np.ndarray) -> np.ndarray:
    """Compress an RGB image: each channel independently DWT-compressed to LL.

    Input:  H x W x 3 array, uint8.
    Output: (H/2) x (W/2) x 3 array.

    This handles the 'three channels R, G, B are separated' step from
    Section 4.1.1, Step 1.
    """
    R = dwt_compress_channel(image_rgb[:, :, 0])
    G = dwt_compress_channel(image_rgb[:, :, 1])
    B = dwt_compress_channel(image_rgb[:, :, 2])
    return np.stack([R, G, B], axis=-1)


def dwt_decompress_image(LL_rgb: np.ndarray) -> np.ndarray:
    """Reconstruct an RGB image from its compressed (LL-only) form."""
    R = dwt_decompress_channel(LL_rgb[:, :, 0])
    G = dwt_decompress_channel(LL_rgb[:, :, 1])
    B = dwt_decompress_channel(LL_rgb[:, :, 2])
    return np.stack([R, G, B], axis=-1)


def stack_into_cube(compressed_images: list[np.ndarray]) -> np.ndarray:
    """Equation 5 of the paper: stack all LL sub-bands into one 3D cube.

    Input:  list of (h_n/2) x (w_n/2) x 3 arrays of varying sizes.
    Output: M_h x M_w x N_layers array.

    Smaller images are zero-padded to fit the cube cross-section, which is
    sized to the largest input image. This is the paper's main limitation
    (zero-padding wastes space).
    """
    if not compressed_images:
        raise ValueError("Need at least one compressed image")

    # Find cube cross-section dimensions (largest image's compressed size).
    M_h = max(img.shape[0] for img in compressed_images)
    M_w = max(img.shape[1] for img in compressed_images)

    # Stack each RGB channel of each image as a separate cube layer.
    layers = []
    for img in compressed_images:
        for c in range(3):
            channel = img[:, :, c]
            padded = np.zeros((M_h, M_w), dtype=np.uint8)
            padded[: channel.shape[0], : channel.shape[1]] = channel.astype(np.uint8)
            layers.append(padded)
    cube = np.stack(layers, axis=-1)
    return cube


if __name__ == "__main__":
    # Quick demo: generate a 256x256 test pattern, compress, decompress.
    h, w = 256, 256
    test_img = np.zeros((h, w, 3), dtype=np.uint8)
    test_img[:, :, 0] = np.tile(np.linspace(0, 255, w, dtype=np.uint8), (h, 1))
    test_img[:, :, 1] = np.tile(np.linspace(0, 255, h, dtype=np.uint8).reshape(-1, 1), (1, w))
    test_img[:, :, 2] = 128

    print(f"Original: {test_img.shape}, dtype={test_img.dtype}")
    compressed = dwt_compress_image(test_img)
    print(f"Compressed (LL only): {compressed.shape} -- 1/4 the pixel count")
    recovered = dwt_decompress_image(compressed)
    print(f"Recovered: {recovered.shape}")
    mse = np.mean((test_img.astype(np.float64) - recovered.astype(np.float64)) ** 2)
    psnr = 10 * np.log10(255**2 / mse) if mse > 0 else float("inf")
    print(f"PSNR after round trip: {psnr:.2f} dB (paper reports avg 32.06 dB on natural images)")

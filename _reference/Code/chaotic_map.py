"""
3D discrete chaotic map for the DWT-encryption paper.

This is a study implementation. The paper's Equation 1 (the exact chaotic-map
form) lives inside a figure that we don't have access to verbatim. We use a
plausible 3-variable generalisation of the Hénon map here. The structure --
iterated state vector, burn-in, quantization -- matches the paper's design.

Reference: Xu, Gao, Cao, Mou (2026), Section 2 and Section 3.1.
"""

from __future__ import annotations

import numpy as np


# Paper's published parameter values (Section 3.1, Step 1).
DEFAULT_PARAMS = {
    "a": 0.3,
    "b": 0.94,
    "c": 0.9,
    "d": 1.6,
    "e": -1.8,
    "f": -1.8,
}
DEFAULT_INIT = (0.1, 0.1, 0.1)

# Paper's burn-in length (Section 3.1, Step 2).
BURN_IN = 125_000


def chaotic_step(x: float, y: float, z: float, p: dict[str, float]) -> tuple[float, float, float]:
    """One iteration of a 3-variable discrete chaotic map.

    The paper's Equation 1 isn't given symbolically in the prose, so this is a
    Hénon-like 3D generalisation that produces the same kind of chaotic
    behaviour: coupled nonlinear updates with parameter-controlled mixing.
    """
    x_new = 1.0 - p["a"] * x * x + p["b"] * y
    y_new = p["c"] * x + p["d"] * z
    z_new = p["e"] * y + p["f"] * np.sin(x)
    return x_new, y_new, z_new


def iterate_map(
    n_samples: int,
    params: dict[str, float] | None = None,
    init: tuple[float, float, float] | None = None,
    burn_in: int = BURN_IN,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Iterate the chaotic map and return three sequences X, Y, Z.

    Steps:
      1. Run burn-in iterations to push the trajectory onto the attractor.
      2. Then run n_samples more iterations, collecting (x, y, z) at each step.
    """
    p = params or DEFAULT_PARAMS
    x, y, z = init or DEFAULT_INIT

    # Burn-in (Step 2 of Section 3.1) -- 1.25e5 iterations of throwaway state.
    for _ in range(burn_in):
        x, y, z = chaotic_step(x, y, z, p)

    # Sample n_samples values into three arrays.
    X = np.zeros(n_samples, dtype=np.float64)
    Y = np.zeros(n_samples, dtype=np.float64)
    Z = np.zeros(n_samples, dtype=np.float64)
    for i in range(n_samples):
        x, y, z = chaotic_step(x, y, z, p)
        X[i] = x
        Y[i] = y
        Z[i] = z
    return X, Y, Z


def quantize_to_range(seq: np.ndarray, modulus: int, decimals: int = 14) -> np.ndarray:
    """Equation 3 of the paper: convert real-valued chaos to integer values.

    Take absolute value, shift decimals to integer part, take mod.
    Result: integers in [0, modulus-1].
    """
    shifted = np.abs(seq) * (10**decimals)
    return np.floor(shifted).astype(np.int64) % modulus


def make_keystream_byte(n_samples: int, seed_init: tuple[float, float, float] | None = None) -> np.ndarray:
    """Generate an n-byte keystream (values 0-255) for XOR diffusion."""
    X, _, _ = iterate_map(n_samples, init=seed_init)
    return quantize_to_range(X, modulus=256).astype(np.uint8)


def make_offset_sequences(
    cube_h: int,
    cube_w: int,
    cube_d: int,
    seed_init: tuple[float, float, float] | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate three offset sequences S1, T1, U1 for confusion.

    Each value lies in the valid coordinate range for its axis.
    """
    n = cube_h * cube_w * cube_d
    X, Y, Z = iterate_map(n, init=seed_init)
    S1 = quantize_to_range(X, cube_h)
    T1 = quantize_to_range(Y, cube_w)
    U1 = quantize_to_range(Z, cube_d)
    return S1, T1, U1


if __name__ == "__main__":
    # Quick sanity check: generate a few sequence values.
    X, Y, Z = iterate_map(10)
    print("First 5 chaotic samples (X, Y, Z):")
    for i in range(5):
        print(f"  step {i}: x={X[i]:+.6f}, y={Y[i]:+.6f}, z={Z[i]:+.6f}")

    print("\nQuantized to bytes (first 10):")
    keystream = make_keystream_byte(10)
    print(" ", keystream.tolist())

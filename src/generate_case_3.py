import numpy as np

# Base rows (look normal)
A = np.array([
    [1.10e3,  2.05e4,  3.01e5,  4.07e6,  5.02e7],
    [2.20e3,  4.10e4,  6.02e5,  8.14e6,  1.004e8],
    [3.30e3,  6.15e4,  9.03e5,  1.221e7, 1.506e8],
    [1.00e12, 1.95e12, 2.90e12, 3.85e12, 4.80e12],
], dtype=np.float64)

# Create row 5 by floating‑point operations that *should* make it distinct,
# but rounding pushes it back onto row 4 numerically.
row4 = A[3]

# Masked near‑dependency: multiply by a factor extremely close to 1,
# then add and subtract large values that cancel out in float64.
row5 = (row4 * 1.0000000000000001) + 1e5 - 1e5

A = np.vstack([A, row5])

b = np.array([1., 2., 3., 4., 5.], dtype=np.float64)

# save to file
np.save('A3.npy',A)
np.save('b3.npy',b)

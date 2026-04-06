import numpy as np


x = np.array([1, 2, 3])
y = np.array([40, 42, 45])


A = np.vstack([x, np.ones(len(x))]).T


theta, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

a, b = theta

print(f"Matrix A:\n{A}")
print(f"Vector y: {y}")
print(f"Computed a (slope): {a:.2f}")
print(f"Computed b (intercept): {b:.2f}")
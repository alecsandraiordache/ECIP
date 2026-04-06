import numpy as np


time_data = np.array([1, 2, 3])
y = np.array([40, 42, 45])


A = np.vstack([time_data, np.ones(len(time_data))]).T


x_params, residuals_lstsq, rank, s = np.linalg.lstsq(A, y, rcond=None)

print(f"Found parameters (a, b): {x_params}\n")


predicted_values = A @ x_params

print("1. Predicted values (Ax):")
print(predicted_values)


r = y - predicted_values

print("2. Residual (r = y - Ax):")
print(r)


squared_error = np.sum(r**2)

print("3. Squared error:")
print(f"{squared_error:.4f}")
#sensor 1 = [1,2]
#sensor2 = [3,4]
#build matrix A
# check independence of columns
#explain why system fails

import numpy as np


sensor1 = [1, 2]
sensor2 = [3, 4]


A = np.column_stack((sensor1, sensor2))

print("Matrix A:")
print(A)


det = np.linalg.det(A)

print(f"Determinant: {det:.2f}")


if np.abs(det) < 1e-9:  
    print("Conclusion: Determinant is 0. Columns are DEPENDENT. System FAILS (singular matrix).")
else:
    print("Conclusion: Determinant is not 0. Columns are INDEPENDENT. System DOES NOT fail.")
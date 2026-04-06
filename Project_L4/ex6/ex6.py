#error: [-1, 2, -2]
#compute squared error
#compare with absolute error
#explain impact on decisions

import numpy as np


errors = np.array([-1, 2, -2])


squared_errors = errors ** 2
sum_squared_error = np.sum(squared_errors)


absolute_errors = np.abs(errors)
sum_absolute_error = np.sum(absolute_errors)

print(f"Individual Squared Errors: {squared_errors}")
print(f"Total Squared Error (SSE): {sum_squared_error}\n")

print(f"Individual Absolute Errors: {absolute_errors}")
print(f"Total Absolute Error (SAE): {sum_absolute_error}")
#generate gaussian random variable with mean = 0, std = 1
#plot histogram
#compare with uniform distribution 

import numpy as np
import matplotlib.pyplot as plt

n_samples = 10000
np.random.seed(42)

gaussian_data = np.random.normal(loc=0.0, scale=1.0, size=n_samples)


uniform_data = np.random.uniform(low=-3.0, high=3.0, size=n_samples)


plt.figure(figsize=(10, 6))


plt.hist(gaussian_data, bins=50, alpha=0.6, color='dodgerblue', edgecolor='black', 
         density=True, label='Gaussian (mean=0, std=1)')


plt.hist(uniform_data, bins=50, alpha=0.5, color='orange', edgecolor='black', 
         density=True, label='Uniform (range: -3 to 3)')


plt.title('Task 5: Gaussian vs. Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)

"""
Comparison: Gaussian vs. Uniform Distribution

1. Shape: 
   - Gaussian (Blue): Forms a classic "bell curve", peaking perfectly at the mean (0).
   - Uniform (Orange): Forms a flat rectangle, showing no central peak.

2. Concentration of Data:
   - Gaussian: Data is heavily concentrated near the center. About 68% of the values 
     fall within exactly one standard deviation (-1 to 1).
   - Uniform: Data is spread out completely evenly. A value near 0 is just as likely 
     as a value near 2.9.

3. Tails / Boundaries:
   - Gaussian: Has fading "tails". It can theoretically produce values out to infinity, 
     though extreme values become exponentially rare.
   - Uniform: Has strict, absolute cut-offs. In this dataset, it will never produce a 
     number lower than -3 or higher than 3.
"""


plt.show()
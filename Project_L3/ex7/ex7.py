#Simulate true value x = 10
#generate measurements y = x+noise
#plot measurement distribution 

import numpy as np
import matplotlib.pyplot as plt

n_samples = 10000
np.random.seed(42)

true_x = 10.0

noise_std = 2.0
noise = np.random.normal(loc=0.0, scale=noise_std, size=n_samples)

measurements_y = true_x + noise

plt.figure(figsize=(10, 6))

plt.hist(measurements_y, bins=50, density=True, alpha=0.7, color='mediumpurple', edgecolor='black', label='Measurements (y)')

plt.axvline(x=true_x, color='red', linestyle='--', linewidth=3, label=f'True Value (x = {true_x})')

mean_y = np.mean(measurements_y)
plt.axvline(x=mean_y, color='gold', linestyle=':', linewidth=3, label=f'Mean of Measurements (~{mean_y:.2f})')

plt.title('Measurement Distribution: True Value + Noise')
plt.xlabel('Measured Value (y)')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)

"""
Discussion: True Value vs. Measurements

1. True Value (x): This is the exact, underlying state of the system we want 
   to know (x = 10.0). It is deterministic and constant.
   
2. Measurements (y): In the real world, sensors are imperfect. Every reading (y) 
   is a combination of the true value and random noise (y = x + noise).
   
3. Measurement Distribution: Because the noise is random (Gaussian), the 
   measurements form a bell curve centered around the true value. Some readings 
   are higher than 10, some are lower.
   
4. The Power of Averaging: If we only take one measurement, we might get 12.5 
   or 7.1, which is highly inaccurate. However, because the noise is centered 
   at 0 (zero-mean), taking many measurements and averaging them (the yellow 
   dotted line) brings us extremely close to the true value (the red dashed line).
"""

plt.show()
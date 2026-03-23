#generate gaussian noise with different variances
#plot and compute distribution
#discuss uncertainty 

import numpy as np
import matplotlib.pyplot as plt

n_samples = 10000
mean = 0.0  #

noise_low = np.random.normal(loc=mean, scale=0.5, size=n_samples)  
noise_mid = np.random.normal(loc=mean, scale=1.0, size=n_samples)  
noise_high = np.random.normal(loc=mean, scale=2.0, size=n_samples)


print(f"Computed Variance (Low): {np.var(noise_low):.4f}")
print(f"Computed Variance (Mid): {np.var(noise_mid):.4f}")
print(f"Computed Variance (High): {np.var(noise_high):.4f}")


plt.figure(figsize=(10, 6))


plt.hist(noise_low, bins=50, density=True, alpha=0.7, color='dodgerblue', label='Low Variance')
plt.hist(noise_mid, bins=50, density=True, alpha=0.6, color='mediumseagreen', label='Medium Variance')
plt.hist(noise_high, bins=50, density=True, alpha=0.5, color='salmon', label='High Variance')


plt.axvline(x=mean, color='black', linestyle='--', linewidth=2, label='Mean (0)')

plt.title('Gaussian Noise Distributions with Different Variances')
plt.xlabel('Noise Value')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)

"""
Discussion: Uncertainty in Gaussian Distributions

1. Variance as Uncertainty: In statistics and signal processing, variance is 
   the mathematical measure of uncertainty. A higher variance means the data 
   is more spread out and less predictable.
   
2. Low Variance (Blue): Represents low uncertainty. The data is tightly 
   packed around the mean (0) forming a tall, narrow peak. If this were a 
   sensor reading, we would be highly confident in the true value.
   
3. High Variance (Red): Represents high uncertainty. The data is widely 
   spread forming a short, wide bell. The peak is much lower because the 
   probability of getting a value close to the mean drops significantly. We 
   are very uncertain about the true value because the noise is so large.
"""

plt.show()
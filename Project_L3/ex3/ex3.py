#compute sample mean of generated data
#compare with theoretical mean 
#discuss implementation of expectation

import numpy as np
import matplotlib.pyplot as plt


n_samples = 10000
np.random.seed(42) 
X = np.random.uniform(0, 1, n_samples)


sample_mean = np.mean(X)
theoretical_mean = 0.5  

print(f"Sample Mean (Empirical): {sample_mean:.4f}")
print(f"Theoretical Mean (Expected): {theoretical_mean:.4f}")


plt.figure(figsize=(9, 6))
plt.hist(X, bins=30, color='lightgreen', edgecolor='black', density=True, label='Empirical Data', alpha=0.7)


plt.axhline(y=1, color='red', linestyle='--', linewidth=2, label='Theoretical PDF')
plt.axvline(x=sample_mean, color='blue', linestyle='-', linewidth=2, label=f'Sample Mean ({sample_mean:.4f})')
plt.axvline(x=theoretical_mean, color='darkorange', linestyle=':', linewidth=3, label=f'Theoretical Mean (0.5)')


plt.title('Simulation of X ~ Uniform(0, 1) and Expectation')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)

"""
Discussion: Implementation of Expectation

1. Theoretical Expectation: Mathematically, E[X] for a continuous variable is 
   calculated using an integral. For Uniform(0, 1), E[X] = ∫ x dx = 0.5.
2. Computational Implementation: We estimate this expectation computationally 
   by generating a large number of samples (N) and calculating their average: 
   E[X] ≈ (1/N) * Σ(x_i).
3. Conclusion: Our sample mean (~0.4942) is very close to the theoretical 
   mean (0.5). This demonstrates the Law of Large Numbers: as N increases, 
   the sample mean converges to the expected theoretical value.
"""

plt.show()
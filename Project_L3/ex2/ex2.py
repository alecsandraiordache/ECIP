#simulate a random variable X ~ Uniform (0,1)
#plot histogram
#interpret distribuțion shape

import numpy as np
import matplotlib.pyplot as plt


n_samples = 10000
X = np.random.uniform(0, 1, n_samples)


plt.figure(figsize=(8, 5))

plt.hist(X, bins=30, color='lightgreen', edgecolor='black', density=True, label='Empirical Data')


plt.axhline(y=1, color='red', linestyle='--', linewidth=2, label='Theoretical PDF')


plt.title('Simulation of X ~ Uniform(0, 1)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)

"""
Interpreting the Distribution Shape:

1. Theoretical Shape (Red Line): For X ~ Uniform(0, 1), any value between 0 and 1 
   is equally likely. The Probability Density Function (PDF) is a perfectly flat, 
   constant horizontal line at f(x) = 1.
2. Empirical Shape (Green Bars): The actual simulated data forms a roughly 
   rectangular shape that hugs the theoretical line, but the tops of the bars 
   are jagged.
3. Sampling Variability: The bars aren't perfectly flat due to randomness. In any 
   finite sample, natural statistical variance means some bins randomly catch slightly 
   more numbers than others.
4. Convergence: If you increase n_samples to a much larger number (e.g., 10,000,000), 
   the tops of the histogram bars will flatten out almost completely, converging 
   with the theoretical mathematical model.
"""


plt.show()
#generate two corelated random variables
#compute covariance
#interpret relationship

import numpy as np
import matplotlib.pyplot as plt

n_samples = 1000
np.random.seed(42)

x = np.random.normal(loc=0.0, scale=1.0, size=n_samples)

noise = np.random.normal(loc=0.0, scale=1.0, size=n_samples)
y = 2.0 * x + noise


cov_matrix = np.cov(x, y)
covariance_xy = cov_matrix[0, 1]

print(f"Covariance between X and Y: {covariance_xy:.4f}")


plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.5, color='teal', edgecolor='black')
plt.title(f'Correlated Random Variables (Covariance ≈ {covariance_xy:.2f})')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.grid(True, linestyle='--', alpha=0.7)

"""
Discussion: Interpreting Covariance and Relationships

1. Correlated Variables: We generated variable Y such that it mathematically 
   depends on variable X (Y = 2X + noise). Because of this dependency, they 
   are correlated. When X increases, Y tends to increase as well.

2. Visualizing the Relationship: The scatter plot shows a clear upward trend. 
   The points form a diagonal cloud moving from the bottom-left to the 
   top-right. This visual shape is the classic signature of a strong, 
   positive linear relationship.

3. Interpreting Covariance: 
   - Covariance is a statistical metric that indicates the extent to which 
     two variables change together.
   - Positive Covariance (like our result, ~1.95): Means the variables show 
     similar behavior. As X gets larger, Y gets larger.
   - Negative Covariance: Would mean they show opposite behavior (as X gets 
     larger, Y gets smaller).
   - Covariance Near Zero: Would mean the variables are completely independent 
     and form a scattered, shapeless cloud with no clear trend.
"""


plt.show()
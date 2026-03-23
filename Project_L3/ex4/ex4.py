#compute variance of generated data 
#analyze spread amound mean
#compare dataset with different variance 

import numpy as np
import matplotlib.pyplot as plt

n_samples = 10000
np.random.seed(42)


X_low_var = np.random.normal(loc=0.5, scale=0.1, size=n_samples)  
X_high_var = np.random.normal(loc=0.5, scale=0.3, size=n_samples) 


var_low = np.var(X_low_var)
var_high = np.var(X_high_var)

print(f"Low Variance Set  - Mean: {np.mean(X_low_var):.4f}, Variance: {var_low:.4f}")
print(f"High Variance Set - Mean: {np.mean(X_high_var):.4f}, Variance: {var_high:.4f}")


plt.figure(figsize=(10, 6))


plt.hist(X_low_var, bins=50, alpha=0.6, color='skyblue', edgecolor='black', 
         density=True, label=f'Low Variance (Var ≈ {var_low:.2f})')


plt.hist(X_high_var, bins=50, alpha=0.5, color='salmon', edgecolor='black', 
         density=True, label=f'High Variance (Var ≈ {var_high:.2f})')


plt.axvline(x=0.5, color='red', linestyle='--', linewidth=3, label='Shared Mean (0.5)')


plt.title('Comparing Data Spread: Low vs. High Variance')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(axis='y', alpha=0.75)

"""
Discussion: Variance and Spread Around the Mean

1. What is Variance? 
   Variance measures how far a set of numbers is spread out from their average 
   (mean). It is the average of the squared differences from the Mean.
2. Low Variance (Blue): 
   A small variance (~0.01) means the data points are tightly clustered right 
   around the mean. The histogram looks tall and narrow.
3. High Variance (Red): 
   A larger variance (~0.09) means the data is much more spread out. The 
   histogram looks shorter and wider, indicating higher unpredictability.
"""


plt.show()
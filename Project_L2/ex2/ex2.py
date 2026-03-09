#use your simulation to pint out at what value of R the population growth becomes chaotic
#show your resolt with a screenshot and plot it


import numpy as np
import matplotlib.pyplot as plt


n_r = 2000 
r_values = np.linspace(2.5, 4.0, n_r)

iterations = 1000
last_generations = 100

population = 1e-5 * np.ones(n_r)


x_points = []
y_points = []


for i in range(iterations):
    population = r_values * population * (1 - population)
    
    
    if i >= (iterations - last_generations):
        x_points.extend(r_values)
        y_points.extend(population)


plt.figure(figsize=(10, 6))


plt.scatter(x_points, y_points, s=0.1, color='black', alpha=0.25)


chaos_onset_r = 3.56995
plt.axvline(x=chaos_onset_r, color='red', linestyle='--', linewidth=1.5, 
            label=f'Onset of Chaos (R ≈ {chaos_onset_r:.2f})')

plt.title("Bifurcation Diagram: Transition to Chaos in Population Growth")
plt.xlabel("Growth Factor (R)")
plt.ylabel("Steady-State Population Fraction (P)")
plt.legend()
plt.tight_layout()


plt.show()
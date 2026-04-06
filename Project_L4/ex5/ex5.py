#data : energy vs time
# fit linear model
#interpret slope as consumption rate
#plot data and fitted line 

import numpy as np
import matplotlib.pyplot as plt

time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
energy = np.array([12.7, 14.9, 18.0, 19.7, 22.6, 24.6, 28.1, 29.8, 32.8, 34.9])


slope, intercept = np.polyfit(time, energy, 1)


consumption_rate = slope
print(f"Calculated slope (a): {slope:.4f}")
print(f"Calculated intercept (b): {intercept:.4f}")
print(f"-> INTERPRETATION: The energy consumption rate is {consumption_rate:.2f} kW.")


fitted_line = slope * time + intercept


plt.figure(figsize=(8, 5))


plt.scatter(time, energy, color='blue', s=60, label='Measured Data (Energy)', zorder=5)


plt.plot(time, fitted_line, color='red', linewidth=2.5, 
         label=f'Consumption Rate: y = {slope:.2f}x + {intercept:.2f}')


plt.title('Cumulative Energy vs Time\n(Slope represents Consumption Rate)')
plt.xlabel('Time (hours)')
plt.ylabel('Cumulative Energy (kWh)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)


plt.show()
#geerate noise obs : y(t) = x(t) + noise 
#use gaussian noise with mean 0 and standard deviation 2
#plot true state and observations on the same gra

import numpy as np
import matplotlib.pyplot as plt

t = 50

x = np.zeros(t)
x[0] = 0

for i in range(t - 1):
    x[i + 1] = x[i] + 1

noise = np.random.normal(0, 2, t)

y = x + noise

plt.figure()
plt.plot(range(t), x, label="True State x(t)")
plt.scatter(range(t), y, label="Observations y(t)", alpha=0.7)
plt.xlabel("Time step")
plt.ylabel("Value")
plt.title("True State vs Noisy Observations")
plt.legend()
plt.grid(True)
plt.show()
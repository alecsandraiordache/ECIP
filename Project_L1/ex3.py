#implemet a moving afverage estimator
#compute an estimated signal from noisy obs
#plot true state, noisy obs and estimated state

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

T = 50

x = np.zeros(T)
for t in range(T - 1):
    x[t + 1] = x[t] + 1

noise = np.random.normal(loc=0.0, scale=2.0, size=T)
y = x + noise

window = 5  
kernel = np.ones(window) / window
y_hat = np.convolve(y, kernel, mode="same") 

plt.figure()
plt.plot(x, label="True state x(t)")
plt.scatter(range(T), y, alpha=0.6, label="Noisy observations y(t)")
plt.plot(y_hat, linewidth=2, label=f"Moving average estimate (window={window})")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.title("True State vs Noisy Observations vs Moving Average Estimate")
plt.grid(True)
plt.legend()
plt.show()
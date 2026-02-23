#consider a simple system: x(t+1) = x(t) + 1
#generate the true state x(t) for 50 time steps
#plot the evolution of the true state 


import numpy as np
import matplotlib.pyplot as plt

t = 50

x = np.zeros(t)

x[0] = 0  

for i in range(t - 1):
    x[i + 1] = x[i] + 1

plt.figure()
plt.plot(range(t), x)
plt.xlabel("Time step")
plt.ylabel("State x(t)")
plt.title("Evolution of the True State")
plt.grid(True)
plt.show()
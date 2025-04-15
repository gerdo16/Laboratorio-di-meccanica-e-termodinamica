import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt('Dati1')

theta_i = data[:, 0]
dtheta_i = data[:, 1]
theta_i_primo = data[:, 2]
dtheta_i_primo = data[:, 3]

delta = theta_i + theta_i_primo - 45
print(delta)
delta = np.concatenate((delta, delta[::-1]))
print(delta)

theta = np.concatenate((theta_i, theta_i_primo[::-1]))
print(theta)

plt.figure(figsize=(10, 5))
plt.plot(theta, delta, 'o-', label='')
plt.xlabel(r'$\theta$ (°)')
plt.ylabel(r'$\delta$ (°)')
plt.title('Graph')
plt.grid(True)
plt.legend()
plt.show()



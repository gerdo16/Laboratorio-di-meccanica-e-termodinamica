import numpy as np
import matplotlib.pyplot as plt

dati = np.loadtxt('altezze.txt')

h = dati[:, 0]
h_error = 0.05
l = 108
l_error = 0.05

delta_theta = []
theta = []

for h_i in h:
    var1 = ((l-h_i)/l)**2
    var2 = (h_i/(l**2))
    d_l = (1/(np.sqrt(1-var1)))*var2

    var3 = (1/l)
    d_h = (1/(np.sqrt(1-var1)))*var3

    var4 = ((d_l*l_error) + (d_h*h_error))
    var5 = np.arccos((l-h_i)/l)

    theta.append(var5)
    delta_theta.append(var4)


print(theta)
print(delta_theta)



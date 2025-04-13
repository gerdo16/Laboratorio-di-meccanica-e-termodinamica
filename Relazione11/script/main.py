import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constants
pi = np.pi

# import data 
from data import r, F, dr, dF, mass_bar, lenght_bar, T

# Computation of torque and uncertainty with differentials method
M = F * r  # torque in Nm

dM_rel = abs(r) * dr + abs(F) * dF # relative uncertainty of M
dM = dM_rel * M  # absolute uncertainty of M

# Computing the mean value of M and its uncertainty
M_mean = np.mean(M)
error_M_mean = np.std(M, ddof=1) / np.sqrt(len(M))

print(f'Mean value of M: {M_mean} ± {error_M_mean} Nm')

# Computing K and its uncertainty
K = M_mean / pi
dK = pi * error_M_mean

print(f'K: {K} ± {dK} Nm/rad')

# PART 1: Moment of inertia

# Moment of the bar
I_bar = mass_bar * lenght_bar**2 / 12  # kg*m^2

print(f'I_bar: {I_bar} kg*m^2')

# Computing the moment of inertia and its uncertainty
I_values = []
for i in range(0, len(T), 4):
    block = T[i:i+4]
    print(block)
    T_mean = np.mean(block)
    I = K * T_mean**2 / (4 * np.pi**2)

    # remove I_bar from I
    I = I - I_bar
    print(I)
    I_values.append(I)

I_values = np.array(I_values)
I_mean = np.mean(I_values)

print("I for each block:", I_values)
print("I mean:", I_mean)
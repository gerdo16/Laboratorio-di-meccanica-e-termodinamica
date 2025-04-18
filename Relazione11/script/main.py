import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Constants
pi = np.pi

# import data 
from data import r, F, dr, dF, mass_bar, lenght_bar, T, dT, T_pt2, dT_pt2, r_pt2, dr_pt2, dmass_bar, dlenght_bar

print('r_pt2', r_pt2)
print('dr_pt2', dr_pt2)

# Computation of torque and uncertainty with differentials method
M = F * r  # torque in Nm

dM_rel = abs(F) * dr + abs(r) * dF # relative uncertainty of M
dM = dM_rel * M  # absolute uncertainty of M

# Computing the mean value of M and its uncertainty
M_mean = np.mean(M)
error_M_mean = np.std(M) / np.sqrt(len(M))

# Computing K and its uncertainty
K = M_mean / pi
dK = error_M_mean / pi

print(f'K: {K} ± {dK} Nm/rad')
print(f'M:{M}')
print('Uncertainties on M', dM)
print(f'Mean M: {M_mean} ± {error_M_mean} Nm')
print(f'K: {K} ± {dK} Nm/rad')

# PART 1: Moment of inertia

# Moment of the bar
I_bar = mass_bar * lenght_bar**2 / 12  # kg*m^2

print(f'I_bar: {I_bar} kg*m^2')

# Computing the moment of inertia and its uncertainty
I_values = []
dI_values = []
T_mean_values = []
error_T_mean_values = []
for i in range(0, len(T), 4):
    block = T[i:i+4]

    # UPDATE
    T_max = np.max(block)
    T_min = np.min(block)
    T_mean = (T_max + T_min) / 2
    error_T_mean = (T_max - T_min) / 2


    T_mean_values.append(T_mean)
    error_T_mean_values.append(error_T_mean)

    I = K * T_mean**2 / (4 * pi**2)
    dI = (T_mean**2 * dK + 2 * K * T_mean * error_T_mean) / (4 * pi**2)

    I = I - I_bar
    dI_bar = (lenght_bar**2 * dmass_bar + 2 * mass_bar * lenght_bar * dlenght_bar) / 12

    # update dI
    dI = dI + dI_bar

    I_values.append(I)
    dI_values.append(dI)

I_values = np.array(I_values)

print('I bar:', I_bar)
print('dI bar:', dI_bar)
print('Distances r' , r)
print('Uncertainties on distances r' , dr)
print('Moments of inertia array' , I_values)
print('Uncertainties on inertia moments array' , dI_values)
print('T_mean array' , T_mean_values)
print('T_mean error array' , error_T_mean_values)

# Graph of T_mean vs r^2
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(r**2, T_mean_values, 'o-', label='T mean')
plt.xlabel('$r^2$ (m$^2$)')
plt.ylabel('T mean (s)')
plt.title('T mean vs $r^2$')
plt.grid(True)
plt.legend()

# Plot 2: I vs r^2
plt.subplot(1, 2, 2)
plt.errorbar(r**2, I_values, yerr=dI_values, fmt='o-', label='I', capsize=4)
plt.xlabel('$r^2$ (m$^2$)')
plt.ylabel('Moment of inertia I (kg·m²)')
plt.title('Moment of inertia vs $r^2$')
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()

# PART 2: Moment of inertia of the Disk

# Computing the moment of inertia and its uncertainty
I_pt2_values = []
dI_pt2_values = []
T_mean_pt2_values = []
for i in range(0, len(T), 4):
    block = T_pt2[i:i+4]

    # UPDATE
    T_max = np.max(block)
    T_min = np.min(block)
    T_mean = (T_max + T_min) / 2
    error_T_mean = (T_max - T_min) / 2

    T_mean_pt2_values.append(T_mean)

    I = K * T_mean**2 / (4 * pi**2)
    dI = (T_mean**2 * dK + 2 * K * T_mean * error_T_mean) / (4 * pi**2)
    I_pt2_values.append(I)
    dI_pt2_values.append(dI)

I_pt2_values = np.array(I_pt2_values)

# Data for Huygens-Steiner theorem
d2 = r_pt2**2
I_pt2_values = np.array(I_pt2_values)
dI_pt2_values = np.array(dI_pt2_values)

print('I pt2:', I_pt2_values)
print('dI pt2:', dI_pt2_values)

# Least squares fit
slope, y_intercept = np.polyfit(d2, I_pt2_values, 1)
y = slope * d2 + y_intercept

plt.plot(d2, y, color="red", label="Best fit line")
plt.errorbar(d2, I_pt2_values, xerr=2*dr_pt2*d2, yerr=dI_pt2_values, fmt='o', capsize=5, label="Dati con errore")

plt.show()
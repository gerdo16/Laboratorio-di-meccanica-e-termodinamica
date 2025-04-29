import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Import T_1 and T_2 from data.py
from data import T1, T2, t

# Convert T_1 and T_2 to numpy arrays for easier manipulation
T1 = np.array(T1)
T2 = np.array(T2)
t = np.array(t)

log_T_2_minus_T_1 = []
for i in range(len(T1)):
    log_T_2_minus_T_1.append(np.log(T2[i] - T1[i]))



# graphical representation of the data
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()



slope_values = []
delta_b_values = []
intercept_values = []
for i in range(len(log_T_2_minus_T_1)):

    # uncertainties in log(T2 - T1)
    dlog_T_2_minus_T_1 = (1 / (T2[i] - T1[i])) * (0.1 + 0.1)  # Assuming error in T1 and T2 is 0.1
    dlog_T_2_minus_T_1 = np.array(dlog_T_2_minus_T_1)

    # least squares fit: y = mx + b
    slope, intercept = np.polyfit(t, log_T_2_minus_T_1[i], 1)

    # compute uncertainties in slope
    residuals = log_T_2_minus_T_1[i] - (slope * t + intercept)
    sigma_y = np.sqrt(np.sum(residuals**2) / (len(t) - 2))
    delta = len(t) * np.sum((t - np.mean(t))**2)
    sigma_b = sigma_y * np.sqrt(len(t) / delta)
    # Unvertainty in slope
    delta_b = 3 * sigma_b

    slope_values.append(slope)
    delta_b_values.append(delta_b)

    # Plot
    ax = axes[i]
    ax.errorbar(t, log_T_2_minus_T_1[i], yerr=dlog_T_2_minus_T_1, fmt='o',ms = 2, label='Dati sperimentali')
    ax.plot(t, slope * t + intercept, 'r-', label='Fit lineare')
    ax.set_title(f'Dataset {i+1}')
    ax.set_xlabel('Tempo (s)')
    ax.set_ylabel('log(T2 - T1)')
    ax.grid(True)
    ax.legend()

plt.suptitle('Fit lineare di log(T2 - T1) vs Tempo')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Output
print("Slopes:", slope_values)
print("Uncertainties on slopes:", delta_b_values)
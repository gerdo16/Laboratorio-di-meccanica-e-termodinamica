import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Import T_1 and T_2 from data.py
from data import T_1, T_2, t

# Convert T_1 and T_2 to numpy arrays for easier manipulation
T_1 = np.array(T_1)
T_2 = np.array(T_2)
t = np.array(t)

# Check if T_1 and T_2 are 2D arrays
if T_1.ndim != 2 or T_2.ndim != 2:
    raise ValueError("T_1 and T_2 must be 2D arrays")

# Check if T_1 and T_2 have the same length
if len(T_1) != len(T_2):
    raise ValueError("T_1 and T_2 must have the same length")

T_1_mean_values = []
error_T_1_mean_values = []
T_2_mean_values = []
error_T_2_mean_values = []

for i in range(len(T_1)):
    T_1_max = np.max(T_1[i])
    T_1_min = np.min(T_1[i])
    T_1_mean = (T_1_max + T_1_min) / 2
    error_T_1_mean = (T_1_max - T_1_min) / 2
    # Store the mean and error values
    T_1_mean_values.append(T_1_mean)
    error_T_1_mean_values.append(error_T_1_mean)

    T_2_max = np.max(T_2[i])
    T_2_min = np.min(T_2[i])
    T_2_mean = (T_2_max + T_2_min) / 2
    error_T_2_mean = (T_2_max - T_2_min) / 2
    # Store the mean and error values
    T_2_mean_values.append(T_2_mean)
    error_T_2_mean_values.append(error_T_2_mean)

# Convert lists to numpy arrays for easier manipulation
T_1_mean_values = np.array(T_1_mean_values)
error_T_1_mean_values = np.array(error_T_1_mean_values)
T_2_mean_values = np.array(T_2_mean_values)
error_T_2_mean_values = np.array(error_T_2_mean_values)

# Compute log(T_2_mean_values - T_1_mean_values)
T_2_minus_T_1 = T_2_mean_values - T_1_mean_values
log_T_2_minus_T_1 = np.log(T_2_minus_T_1)

# Compute the uncertainty in log(T_2_mean_values - T_1_mean_values)
dlog_T_2_minus_T_1 = (1 / T_2_minus_T_1) * (error_T_2_mean_values + error_T_1_mean_values)

# Least squares fit: y = mx + b
slope, intercept = np.polyfit(t, log_T_2_minus_T_1, 1)

# Calculate fitted y values
y_fit = slope * t + intercept

# Calculate the residuals (difference between the observed and fitted values)
residuals = log_T_2_minus_T_1 - y_fit

# Calculate sigma_y (standard deviation of the residuals)
sigma_y = np.sqrt(np.sum(residuals**2) / (len(t) - 2))

# Calculate the uncertainty in the slope (sigma_b) and intercept (sigma_a)
delta = len(t) * np.sum((t - np.mean(t))**2)
sigma_b = sigma_y * np.sqrt(len(t) / delta)
sigma_a = sigma_y * np.sqrt(np.sum(t**2) / delta)

# Calculate the final uncertainties (3 * sigma)
delta_b = 3 * sigma_b
delta_a = 3 * sigma_a

# Display the results
print(f"Slope (b) = {slope:.4f} ± {delta_b:.4f}")
print(f"Intercept (a) = {intercept:.4f} ± {delta_a:.4f}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.errorbar(t, log_T_2_minus_T_1, yerr=dlog_T_2_minus_T_1, fmt='o', label="Data with error")
plt.plot(t, y_fit, label="Least Squares Fit", color='red')
plt.xlabel('Time (s)')
plt.ylabel('log(T2 - T1)')
plt.title('Least Squares Fit of log(T2 - T1) vs Time')
plt.legend()
plt.grid(True)
plt.show()
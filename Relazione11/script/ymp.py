# graph of I_pt2_values vs r_pt2^2
plt.subplot(1, 3, 1)
plt.errorbar(r_pt2**2, I_pt2_values, yerr=dI_pt2_values, fmt='o-', label='I', capsize=4)
plt.xlabel('$r^2$ (m$^2$)')
plt.ylabel('Moment of inertia I (kg·m²)')
plt.title('Moment of inertia vs $r^2$')
plt.grid(True)
plt.legend()

# Data for Huygens-Steiner theorem
d2 = r_pt2**2
I_pt2_values = np.array(I_pt2_values)
dI_pt2_values = np.array(dI_pt2_values)


# Parameters
mass = 2.00  # kg 
I0 = I_pt2_values[0]  

# Grid of values
d2_grid = np.linspace(0, np.max(d2)*1.1, 200)

# Plot
plt.subplot(1, 3, 2)
plt.plot(d2_grid, I0 + mass * d2_grid, 'r--', label=f'(mass = {mass:.2f} kg)')

plt.xlabel('$d^2$ (m²)')
plt.ylabel('I (kg·m²)')
plt.title('Huygens-Steiner')
plt.grid(True)
plt.legend()

# Least squares fit
slope, y_intercept = np.polyfit(d2, I_pt2_values, 1)
y = slope * d2 + y_intercept

plt.plot(d2, y, color="red", label="Best fit line")

plt.show()
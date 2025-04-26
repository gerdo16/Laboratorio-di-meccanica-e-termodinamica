import numpy as np
import matplotlib.pyplot as plt

from Data import theta_i_degrees, dtheta_i_degrees, theta_ip_degrees, dtheta_i_degrees, theta_min_degrees, dtheta_min_degrees, theta_i_radians, dtheta_i_radians, theta_ip_radians, dtheta_ip_radians, theta_min_radians, dtheta_min_radians, alpha_degrees, alpha_radians
from Scripts.Grafico1 import theta_min


def delta_teorico(theta_i_deg, alpha_deg, n):
    theta_i = np.radians(theta_i_deg)
    alpha = np.radians(alpha_deg)
    delta = theta_i-alpha+np.arcsin((np.sin(alpha)*np.sqrt(n**2-np.sin(theta_i)**2))-(np.cos(alpha)*np.sin(theta_i)))
    return np.degrees(delta)


delta_single = [i + ip - alpha_degrees for i, ip in zip(theta_i_degrees, theta_ip_degrees)]
delta = delta_single + delta_single[::-1]
theta = theta_i_degrees + theta_ip_degrees[::-1]

ddelta = [1 for v in delta]
dtheta = [0.5 for v in theta]

theta_i_continui = np.linspace(min(theta), max(theta), 500)
delta_teo = delta_teorico(theta_i_continui, alpha_deg=45, n=1.5)

plt.figure(figsize=(10, 5))
plt.errorbar(theta, delta, xerr=dtheta, yerr=ddelta, fmt='o', linestyle='-', capsize=5, label="Dati sperimentali")
plt.plot(theta_i_continui, delta_teo, 'r-', label='Curva teorica')

# Aggiungere etichette e titolo
plt.xlabel(r'$\theta$ (°)')
plt.ylabel(r'$\delta$ (°)')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.savefig("grafico1.pdf", format="pdf")
plt.show()

n = np.sin(theta_min_radians)/np.sin(alpha_radians/2)
dn = (np.cos(theta_min_radians)/np.sin(alpha_radians/2))*dtheta_min_radians

print("n= ", n, "+-", dn)





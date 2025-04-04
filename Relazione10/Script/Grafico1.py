import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt('dati')

OD = 19.5 / 100
OpD = data[:, 0] / 100
h = data[:, 1] / 100
theta_i = 62.06

y = OD-OpD
x = h
xerror = 0.0005
yerror = 0.0005

mediax = np.mean(x)
mediay = np.mean(y)
somma = 0
sommax = 0

for elementox,elementoy in zip(x, y):
    somma = somma + (elementox - mediax)*(elementoy - mediay)

for elemento in x:
    sommax = sommax + (elemento - mediax)**2

b = somma/sommax
a = mediay - (b*mediax)
print("b=", b)
print("a=", a)

delta = sommax*len(x)

somma_sigmay = 0
for elementox, elementoy in zip(x, y):
    somma_sigmay =  somma_sigmay + (elementoy - (elementox*b) - a)**2

sigmay = np.sqrt(somma_sigmay/(len(x)-2))

somma_sigma_a = 0
for elemento in x:
    somma_sigma_a = somma_sigma_a + elemento**2

sigma_a = sigmay*np.sqrt(somma_sigma_a/delta)
sigma_b = sigmay*np.sqrt(len(x)/delta)

delta_a = 3*sigma_a
delta_b = 3*sigma_b

theta_r = np.arctan(np.tan(math.radians(theta_i)) - b)

print("theta_r: ", theta_r)

n = np.sin(math.radians(theta_i))/np.sin(theta_r)

print("n: ", n)

plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='o', capsize=5, label="Dati con errore")

# Aggiungo retta di regressione
coeff_angolare, intercetta = np.polyfit(x, y, 1)
y_retta = coeff_angolare * x + intercetta
#acc = coeff_angolare*2
#alpha = np.arctan(2.3/85)
#sinalpha = np.sin(alpha)
#print("alpha:", alpha)
#print("sin(alpha):", sinalpha)
#print("Accelerazione:", acc)
#print("Coefficiente angolare (slope):", coeff_angolare)
#print("Intercetta:", intercetta)
plt.plot(x, y_retta, color="red", label="Retta di best fit")

# Aggiungere etichette e titolo
plt.xlabel(r"Altezza ($m$)")
plt.ylabel(r'$\Delta x$ ($m$)')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.savefig("grafico1.pdf", format="pdf")
plt.show()
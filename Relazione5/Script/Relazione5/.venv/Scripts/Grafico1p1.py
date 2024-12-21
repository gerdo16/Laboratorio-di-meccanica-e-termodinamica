import numpy as np
import matplotlib.pyplot as plt
# Leggere i dati dal file .txt
data = np.loadtxt('Dati1p1.txt')

# Separare i dati in x, y, e gli errori
y = data[:, 0]  # prima colonna
yerror = data[:, 1]  # seconda colonna
x = data[:, 2]  # terza colonna
xerror = data[:, 3] # quarta colonna

y = y/100
yerror = yerror/100
x = x/1000
xerror = xerror/1000

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

print("delta_b=", delta_b)
print("delta_a=", delta_a)



# Creare il grafico con bande di errore
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='o', capsize=5, label="Dati con errore")

# Aggiungo retta di regressione
coeff_angolare, intercetta = np.polyfit(x, y, 1)
y_retta = coeff_angolare * x + intercetta

print("Coefficiente angolare (slope):", coeff_angolare)
print("Intercetta:", intercetta)
plt.plot(x, y_retta, color="red", label="Retta di best fit")

# Aggiungere etichette e titolo
plt.xlabel(r'Massa ($kg$)')
plt.ylabel(r'$\Delta x$ ($m$)')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.savefig("grafico1p1.pdf", format="pdf")
plt.show()
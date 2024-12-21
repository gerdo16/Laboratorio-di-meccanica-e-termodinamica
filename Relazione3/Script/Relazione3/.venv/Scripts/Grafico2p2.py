import numpy as np
import matplotlib.pyplot as plt
# Leggere i dati dal file .txt
data = np.loadtxt('Dati1p2.txt')
# Separare i dati in x, y, e gli errori
y = data[:, 0]  # prima colonna
x = data[:, 1]  # seconda colonna

x = x/100
y = y ** 2

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
plt.scatter(x, y, label="Dati")

coeff_angolare, intercetta = np.polyfit(x, y, 1)
y_retta = coeff_angolare * x + intercetta
print("Coefficiente angolare (slope):", coeff_angolare)

# Aggiungo la retta di best fit
plt.plot(x, y_retta, color="red", label="Retta di best fit")

# Aggiungere etichette e titolo
plt.xlabel(r'Lunghezza $(m)$')
plt.ylabel(r'Quadrato del periodo $(s^2)$')
plt.title('Grafico')
# Mostrare legenda
plt.legend()
# Mostrare il grafico
plt.savefig("grafico2p2.pdf", format="pdf")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
# Leggere i dati dal file .txt
data = np.loadtxt('Dati1p2.txt')
# Separare i dati in x, y, e gli errori
y = data[:, 0]  # prima colonna
x = data[:, 1]  # seconda colonna

x = x/100

# Creare il grafico con bande di errore
plt.scatter(x, y, label="Dati")

coeff_angolare, intercetta = np.polyfit(x, y, 1)
y_retta = coeff_angolare * x + intercetta
print("Coefficiente angolare (slope):", coeff_angolare)
plt.plot(x, y_retta, color="red", label="Retta di best fit")

# Aggiungere etichette e titolo
plt.xlabel(r'Lunghezza $(m)$')
plt.ylabel(r'Periodo $(s)$')
plt.title('Grafico')
# Mostrare legenda
plt.legend()
# Mostrare il grafico
plt.savefig("grafico1p2.pdf", format="pdf")
plt.show()
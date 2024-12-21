import numpy as np
import matplotlib.pyplot as plt

# Leggere i dati dal file .txt
data = np.loadtxt('file.txt')

# Separare i dati in x, y, e gli errori
x = data[:, 0]  # prima colonna
y = data[:, 1]  # seconda colonna
error = data[:, 2]  # terza colonna

# Creare il grafico con bande di errore
plt.errorbar(x, y, yerr=error, fmt='o', capsize=5, label="Dati con errore")

# Aggiungere etichette e titolo
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.show()
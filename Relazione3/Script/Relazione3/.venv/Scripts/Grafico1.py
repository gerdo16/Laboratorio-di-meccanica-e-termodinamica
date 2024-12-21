import numpy as np
import matplotlib.pyplot as plt
# Leggere i dati dal file .txt
data = np.loadtxt('Dati1.txt')

# Separare i dati in x, y, e gli errori
x = data[:, 0]  # prima colonna
y = data[:, 1]  # seconda colonna
xerror = data[:, 2]  # terza colonna
yerror = data[:, 3] # quarta colonna

x = x*3.14/180
xerror = xerror*3.14/180

# Creare il grafico con bande di errore
plt.errorbar(x, y, xerr=xerror, yerr=yerror, fmt='o', capsize=5, label="Dati con errore")

# Aggiungere etichette e titolo
plt.xlabel('Ampiezza (rad)')
plt.ylabel('Periodo (s)')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.savefig("grafico1p1.pdf", format="pdf")
plt.show()

import numpy as np
import matplotlib.pyplot as plt

from Data import T, dT, DV, dDV, I, dI, Me, dMe, M, dM, t, dt, T0, dT0

E = []
dE = []

for temp, dtemp in zip(t, dt):
    E.append(temp*I*DV)
    dE.append((I*temp*dDV)+(DV*temp*dI)+(DV*I*dtemp))


Q = []
dQ = []

T2 = []
dT2 = []

for temp, dtemp in zip(T, dT):
    T2.append(temp-T0)
    dT2.append(dtemp + dT0)


for temp, dtemp in zip(T2, dT2):
    Q.append((M+Me)*temp)
    dQ.append((temp*dM)+(temp*dMe)+(M+Me)*dtemp)

# Creare il grafico con bande di errore
plt.errorbar(Q, E, xerr=dQ, yerr=dE, fmt='o', capsize=5, label="Dati con errore")
#plt.plot(x, y)

# Aggiungo retta di regressione
coeff_angolare, intercetta = np.polyfit(Q, E, 1)
y_retta = coeff_angolare * np.array(Q) + intercetta

print("Coefficiente angolare (slope):", coeff_angolare)
print("Intercetta:", intercetta)
plt.plot(Q, y_retta, color="red", label="Retta di best fit")

# Aggiungere etichette e titolo
plt.xlabel(r'Q')
plt.ylabel(r'E')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.savefig("grafico1.pdf", format="pdf")
plt.show()


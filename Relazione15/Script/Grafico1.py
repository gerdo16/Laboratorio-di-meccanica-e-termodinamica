import numpy as np
import matplotlib.pyplot as plt

from Data import P_lente, dP_lente, P_candela, dP_candela, Q

""" Calcolo p e la sua incertezza """
p = [candela-lente for candela, lente in zip(P_candela, P_lente)]
dp = [candela+lente for candela, lente in zip(dP_candela, dP_lente)]


q_temp = []
for x in Q:
    q_temp.append([round(P_lente[0]-x[0], 1), round(P_lente[0]-x[1], 1)])


""" Calcolo q e la sua incertezza """
q = []
dq = []
for x in q_temp:
    q.append( round((x[0]+x[1])/2, 1) )
    dq.append( round((x[0]-x[1])/2, 1) )


x = [1/t for t in p]
y = [1/t for t in q]
dx = [(1/(t**2))*dt for t,dt in zip(p, dp)]
dy = [(1/(t**2))*dt for t,dt in zip(q, dq)]

# Creare il grafico con bande di errore
plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o', capsize=5, label="Dati con errore")
#plt.plot(x, y)

# Aggiungo retta di regressione
coeff_angolare, intercetta = np.polyfit(x, y, 1)
y_retta = coeff_angolare * np.array(x) + intercetta

print("Coefficiente angolare (slope):", coeff_angolare)
print("Intercetta:", intercetta)
plt.plot(x, y_retta, color="red", label="Retta di best fit")

# Aggiungere etichette e titolo
plt.xlabel(r'p')
plt.ylabel(r'q')
plt.title('Grafico con Bande di Errore')

# Mostrare legenda
plt.legend()

# Mostrare il grafico
plt.savefig("grafico1.pdf", format="pdf")
plt.show()


f = 1/intercetta
print("Distanza focale: ", f)
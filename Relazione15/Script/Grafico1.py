import numpy as np
import matplotlib.pyplot as plt

from Data import P_lente, dP_lente, P_candela, dP_candela, Q

""" Calcolo p e la sua incertezza """
p = [candela-lente for candela, lente in zip(P_candela, P_lente)]
dp = [candela+lente for candela, lente in zip(dP_candela, dP_lente)]
print("p: ", p, "+-", dp)

q_temp = []
for x in Q:
    q_temp.append([round(P_lente[0]-x[0], 1), round(P_lente[0]-x[1], 1)])


""" Calcolo q e la sua incertezza """
q = []
dq = []
for x in q_temp:
    q.append( round((x[0]+x[1])/2, 1) )
    dq.append( round((x[0]-x[1])/2, 1) )
print("q: ", q, "+-", dq)

x = [1/t for t in p]
y = [1/t for t in q]
dx = [(1/(t**2))*dt for t,dt in zip(p, dp)]
dy = [(1/(t**2))*dt for t,dt in zip(q, dq)]

xerror = dx
yerror = dy
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
print("delta a: ", delta_a)

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
df = (1/a**2)*delta_a
print("Distanza focale: ", f, "+-", df)
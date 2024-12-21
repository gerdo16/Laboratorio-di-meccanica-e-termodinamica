import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.backends.backend_pdf import PdfPages
import statistics
# Dati di esempio
dati = np.loadtxt('tempi1.txt')
# Creare un istogramma
counts, bin_edges = np.histogram(dati, bins=10, density=True)

fig, ax = plt.subplots()

ax.hist(dati, bins=6, density=True, color='skyblue', edgecolor='black')
# Aggiungere etichette e legenda
ax.set_xlabel('Tempi misurati (s)')
ax.set_ylabel('Densità di Frequenza')
ax.set_title('Istogramma dei dati')
#plt.legend()
# Mostrare il grafico
plt.show()

# Salvataggio dell'istogramma in un file PDF
with PdfPages('istogramma.pdf') as pdf:
    pdf.savefig(fig)  # Salva la figura corrente nel PDF
    plt.close(fig)    # Chiude la figura per liberare memoria



media = statistics.mean(dati)
mediana = statistics.median(dati)
moda = statistics.mode(dati)

print("media: ",media)

dev_std = np.std(dati)
print("dev std: ",dev_std)


# Intervallo in cui vuoi calcolare la frequenza relativa
interval_start = media - 3*dev_std  # Inizio dell'intervallo
interval_end = media + 3*dev_std    # Fine dell'intervallo
print("3dev std: ", 3*dev_std)


# Trova i bin che si sovrappongono con l'intervallo desiderato
bin_widths = np.diff(bin_edges)
relative_frequency = 0

for count, bin_start, bin_width in zip(counts, bin_edges[:-1], bin_widths):
    bin_end = bin_start + bin_width
    # Controlla se il bin è all'interno dell'intervallo desiderato
    if bin_start >= interval_start and bin_end <= interval_end:
        relative_frequency += count * bin_width

#print(f"Frequenza relativa nell'intervallo [{interval_start}, {interval_end}]: {relative_frequency}")

r = 0.001144
delta_r = 0.000099

p_s = 11047
delta_p_s = 2925

p = 1000
delta_p = 21

vl = 0.38/23.41
print("velocità: ", vl)
delta_vl = 3.23

n = (2/9)*(r**2)*((p_s-p)/vl)*9.81

print("coefficiente di viscosità: ", n)
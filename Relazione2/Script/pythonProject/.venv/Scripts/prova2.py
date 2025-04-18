import numpy as np
import matplotlib.pyplot as pltave
from scipy import stats
from matplotlib.backends.backend_pdf import PdfPages
import statistics
# Dati di esempio
dati = np.loadtxt('DatiIstogramma2.txt')
# Creare un istogramma
counts, bin_edges = np.histogram(dati, bins=10, density=True)

fig, ax = plt.subplots()

ax.hist(dati, bins=15, density=True, color='skyblue', edgecolor='black')
# Aggiungere etichette e legenda
ax.set_xlabel('Valori')
ax.set_ylabel('Densità di Frequenza')
ax.set_title('Istogramma dei dati')
plt.legend()
# Mostrare il grafico
plt.show()

# Salvataggio dell'istogramma in un file PDF
with PdfPages('istogramma.pdf') as pdf:
    pdf.savefig(fig)  # Salva la figura corrente nel PDF
    plt.close(fig)    # Chiude la figura per liberare memoria



media = statistics.mean(dati)
mediana = statistics.median(dati)
moda = statistics.mode(dati)

print(media)
print(mediana)
print(moda)

dev_std = np.std(dati)
print(dev_std)


# Intervallo in cui vuoi calcolare la frequenza relativa
interval_start = media - 3*dev_std  # Inizio dell'intervallo
interval_end = media + 3*dev_std    # Fine dell'intervallo

# Trova i bin che si sovrappongono con l'intervallo desiderato
bin_widths = np.diff(bin_edges)
relative_frequency = 0

for count, bin_start, bin_width in zip(counts, bin_edges[:-1], bin_widths):
    bin_end = bin_start + bin_width
    # Controlla se il bin è all'interno dell'intervallo desiderato
    if bin_start >= interval_start and bin_end <= interval_end:
        relative_frequency += count * bin_width

print(f"Frequenza relativa nell'intervallo [{interval_start}, {interval_end}]: {relative_frequency}")
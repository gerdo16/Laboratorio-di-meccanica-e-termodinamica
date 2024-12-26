import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib.backends.backend_pdf import PdfPages
import statistics

result = []
counter = 0

for i  in range(4):
    for j in range(20):
        result.append(i+1 + j+1)
        counter += 1


#print(result)
lista = list(set(result))
print(lista)


counts, bin_edges = np.histogram(result, bins=23, density=True)

fig, ax = plt.subplots()

ax.hist(result, density=True, bins=23, color='skyblue', edgecolor='black')
# Aggiungere etichette e legenda
ax.set_xlabel('Valori')
ax.set_ylabel('Frequenza relativa')
ax.set_title('Istogramma dei dati')
plt.legend()
# Mostrare il grafico
plt.show()

# Salvataggio dell'istogramma in un file PDF
with PdfPages('istogramma1.pdf') as pdf:
    pdf.savefig(fig)  # Salva la figura corrente nel PDF
    plt.close(fig)    # Chiude la figura per liberare memoria



media = statistics.mean(result)
mediana = statistics.median(result)
moda = statistics.mode(result)

print(media)
print(mediana)
print(moda)

dev_std = np.std(result)
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
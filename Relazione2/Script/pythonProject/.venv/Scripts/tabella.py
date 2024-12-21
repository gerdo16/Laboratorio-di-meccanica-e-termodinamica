import pandas as pd

# Carica il file (adatta il percorso e il nome del file)
df = pd.read_csv('DatiIstogramma2.txt', header=None, names=['valori'])

# Calcola la frequenza assoluta per la colonna "valori"
frequenze_assolute = df['valori'].value_counts().reset_index()

# Rinomina le colonne per chiarezza
frequenze_assolute.columns = ['Valore', 'Frequenza Assoluta']

# Mostra la tabella con le frequenze assolute
print(frequenze_assolute)
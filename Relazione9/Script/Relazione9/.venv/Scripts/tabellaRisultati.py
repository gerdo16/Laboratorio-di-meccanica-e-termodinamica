import pandas as pd

# Carica il file
df = pd.read_csv('Somma.txt', header=None, names=['Valori'])

# Calcola la frequenza assoluta per la colonna "valori"
frequenze_assolute = df['Valori'].value_counts().reset_index()

frequenze_assolute.columns = ['Valore', 'Frequenza assoluta']

print(frequenze_assolute)

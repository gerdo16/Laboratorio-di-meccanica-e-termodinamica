import pandas as pd

# Carica il file
df_quattro = pd.read_csv('Quattro.txt', header=None, names=['Valori'])
df_venti = pd.read_csv('Venti.txt', header=None, names=['Valori'])

# Calcola la frequenza assoluta per la colonna "valori"
frequenze_assolute_quattro = df_quattro['Valori'].value_counts().reset_index()
frequenze_assolute_venti = df_venti['Valori'].value_counts().reset_index()

frequenze_assolute_quattro.columns = ['Valore', 'Frequenza assoluta']
frequenze_assolute_venti.columns = ['Valore', 'Frequenza assoluta']

print(frequenze_assolute_quattro)
print(frequenze_assolute_venti)

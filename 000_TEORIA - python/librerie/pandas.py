import pandas as pd

# 1. Creazione di un DataFrame

# Creare un DataFrame da un dizionario
data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Età': [25, 30, 35],
    'Città': ['Roma', 'Milano', 'Torino']
}
df = pd.DataFrame(data)
print("DataFrame Creato:")
print(df)

# 2. Lettura di Dati da File

# Leggere un file CSV
df_csv = pd.read_csv('file.csv')
print("\nDati Lettura da CSV:")
print(df_csv)

# 3. Scrittura di Dati in un File

# Scrivere il DataFrame in un file CSV
df.to_csv('output.csv', index=False)
print("\nDataFrame scritto in 'output.csv'.")

# 4. Selezione di Dati

# Selezionare una colonna
nomi = df['Nome']
print("\nColonna 'Nome':")
print(nomi)

# Selezionare righe tramite condizioni
over_30 = df[df['Età'] > 30]
print("\nPersone con età superiore a 30:")
print(over_30)

# 5. Manipolazione di Dati

# Aggiungere una nuova colonna
df['Sesso'] = ['F', 'M', 'M']
print("\nDataFrame dopo l'aggiunta di una colonna 'Sesso':")
print(df)

# Modificare una colonna esistente
df['Età'] += 1  # Incrementare l'età di 1 anno
print("\nDataFrame dopo l'aggiornamento dell'età:")
print(df)

# 6. Aggregazione dei Dati

# Raggruppare i dati per città e calcolare l'età media
age_grouped = df.groupby('Città')['Età'].mean()
print("\nEtà media per città:")
print(age_grouped)

# 7. Gestione dei Dati Mancanti

# Creare un DataFrame con dati mancanti
data_with_nan = {
    'Nome': ['Alice', 'Bob', None],
    'Età': [25, None, 35]
}
df_nan = pd.DataFrame(data_with_nan)

# Riempire i dati mancanti
df_nan_filled = df_nan.fillna({'Nome': 'Sconosciuto', 'Età': df_nan['Età'].mean()})
print("\nDataFrame con dati mancanti riempiti:")
print(df_nan_filled)

# 8. Ordinamento dei Dati

# Ordinare il DataFrame per età
df_sorted = df.sort_values(by='Età', ascending=False)
print("\nDataFrame ordinato per età (decrescente):")
print(df_sorted)

# 9. Filtraggio Avanzato

# Filtrare righe che soddisfano più condizioni
filtered_df = df[(df['Età'] > 25) & (df['Città'] == 'Milano')]
print("\nPersone di Milano con età superiore a 25:")
print(filtered_df)

# 10. Visualizzazione dei Dati

# Visualizzazione dei dati (richiede matplotlib)
import matplotlib.pyplot as plt

df['Età'].hist()
plt.title('Distribuzione delle Età')
plt.xlabel('Età')
plt.ylabel('Frequenza')
plt.show()

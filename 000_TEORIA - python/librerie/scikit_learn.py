import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Caricamento di un Dataset

# Caricare il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target
print("Dataset Iris caricato. Numero di campioni:", X.shape[0])

# 2. Suddivisione del Dataset

# Suddividere il dataset in training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Suddivisione del dataset completata.")

# 3. Normalizzazione dei Dati

# Normalizzare i dati
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("Dati normalizzati.")

# 4. Creazione e Addestramento di un Modello

# Creare un classificatore Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Modello addestrato.")

# 5. Previsione sui Dati di Test

# Fare previsioni sui dati di test
y_pred = model.predict(X_test)

# 6. Valutazione del Modello

# Calcolare l'accuratezza
accuracy = accuracy_score(y_test, y_pred)
print("Accuratezza del modello:", accuracy)

# Matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrice di confusione:\n", conf_matrix)

# 7. Visualizzazione della Matrice di Confusione

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()

# 8. Importanza delle Caratteristiche

# Calcolare l'importanza delle caratteristiche
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

# Visualizzare l'importanza delle caratteristiche
plt.figure(figsize=(8, 6))
plt.title('Importanza delle Caratteristiche')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), iris.feature_names, rotation=45)
plt.xlim([-1, X.shape[1]])
plt.show()

# 9. Salvataggio del Modello

import joblib

# Salvare il modello
joblib.dump(model, 'random_forest_model.pkl')
print("Modello salvato come 'random_forest_model.pkl'.")

# 10. Caricamento del Modello

# Caricare il modello
loaded_model = joblib.load('random_forest_model.pkl')
print("Modello caricato con successo.")

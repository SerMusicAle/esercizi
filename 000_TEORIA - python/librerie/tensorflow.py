import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# 1. Caricamento di un Dataset

# Utilizzare il dataset MNIST per il riconoscimento di cifre
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizzare i dati

# 2. Creazione di un Modello

# Creare un modello sequenziale
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Appiattire le immagini
    layers.Dense(128, activation='relu'),   # Strato denso con ReLU
    layers.Dropout(0.2),                    # Dropout per prevenire l'overfitting
    layers.Dense(10, activation='softmax')  # Strato di output
])

# 3. Compilazione del Modello

model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])
print("Modello compilato.")

# 4. Addestramento del Modello

model.fit(x_train, y_train, epochs=5)  # Addestrare per 5 epoche
print("Addestramento completato.")

# 5. Valutazione del Modello

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print("\nAccuratezza sul test set:", test_acc)

# 6. Previsione con il Modello

predictions = model.predict(x_test)
predicted_classes = np.argmax(predictions, axis=1)  # Classi previste

# 7. Visualizzazione di Alcuni Risultati

import matplotlib.pyplot as plt

# Visualizzare alcune immagini di test e le loro previsioni
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f'Predizione: {predicted_classes[i]}')
    plt.axis('off')
plt.show()

# 8. Salvataggio del Modello

model.save('mnist_model.h5')
print("Modello salvato come 'mnist_model.h5'.")

# 9. Caricamento del Modello

loaded_model = keras.models.load_model('mnist_model.h5')
print("Modello caricato con successo.")

# 10. Utilizzo del Modello Caricato per Previsioni

loaded_predictions = loaded_model.predict(x_test)
loaded_predicted_classes = np.argmax(loaded_predictions, axis=1)
print("Previsioni con il modello caricato:", loaded_predicted_classes[:10])

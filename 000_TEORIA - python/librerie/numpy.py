import numpy as np

# 1. Creazione di Array

# Creare un array da una lista
array_1d = np.array([1, 2, 3, 4, 5])
print("Array 1D creato:", array_1d)

# Creare un array 2D (matrice)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray 2D creato:")
print(array_2d)

# 2. Creazione di Array Speciali

# Creare un array di zeri
zeros_array = np.zeros((2, 3))
print("\nArray di zeri:")
print(zeros_array)

# Creare un array di uno
ones_array = np.ones((3, 2))
print("\nArray di uno:")
print(ones_array)

# Creare un array di valori equidistanti
linspace_array = np.linspace(0, 10, 5)  # 5 valori da 0 a 10
print("\nArray di valori equidistanti:", linspace_array)

# 3. Operazioni su Array

# Operazioni element-wise
array_sum = array_1d + 10
print("\nArray dopo somma di 10:", array_sum)

# Moltiplicazione per uno scalare
array_product = array_1d * 2
print("Array dopo moltiplicazione per 2:", array_product)

# 4. Statistiche

# Calcolo della media
mean_value = np.mean(array_1d)
print("\nMedia dell'array 1D:", mean_value)

# Calcolo della somma
sum_value = np.sum(array_1d)
print("Somma dell'array 1D:", sum_value)

# 5. Indicizzazione e Slicing

# Accesso a elementi singoli
first_element = array_1d[0]
print("\nPrimo elemento dell'array 1D:", first_element)

# Slicing dell'array
slice_array = array_1d[1:4]  # elementi da indice 1 a 3
print("Slicing dell'array 1D:", slice_array)

# 6. Operazioni su Matrici

# Trasposizione di una matrice
transposed_array = array_2d.T
print("\nMatrice trasposta:")
print(transposed_array)

# Moltiplicazione di matrici
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("\nProdotto di due matrici:")
print(matrix_product)

# 7. Reshape degli Array

# Cambiare la forma di un array
reshaped_array = array_1d.reshape(5, 1)
print("\nArray dopo reshape (5, 1):")
print(reshaped_array)

# 8. Maschere Logiche

# Creare una maschera logica
mask = array_1d > 3
print("\nMaschera logica per valori maggiori di 3:", mask)

# Usare la maschera per filtrare l'array
filtered_array = array_1d[mask]
print("Valori maggiori di 3:", filtered_array)

# 9. Concatenazione di Array

# Concatenare due array
concatenated_array = np.concatenate((array_1d, array_product))
print("\nArray concatenato:")
print(concatenated_array)

# 10. Funzioni Universali (ufunc)

# Funzione seno applicata a un array
sin_array = np.sin(array_1d)
print("\nSeno dei valori dell'array 1D:")
print(sin_array)

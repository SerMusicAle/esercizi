import array

# Nome: Array - Creazione
# Codice:
arr = array.array('i', [1, 2, 3])
# Output: array('i', [1, 2, 3])
# Descrizione: Crea un array di interi con valori 1, 2, e 3.

# Nome: Array - Accesso agli elementi
# Codice:
print(arr[0])  
# Output: 1
# Descrizione: Accede al primo elemento dell'array.

# Nome: Array - Aggiornamento di un elemento
# Codice:
arr[0] = 10
print(arr)
# Output: array('i', [10, 2, 3])
# Descrizione: Aggiorna il primo elemento dell'array a 10.

# Nome: Array - Aggiunta di elementi
# Codice:
arr.append(4)
print(arr)  
# Output: array('i', [10, 2, 3, 4])
# Descrizione: Aggiunge 4 alla fine dell'array.

# Nome: Array - Aggiunta di più elementi
# Codice:
arr.extend([5, 6])
print(arr)  
# Output: array('i', [10, 2, 3, 4, 5, 6])
# Descrizione: Aggiunge 5 e 6 alla fine dell'array.

# Nome: Array - Inserimento di un elemento
# Codice:
arr.insert(1, 15)
print(arr)
# Output: array('i', [10, 15, 2, 3, 4, 5, 6])
# Descrizione: Inserisce 15 alla posizione con indice 1.

# Nome: Array - Rimozione di un elemento
# Codice:
arr.remove(2)
print(arr)  
# Output: array('i', [10, 15, 3, 4, 5, 6])
# Descrizione: Rimuove la prima occorrenza del valore 2 nell'array.

# Nome: Array - Rimozione dell'ultimo elemento
# Codice:
arr.pop()
print(arr)  
# Output: array('i', [10, 15, 3, 4, 5])
# Descrizione: Rimuove l'ultimo elemento dall'array.

# Nome: Array - Concatenazione di array
# Codice:
new_arr = arr + array.array('i', [7, 8])
print(new_arr)  
# Output: array('i', [10, 15, 3, 4, 5, 7, 8])
# Descrizione: Concatenazione di due array.

# Nome: Array - Slicing
# Codice:
print(arr[1:4])  
# Output: array('i', [15, 3, 4])
# Descrizione: Estrae una porzione dell'array dall'indice 1 all'indice 3.

# Nome: Array - Lunghezza
# Codice:
print(len(arr))  
# Output: 5
# Descrizione: Restituisce la lunghezza dell'array.

# Nome: Array - Trovare l'indice di un elemento
# Codice:
print(arr.index(15))  
# Output: 1
# Descrizione: Trova l'indice della prima occorrenza di 15 nell'array.

# Nome: Array - Contare le occorrenze di un elemento
# Codice:
print(arr.count(10))  
# Output: 1
# Descrizione: Conta il numero di volte che il valore 10 appare nell'array.

# Nome: Array - Inversione degli elementi
# Codice:
arr.reverse()
print(arr)  
# Output: array('i', [5, 4, 3, 15, 10])
# Descrizione: Inverte l'ordine degli elementi nell'array.

# Nome: Array - Conversione a lista
# Codice:
lst = arr.tolist()
print(lst)  
# Output: [5, 4, 3, 15, 10]
# Descrizione: Converte l'array in una lista.

# Nome: Array - Buffer di memoria
# Codice:
buffer_info = arr.buffer_info()
print(buffer_info)  
# Output: (buffer address, element count)
# Descrizione: Restituisce una tupla con l'indirizzo del buffer e il numero di elementi.

# Nome: Array - Verifica del tipo di elementi
# Codice:
print(arr.typecode)  
# Output: 'i'
# Descrizione: Restituisce il tipo di codice degli elementi nell'array.

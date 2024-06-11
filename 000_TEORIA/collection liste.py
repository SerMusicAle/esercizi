# Nome: Lista - Creazione
# Codice:
my_list = [1, 2, 3]
# Output: [1, 2, 3]
# Descrizione: Crea una lista con gli elementi 1, 2, e 3.

# Nome: Lista - Accesso agli elementi
# Codice:
print(my_list[0])  
# Output: 1
# Descrizione: Accede al primo elemento della lista.

# Nome: Lista - Aggiornamento di un elemento
# Codice:
my_list[0] = 10
print(my_list)  
# Output: [10, 2, 3]
# Descrizione: Aggiorna il primo elemento a 10.

# Nome: Lista - Aggiunta di elementi
# Codice:
my_list.append(4)
print(my_list)  
# Output: [10, 2, 3, 4]
# Descrizione: Aggiunge 4 alla fine della lista.

my_list.extend([5, 6])
print(my_list)  
# Output: [10, 2, 3, 4, 5, 6]
# Descrizione: Estende la lista con gli elementi 5 e 6.

my_list.insert(1, 15)
print(my_list)  
# Output: [10, 15, 2, 3, 4, 5, 6]
# Descrizione: Inserisce 15 alla posizione 1 della lista.

# Nome: Lista - Rimozione di elementi
# Codice:
my_list.remove(15)
print(my_list)  
# Output: [10, 2, 3, 4, 5, 6]
# Descrizione: Rimuove il primo 15 dalla lista.

my_list.pop(1)
print(my_list)  
# Output: [10, 3, 4, 5, 6]
# Descrizione: Rimuove l'elemento alla posizione 1 della lista.

my_list.clear()
print(my_list)  
# Output: []
# Descrizione: Rimuove tutti gli elementi dalla lista.

# Nome: Lista - Ricerca di elementi
# Codice:
my_list = [1, 2, 3, 4, 2]
print(my_list.index(2))  
# Output: 1
# Descrizione: Trova la posizione del primo 2 nella lista.

print(my_list.count(2))  
# Output: 2
# Descrizione: Conta il numero di 2 nella lista.

# Nome: Lista - Ordinamento
# Codice:
my_list.sort()
print(my_list)  
# Output: [1, 2, 2, 3, 4]
# Descrizione: Ordina la lista in ordine crescente.

# Nome: Lista - Reversing
# Codice:
my_list.reverse()
print(my_list)  
# Output: [4, 3, 2, 2, 1]
# Descrizione: Inverte l'ordine degli elementi nella lista.

# Nome: Lista - Slicing
# Codice:
print(my_list[1:4])  
# Output: [3, 2, 2]
# Descrizione: Estrae una sotto-lista dalla posizione 1 alla 3 (inclusi).

# Nome: Lista - Concatenazione
# Codice:
new_list = my_list + [5, 6]
print(new_list)  
# Output: [4, 3, 2, 2, 1, 5, 6]
# Descrizione: Concatena due liste.

# Nome: Lista - Ripetizione
# Codice:
print(my_list * 2)  
# Output: [4, 3, 2, 2, 1, 4, 3, 2, 2, 1]
# Descrizione: Ripete la lista.

# Nome: Lista - Controllo dell'esistenza di un elemento
# Codice:
print(3 in my_list)  
# Output: True
# Descrizione: Controlla se l'elemento 3 è presente nella lista.

# Nome: Lista - Lunghezza
# Codice:
print(len(my_list))  
# Output: 5
# Descrizione: Restituisce la lunghezza della lista.

# Nome: Lista - Creazione
# Codice:
lst = [1, 2, 3]
# Output: [1, 2, 3]
# Descrizione: Crea una lista con elementi 1, 2, e 3.

# Nome: Lista - Accesso agli elementi
# Codice:
print(lst[0])
# Output: 1
# Descrizione: Accede al primo elemento della lista.

# Nome: Lista - Aggiornamento di un elemento
# Codice:
lst[0] = 10
print(lst)
# Output: [10, 2, 3]
# Descrizione: Aggiorna il primo elemento della lista a 10.

# Nome: Lista - Aggiunta di un elemento
# Codice:
lst.append(4)
print(lst)
# Output: [10, 2, 3, 4]
# Descrizione: Aggiunge 4 alla fine della lista.

# Nome: Lista - Inserimento di un elemento
# Codice:
lst.insert(1, 5)
print(lst)
# Output: [10, 5, 2, 3, 4]
# Descrizione: Inserisce 5 alla posizione con indice 1.

# Nome: Lista - Rimozione di un elemento
# Codice:
lst.remove(2)
print(lst)
# Output: [10, 5, 3, 4]
# Descrizione: Rimuove la prima occorrenza del valore 2 nella lista.

# Nome: Lista - Rimozione dell'ultimo elemento
# Codice:
lst.pop()
print(lst)
# Output: [10, 5, 3]
# Descrizione: Rimuove l'ultimo elemento della lista.

# Nome: Lista - Concatenazione di liste
# Codice:
new_lst = lst + [6, 7]
print(new_lst)
# Output: [10, 5, 3, 6, 7]
# Descrizione: Concatenazione di due liste.

# Nome: Lista - Slicing
# Codice:
print(lst[1:3])
# Output: [5, 3]
# Descrizione: Estrae una porzione della lista dall'indice 1 all'indice 2.

# Nome: Lista - Lunghezza
# Codice:
print(len(lst))
# Output: 3
# Descrizione: Restituisce la lunghezza della lista.

# Nome: Lista - Ordinamento
# Codice:
lst.sort()
print(lst)
# Output: [3, 5, 10]
# Descrizione: Ordina gli elementi della lista in ordine crescente.

# Nome: Lista - Inversione dell'ordine
# Codice:
lst.reverse()
print(lst)
# Output: [10, 5, 3]
# Descrizione: Inverte l'ordine degli elementi nella lista.

# Nome: Lista - Contare le occorrenze di un elemento
# Codice:
print(lst.count(5))
# Output: 1
# Descrizione: Conta il numero di volte che il valore 5 appare nella lista.

# Nome: Lista - Trovare l'indice di un elemento
# Codice:
print(lst.index(5))
# Output: 1
# Descrizione: Trova l'indice della prima occorrenza di 5 nella lista.

# Nome: Lista - Copia
# Codice:
copy_lst = lst.copy()
print(copy_lst)
# Output: [10, 5, 3]
# Descrizione: Crea una copia della lista.

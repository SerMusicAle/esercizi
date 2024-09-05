# Nome: Tupla - Creazione
# Codice:
my_tuple = (1, 2, 3)
# Output: (1, 2, 3)
# Descrizione: Crea una tupla con gli elementi 1, 2, e 3.

# Nome: Tupla - Accesso agli elementi
# Codice:
print(my_tuple[0])  
# Output: 1
# Descrizione: Accede al primo elemento della tupla.

# Nome: Tupla - Ricerca di elementi
# Codice:
print(my_tuple.index(2))  
# Output: 1
# Descrizione: Trova la posizione del primo 2 nella tupla.

print(my_tuple.count(2))  
# Output: 1
# Descrizione: Conta il numero di 2 nella tupla.

# Nome: Tupla - Slicing
# Codice:
print(my_tuple[1:3])  
# Output: (2, 3)
# Descrizione: Estrae una sotto-tupla dalla posizione 1 alla 2 (inclusi).

# Nome: Tupla - Concatenazione
# Codice:
new_tuple = my_tuple + (4, 5)
print(new_tuple)  
# Output: (1, 2, 3, 4, 5)
# Descrizione: Concatena due tuple.

# Nome: Tupla - Ripetizione
# Codice:
print(my_tuple * 2)  
# Output: (1, 2, 3, 1, 2, 3)
# Descrizione: Ripete la tupla.

# Nome: Tupla - Controllo dell'esistenza di un elemento
# Codice:
print(3 in my_tuple)  
# Output: True
# Descrizione: Controlla se l'elemento 3 è presente nella tupla.

# Nome: Tupla - Lunghezza
# Codice:
print(len(my_tuple))  
# Output: 3
# Descrizione: Restituisce la lunghezza della tupla.


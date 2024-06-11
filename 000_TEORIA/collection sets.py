# Nome: Set - Creazione
# Codice:
my_set = {1, 2, 3}
# Output: {1, 2, 3}
# Descrizione: Crea un set con gli elementi 1, 2, e 3.

# Nome: Set - Aggiunta di elementi
# Codice:
my_set.add(4)
print(my_set)  
# Output: {1, 2, 3, 4}
# Descrizione: Aggiunge 4 al set.

my_set.update([5, 6])
print(my_set)  
# Output: {1, 2, 3, 4, 5, 6}
# Descrizione: Estende il set con gli elementi 5 e 6.

# Nome: Set - Rimozione di elementi
# Codice:
my_set.remove(6)
print(my_set)  
# Output: {1, 2, 3, 4, 5}
# Descrizione: Rimuove il 6 dal set.

my_set.discard(5)
print(my_set)  
# Output: {1, 2, 3, 4}
# Descrizione: Rimuove il 5 dal set (senza errore se non presente).

my_set.pop()
print(my_set)  
# Output: {2, 3, 4}
# Descrizione: Rimuove un elemento casuale dal set.

my_set.clear()
print(my_set)  
# Output: set()
# Descrizione: Rimuove tutti gli elementi dal set.

# Nome: Set - Unione
# Codice:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  
# Output: {1, 2, 3, 4, 5}
# Descrizione: Unisce due set.

# Nome: Set - Intersezione
# Codice:
print(set1 & set2)  
# Output: {3}
# Descrizione: Trova l'intersezione di due set.

# Nome: Set - Differenza
# Codice:
print(set1 - set2)  
# Output: {1, 2}
# Descrizione: Trova la differenza tra due set.

# Nome: Set - Differenza simmetrica
# Codice:
print(set1 ^ set2)  
# Output: {1, 2, 4, 5}
# Descrizione: Trova la differenza simmetrica tra due set.

# Nome: Set - Controllo dell'esistenza di un elemento
# Codice:
print(2 in set1)  
# Output: True
# Descrizione: Controlla se l'elemento 2 è presente nel set.

# Nome: Set - Sottoinsieme
# Codice:
print(set1.issubset(set2))  
# Output: False


# Nome: Set - Creazione
# Codice:
s = {1, 2, 3}
# Output: {1, 2, 3}
# Descrizione: Crea un set con elementi 1, 2 e 3.

# Nome: Set - Aggiunta di un elemento
# Codice:
s.add(4)
print(s)
# Output: {1, 2, 3, 4}
# Descrizione: Aggiunge 4 al set.

# Nome: Set - Rimozione di un elemento
# Codice:
s.remove(2)
print(s)
# Output: {1, 3, 4}
# Descrizione: Rimuove 2 dal set.

# Nome: Set - Unione di set
# Codice:
s2 = {3, 4, 5}
union_set = s.union(s2)
print(union_set)
# Output: {1, 3, 4, 5}
# Descrizione: Restituisce l'unione di due set.

# Nome: Set - Intersezione di set
# Codice:
intersection_set = s.intersection(s2)
print(intersection_set)
# Output: {3, 4}
# Descrizione: Restituisce l'intersezione di due set.

# Nome: Set - Differenza tra set
# Codice:
difference_set = s.difference(s2)
print(difference_set)
# Output: {1}
# Descrizione: Restituisce la differenza tra due set.

# Nome: Set - Differenza simmetrica
# Codice:
sym_difference_set = s.symmetric_difference(s2)
print(sym_difference_set)
# Output: {1, 5}
# Descrizione: Restituisce la differenza simmetrica tra due set.

# Nome: Set - Sottoset
# Codice:
print(s.issubset({1, 2, 3, 4, 5}))
# Output: True
# Descrizione: Verifica se il set è un sottoinsieme di un altro set.

# Nome: Set - Sovraset
# Codice:
print(s.issuperset({1, 3}))
# Output: True
# Descrizione: Verifica se il set è un sovrainsieme di un altro set.

# Nome: Set - Copia
# Codice:
s_copy = s.copy()
print(s_copy)
# Output: {1, 3, 4}
# Descrizione: Crea una copia del set.

# Nome: Set - Lunghezza
# Codice:
print(len(s))
# Output: 3
# Descrizione: Restituisce il numero di elementi nel set.

# Nome: Set - Iterazione
# Codice:
for elem in s:
    print(elem)
# Output: 1 3 4
# Descrizione: Itera sugli elementi del set.

# Nome: Set - Verifica dell'esistenza di un elemento
# Codice:
print(3 in s)
# Output: True
# Descrizione: Verifica se l'elemento 3 è presente nel set.

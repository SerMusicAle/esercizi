# Nome: Dizionario - Creazione
# Codice:
my_dict = {"a": 1, "b": 2, "c": 3}
# Output: {'a': 1, 'b': 2, 'c': 3}
# Descrizione: Crea un dizionario con le chiavi "a", "b", e "c" e i rispettivi valori 1, 2, e 3.

# Nome: Dizionario - Accesso agli elementi
# Codice:
print(my_dict["a"])
# Output: 1
# Descrizione: Accede al valore corrispondente alla chiave "a".

# Nome: Dizionario - Aggiunta/Aggiornamento di elementi
# Codice:
my_dict["d"] = 4
print(my_dict)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Descrizione: Aggiunge un nuovo elemento o aggiorna il valore di una chiave esistente.

# Nome: Dizionario - Rimozione di elementi
# Codice:
del my_dict["a"]
print(my_dict)
# Output: {'b': 2, 'c': 3, 'd': 4}
# Descrizione: Rimuove un elemento dal dizionario utilizzando la chiave.

my_dict.pop("b")
print(my_dict)
# Output: {'c': 3, 'd': 4}
# Descrizione: Rimuove e restituisce l'elemento corrispondente alla chiave specificata.

my_dict.clear()
print(my_dict)
# Output: {}
# Descrizione: Rimuove tutti gli elementi dal dizionario.

# Nome: Dizionario - Ricerca di elementi
# Codice:
print("a" in my_dict)
# Output: False
# Descrizione: Controlla se una chiave è presente nel dizionario.

# Nome: Dizionario - Lunghezza del dizionario
# Codice:
print(len(my_dict))
# Output: 0
# Descrizione: Restituisce il numero di coppie chiave-valore nel dizionario.

# Nome: Dizionario - Iterazione sulle chiavi
# Codice:
for key in my_dict:
    print(key)
# Output: 'c' 'd'
# Descrizione: Itera sulle chiavi del dizionario.

# Nome: Dizionario - Iterazione sui valori
# Codice:
for value in my_dict.values():
    print(value)
# Output: 3 4
# Descrizione: Itera sui valori del dizionario.

# Nome: Dizionario - Iterazione sugli elementi
# Codice:
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output: 'c': 3 'd': 4
# Descrizione: Itera sulle coppie chiave-valore del dizionario.

# Nome: Dizionario - Unione di dizionari
# Codice:
d2 = {'e': 5, 'f': 6}
my_dict.update(d2)
print(my_dict)
# Output: {'c': 3, 'd': 4, 'e': 5, 'f': 6}
# Descrizione: Unisce il dizionario my_dict con d2.

# Nome: Dizionario - Recupero di un valore con default
# Codice:
print(my_dict.get('e', 0))
# Output: 5
# Descrizione: Recupera il valore associato alla chiave 'e' o restituisce 0 se la chiave non esiste.

# Nome: Dizionario - Estrazione di un elemento
# Codice:
value = my_dict.pop('e', 'Chiave non trovata')
print(value)
# Output: 5
# Descrizione: Rimuove e restituisce il valore associato alla chiave 'e'. Se la chiave non esiste, restituisce 'Chiave non trovata'.

# Nome: Dizionario - Creazione di un dizionario da liste
# Codice:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)
# Output: {'a': 1, 'b': 2, 'c': 3}
# Descrizione: Crea un dizionario dalle liste keys e values.

# Nome: Dizionario - Creazione di un dizionario con valori di default
# Codice:
keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys, 0)
print(my_dict)
# Output: {'a': 0, 'b': 0, 'c': 0}
# Descrizione: Crea un dizionario con le chiavi specificate e valori di default.

# Nome: Dizionario - Copia di un dizionario
# Codice:
my_dict_copy = my_dict.copy()
print(my_dict_copy)
# Output: {'a': 1, 'b': 2, 'c': 3}
# Descrizione: Crea una copia superficiale del dizionario.

# Nome: Dizionario - Aggiornamento di un dizionario con un'altra chiave-valore
# Codice:
my_dict.update({'g': 7})
print(my_dict)
# Output: {'a': 1

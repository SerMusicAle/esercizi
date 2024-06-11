from collections import Counter

# Nome: Counter - Creazione
# Codice:
count = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# Output: Counter({'b': 3, 'a': 2, 'c': 1})
# Descrizione: Crea un Counter con il conteggio degli elementi nella lista.

# Nome: Counter - Accesso agli elementi
# Codice:
print(count['a'])
# Output: 2
# Descrizione: Restituisce il conteggio dell'elemento 'a'.

# Nome: Counter - Aggiunta di elementi
# Codice:
count.update(['a', 'd', 'd'])
print(count)
# Output: Counter({'b': 3, 'a': 3, 'd': 2, 'c': 1})
# Descrizione: Aggiunge elementi al Counter e aggiorna i conteggi.

# Nome: Counter - Rimozione di elementi
# Codice:
count.subtract(['a', 'b'])
print(count)
# Output: Counter({'b': 2, 'a': 2, 'd': 2, 'c': 1})
# Descrizione: Sottrae il conteggio degli elementi nel Counter.

# Nome: Counter - Elementi più comuni
# Codice:
print(count.most_common(2))
# Output: [('b', 2), ('a', 2)]
# Descrizione: Restituisce una lista degli n elementi più comuni e i loro conteggi.

# Nome: Counter - Convertire in lista
# Codice:
elements = list(count.elements())
print(elements)
# Output: ['a', 'a', 'b', 'b', 'c', 'd', 'd']
# Descrizione: Restituisce una lista di tutti gli elementi nel Counter.

# Nome: Counter - Concatenazione di Counter
# Codice:
new_count = count + Counter(['a', 'b'])
print(new_count)
# Output: Counter({'a': 3, 'b': 3, 'd': 2, 'c': 1})
# Descrizione: Somma due Counter.

# Nome: Counter - Sottrazione di Counter
# Codice:
new_count = count - Counter(['a', 'b'])
print(new_count)
# Output: Counter({'d': 2, 'c': 1, 'b': 1, 'a': 1})
# Descrizione: Sottrae un Counter da un altro.

# Nome: Counter - Intersezione di Counter
# Codice:
new_count = count & Counter(['a', 'b', 'c'])
print(new_count)
# Output: Counter({'a': 2, 'b': 2, 'c': 1})
# Descrizione: Intersezione di due Counter.

# Nome: Counter - Unione di Counter
# Codice:
new_count = count | Counter(['a', 'b', 'c', 'd', 'e'])
print(new_count)
# Output: Counter({'a': 2, 'b': 2, 'd': 2, 'c': 1, 'e': 1})
# Descrizione: Unisce due Counter mantenendo il conteggio massimo per ciascun elemento.

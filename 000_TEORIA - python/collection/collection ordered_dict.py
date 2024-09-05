from collections import OrderedDict

# Nome: OrderedDict - Creazione
# Codice:
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Descrizione: Crea un OrderedDict con coppie chiave-valore 'a': 1, 'b': 2, 'c': 3.

# Nome: OrderedDict - Accesso agli elementi
# Codice:
print(od['a'])
# Output: 1
# Descrizione: Accede al valore associato alla chiave 'a'.

# Nome: OrderedDict - Aggiunta di un nuovo elemento
# Codice:
od['d'] = 4
print(od)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# Descrizione: Aggiunge una nuova coppia chiave-valore 'd': 4 all'OrderedDict.

# Nome: OrderedDict - Iterazione sugli elementi
# Codice:
for key, value in od.items():
    print(key, value)
# Output: a 1, b 2, c 3, d 4
# Descrizione: Itera sulle coppie chiave-valore dell'OrderedDict.

# Nome: OrderedDict - Rimozione dell'ultimo elemento
# Codice:
od.popitem()
print(od)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Descrizione: Rimuove l'ultima coppia chiave-valore dall'OrderedDict.

# Nome: OrderedDict - Spostare elemento alla fine
# Codice:
od.move_to_end('a')
print(od)
# Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])
# Descrizione: Sposta la coppia chiave-valore con chiave 'a' alla fine dell'OrderedDict.

# Nome: OrderedDict - Spostare elemento all'inizio
# Codice:
od.move_to_end('a', last=False)
print(od)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Descrizione: Sposta la coppia chiave-valore con chiave 'a' all'inizio dell'OrderedDict.

# Nome: OrderedDict - Copia
# Codice:
od_copy = od.copy()
print(od_copy)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# Descrizione: Crea una copia dell'OrderedDict.

# Nome: OrderedDict - Verifica dell'esistenza di una chiave
# Codice:
print('a' in od)
# Output: True
# Descrizione: Verifica se la chiave 'a' è presente nell'OrderedDict.

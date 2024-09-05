from collections import deque

# Nome: Deque - Creazione
# Codice:
dq = deque([1, 2, 3])
# Output: deque([1, 2, 3])
# Descrizione: Crea una deque con elementi 1, 2, e 3.

# Nome: Deque - Aggiunta di elementi a destra
# Codice:
dq.append(4)
print(dq)
# Output: deque([1, 2, 3, 4])
# Descrizione: Aggiunge 4 alla fine della deque.

# Nome: Deque - Aggiunta di elementi a sinistra
# Codice:
dq.appendleft(0)
print(dq)
# Output: deque([0, 1, 2, 3, 4])
# Descrizione: Aggiunge 0 all'inizio della deque.

# Nome: Deque - Rimozione di elementi da destra
# Codice:
dq.pop()
print(dq)
# Output: deque([0, 1, 2, 3])
# Descrizione: Rimuove l'ultimo elemento dalla deque.

# Nome: Deque - Rimozione di elementi da sinistra
# Codice:
dq.popleft()
print(dq)
# Output: deque([1, 2, 3])
# Descrizione: Rimuove il primo elemento dalla deque.

# Nome: Deque - Estensione della deque a destra
# Codice:
dq.extend([4, 5])
print(dq)
# Output: deque([1, 2, 3, 4, 5])
# Descrizione: Aggiunge 4 e 5 alla fine della deque.

# Nome: Deque - Estensione della deque a sinistra
# Codice:
dq.extendleft([0, -1])
print(dq)
# Output: deque([-1, 0, 1, 2, 3, 4, 5])
# Descrizione: Aggiunge -1 e 0 all'inizio della deque.

# Nome: Deque - Rotazione della deque
# Codice:
dq.rotate(2)
print(dq)
# Output: deque([4, 5, -1, 0, 1, 2, 3])
# Descrizione: Ruota la deque di 2 posizioni verso destra.

# Nome: Deque - Inversione della deque
# Codice:
dq.reverse()
print(dq)
# Output: deque([3, 2, 1, 0, -1, 5, 4])
# Descrizione: Inverte l'ordine degli elementi nella deque.

# Nome: Deque - Svuotamento della deque
# Codice:
dq.clear()
print(dq)
# Output: deque([])
# Descrizione: Rimuove tutti gli elementi dalla deque.

# Nome: Deque - Conteggio degli elementi
# Codice:
dq = deque([1, 2, 2, 3, 4])
print(dq.count(2))
# Output: 2
# Descrizione: Conta il numero di occorrenze di un elemento nella deque.

from collections import deque

# Nome: Deque - Creazione
# Codice:
dq = deque([1, 2, 3])
# Output: deque([1, 2, 3])
# Descrizione: Crea una deque con elementi 1, 2, e 3.

# Nome: Deque - Aggiunta di elementi a destra
# Codice:
dq.append(4)
print(dq)
# Output: deque([1, 2, 3, 4])
# Descrizione: Aggiunge 4 alla fine della deque.

# Nome: Deque - Aggiunta di elementi a sinistra
# Codice:
dq.appendleft(0)
print(dq)
# Output: deque([0, 1, 2, 3, 4])
# Descrizione: Aggiunge 0 all'inizio della deque.

# Nome: Deque - Rimozione di elementi da destra
# Codice:
dq.pop()
print(dq)
# Output: deque([0, 1, 2, 3])
# Descrizione: Rimuove l'ultimo elemento dalla deque.

# Nome: Deque - Rimozione di elementi da sinistra
# Codice:
dq.popleft()
print(dq)
# Output: deque([1, 2, 3])
# Descrizione: Rimuove il primo elemento dalla deque.

# Nome: Deque - Estensione della deque a destra
# Codice:
dq.extend([4, 5])
print(dq)
# Output: deque([1, 2, 3, 4, 5])
# Descrizione: Aggiunge 4 e 5 alla fine della deque.

# Nome: Deque - Estensione della deque a sinistra
# Codice:
dq.extendleft([0, -1])
print(dq)
# Output: deque([-1, 0, 1, 2, 3, 4, 5])
# Descrizione: Aggiunge -1 e 0 all'inizio della deque.

# Nome: Deque - Rotazione della deque
# Codice:
dq.rotate(2)
print(dq)
# Output: deque([4, 5, -1, 0, 1, 2, 3])
# Descrizione: Ruota la deque di 2 posizioni verso destra.

# Nome: Deque - Inversione della deque
# Codice:
dq.reverse()
print(dq)
# Output: deque([3, 2, 1, 0, -1, 5, 4])
# Descrizione: Inverte l'ordine degli elementi nella deque.

# Nome: Deque - Svuotamento della deque
# Codice:
dq.clear()
print(dq)
# Output: deque([])
# Descrizione: Rimuove tutti gli elementi dalla deque.

# Nome: Deque - Conteggio degli elementi
# Codice:
dq = deque([1, 2, 2, 3, 4])
print(dq.count(2))
# Output: 2
# Descrizione: Conta il numero di occorrenze di un elemento nella deque.

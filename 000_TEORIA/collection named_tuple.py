from collections import namedtuple

# Creazione di una named tuple
Person = namedtuple('Person', 'name age')
person = Person(name="Alice", age=30)

# Accesso agli elementi
print(person.name)  # Output: Alice
print(person[1])  # Output: 30

# Ricerca di elementi
print(person.index(30))  # Output: 1
print(person.count(30))  # Output: 1

# Slicing
print(person[0:2])  # Output: ('Alice', 30)

# Concatenazione
new_person = person + ("Engineer",)
print(new_person)  # Output: ('Alice', 30, 'Engineer')

# Ripetizione
print(person * 2)  # Output: ('Alice', 30, 'Alice', 30)

# Controllo dell'esistenza di un elemento
print("Alice" in person)  # Output: True

# Lunghezza
print(len(person))  # Output: 2

from collections import namedtuple

# Nome: NamedTuple - Creazione e Accesso agli elementi
# Codice:
Point = namedtuple('Point', 'x y')
p = Point(11, 22)
print(p)
# Output: Point(x=11, y=22)
# Descrizione: Crea una named tuple 'Point' con campi 'x' e 'y' e li inizializza con valori 11 e 22.

# Nome: NamedTuple - Accesso per nome
# Codice:
print(p.x, p.y)
# Output: 11 22
# Descrizione: Accede ai valori dei campi 'x' e 'y' per nome.

# Nome: NamedTuple - Accesso per indice
# Codice:
print(p[0], p[1])
# Output: 11 22
# Descrizione: Accede ai valori dei campi 'x' e 'y' per indice.

# Nome: NamedTuple - Conversione a dizionario
# Codice:
print(p._asdict())
# Output: {'x': 11, 'y': 22}
# Descrizione: Converte la named tuple in un dizionario.

# Nome: NamedTuple - Sostituzione di valori
# Codice:
p = p._replace(x=33)
print(p)
# Output: Point(x=33, y=22)
# Descrizione: Crea una nuova named tuple sostituendo il valore del campo 'x'.

# Nome: NamedTuple - Creazione da lista
# Codice:
p = Point._make([44, 55])
print(p)
# Output: Point(x=44, y=55)
# Descrizione: Crea una named tuple dai valori in una lista.

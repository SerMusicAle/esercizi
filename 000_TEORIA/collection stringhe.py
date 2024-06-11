# Creazione di una stringa
my_string = "hello world"

# Accesso ai caratteri
print(my_string[0])  # Output: h

# Concatenazione
new_string = my_string + "!"
print(new_string)  # Output: hello world!

# Ripetizione
print(my_string * 2)  # Output: hello worldhello world

# Slicing
print(my_string[0:5])  # Output: hello

# Ricerca di sottostringhe
print(my_string.find("world"))  # Output: 6
print(my_string.count("l"))  # Output: 3

# Sostituzione
print(my_string.replace("world", "there"))  # Output: hello there

# Dividere
print(my_string.split(" "))  # Output: ['hello', 'world']

# Unire
print(" ".join(['hello', 'world']))  # Output: hello world

# Cambiare caso
print(my_string.upper())  # Output: HELLO WORLD
print(my_string.lower())  # Output: hello world

# Rimuovere spazi
print(" hello ".strip())  # Output: hello

# Controllo dell'esistenza di una sottostringa
print("world" in my_string)  # Output: True

# Lunghezza
print(len(my_string))  # Output: 11
# Nome: Stringa - Creazione
# Codice:
s = "Hello, World!"
# Output: Hello, World!
# Descrizione: Crea una stringa.

# Nome: Stringa - Accesso ai caratteri
# Codice:
print(s[0])
# Output: H
# Descrizione: Accede al primo carattere della stringa.

# Nome: Stringa - Slicing
# Codice:
print(s[0:5])
# Output: Hello
# Descrizione: Estrae una sottostringa dall'indice 0 all'indice 4.

# Nome: Stringa - Lunghezza
# Codice:
print(len(s))
# Output: 13
# Descrizione: Restituisce la lunghezza della stringa.

# Nome: Stringa - Concatenazione
# Codice:
s2 = s + " How are you?"
print(s2)
# Output: Hello, World! How are you?
# Descrizione: Concatenazione di due stringhe.

# Nome: Stringa - Ripetizione
# Codice:
print(s * 2)
# Output: Hello, World!Hello, World!
# Descrizione: Ripete la stringa due volte.

# Nome: Stringa - Conversione a maiuscolo
# Codice:
print(s.upper())
# Output: HELLO, WORLD!
# Descrizione: Converte tutti i caratteri della stringa in maiuscolo.

# Nome: Stringa - Conversione a minuscolo
# Codice:
print(s.lower())
# Output: hello, world!
# Descrizione: Converte tutti i caratteri della stringa in minuscolo.

# Nome: Stringa - Suddivisione
# Codice:
print(s.split(','))
# Output: ['Hello', ' World!']
# Descrizione: Divide la stringa in una lista di sottostringhe usando ',' come delimitatore.

# Nome: Stringa - Sostituzione
# Codice:
print(s.replace('World', 'Python'))
# Output: Hello, Python!
# Descrizione: Sostituisce tutte le occorrenze della sottostringa 'World' con 'Python'.

# Nome: Stringa - Trovare una sottostringa
# Codice:
print(s.find('World'))
# Output: 7
# Descrizione: Restituisce l'indice della prima occorrenza della sottostringa 'World'.

# Nome: Stringa - Verifica prefisso
# Codice:
print(s.startswith('Hello'))
# Output: True
# Descrizione: Verifica se la stringa inizia con 'Hello'.

# Nome: Stringa - Verifica suffisso
# Codice:
print(s.endswith('!'))
# Output: True
# Descrizione: Verifica se la stringa termina con '!'.


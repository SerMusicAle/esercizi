# Nome: Int -> Float
my_int = 5
my_float = float(my_int)
print(my_float)  
# Output: 5.0
# Descrizione: Converte un numero intero (int) in un numero con la virgola (float).

# Nome: Float -> Int
my_float = 3.7
my_int = int(my_float)
print(my_int)  
# Output: 3
# Descrizione: Converte un numero con la virgola (float) in un numero intero (int) arrotondando per difetto.

# Nome: String -> Int
my_string = "10"
my_int = int(my_string)
print(my_int)  
# Output: 10
# Descrizione: Converte una stringa numerica (string) in un numero intero (int).

# Nome: Int -> String
my_int = 123
my_string = str(my_int)
print(my_string)  
# Output: "123"
# Descrizione: Converte un numero intero (int) in una stringa (string).

# Nome: String -> Float
my_string = "3.14"
my_float = float(my_string)
print(my_float)  
# Output: 3.14
# Descrizione: Converte una stringa numerica con decimali (string) in un numero float.

# Nome: Float -> String
my_float = 9.81
my_string = str(my_float)
print(my_string)  
# Output: "9.81"
# Descrizione: Converte un numero float in una stringa (string).

# Nome: String -> Lista
my_string = "apple,banana,orange"
my_list = my_string.split(',')
print(my_list)  
# Output: ['apple', 'banana', 'orange']
# Descrizione: Converte una stringa in una lista, separando gli elementi con una virgola.

# Nome: Lista -> String
my_list = ['apple', 'banana', 'orange']
my_string = ','.join(my_list)
print(my_string)  
# Output: "apple,banana,orange"
# Descrizione: Converte una lista di stringhe in una singola stringa, unendo gli elementi con una virgola.

# Nome: Lista -> Set
my_list = [1, 2, 2, 3, 3]
my_set = set(my_list)
print(my_set)  
# Output: {1, 2, 3}
# Descrizione: Converte una lista in un set, rimuovendo i duplicati.

# Nome: Set -> Lista
my_set = {1, 2, 3}
my_list = list(my_set)
print(my_list)  
# Output: [1, 2, 3]
# Descrizione: Converte un set in una lista.

# Nome: Int -> Bool
my_int = 0
my_bool = bool(my_int)
print(my_bool)  
# Output: False
# Descrizione: Converte un numero intero in un valore booleano. Zero diventa False, qualsiasi altro valore diventa True.

# Nome: Bool -> Int
my_bool = True
my_int = int(my_bool)
print(my_int)  
# Output: 1
# Descrizione: Converte un valore booleano (True o False) in un numero intero. True diventa 1, False diventa 0.

# Nome: Tuple -> Lista
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  
# Output: [1, 2, 3]
# Descrizione: Converte una tupla (tuple) in una lista (list).

# Nome: Lista -> Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  
# Output: (1, 2, 3)
# Descrizione: Converte una lista in una tupla.

# Nome: Dict -> Lista (chiavi)
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_keys = list(my_dict.keys())
print(my_keys)  
# Output: ['a', 'b', 'c']
# Descrizione: Converte le chiavi di un dizionario in una lista.

# Nome: Dict -> Lista (valori)
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_values = list(my_dict.values())
print(my_values)  
# Output: [1, 2, 3]
# Descrizione: Converte i valori di un dizionario in una lista.

# Nome: Lista -> Dict (con enumerazione)
my_list = ['apple', 'banana', 'orange']
my_dict = dict(enumerate(my_list))
print(my_dict)  
# Output: {0: 'apple', 1: 'banana', 2: 'orange'}
# Descrizione: Converte una lista in un dizionario con indici come chiavi.

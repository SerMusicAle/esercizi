"""
Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:

Test	Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}
"""

def merge_dictionaries(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    dictunico: dict[str, int] = {}
    
    # Aggiungi tutte le coppie chiave-valore da dict1 a dictunico
    for chiave1, valore1 in dict1.items():
        dictunico[chiave1] = valore1
    
    # Aggiorna dictunico con le coppie chiave-valore di dict2
    for chiave2, valore2 in dict2.items():
        if chiave2 in dictunico:
            dictunico[chiave2] += valore2
        else:
            dictunico[chiave2] = valore2
    
    return dictunico

"""
Q_2 
    Scrivi una funzione che inverte le chiavi e i valori in un dizionario. 
    Se ci sono valori duplicati, scarta i duplicati.
"""

def invertedkey (dizionario:dict[str,int]):

    __dizionario2:dict = {}
    
    for chiave,valore in dizionario.items():
        if valore not in __dizionario2:
            __dizionario2[valore] = chiave
            
    return __dizionario2

dizionario: dict = {"a":1, "b":2, "c":3, "d":1}
print (invertedkey(dizionario)) 
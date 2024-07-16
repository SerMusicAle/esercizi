"""
    funzione che 
        prende una lista di numeri
        ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
"""

def f_paridispari(numeri: list[int]):
    __pari:list[int] = []
    __dispari:list[int] = []
    i:int
    
    ordinamento:dict[str,list[int]] = {"dispari": __dispari, "pari": __pari}
    
    for i in numeri:
        if i%2 == 0:
            __pari.append (i)
        else:
            __dispari.append (i)
    
    return ordinamento

numeri: list[int] = [1,2,3,4,5,6]
risultato = f_paridispari(numeri)
print(risultato)
    
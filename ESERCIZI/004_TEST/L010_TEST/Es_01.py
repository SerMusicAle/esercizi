"""
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
"""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
    #DEC
    padis: dict = {"pari": [], "dispari": []}

    #BODY
    for numero in lista:
        if numero % 2 == 0:
            padis["pari"].append(numero)
        else:
            padis["dispari"].append(numero)
    return (padis)
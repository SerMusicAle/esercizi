"""
Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.
"""


def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:

    #DEC
    dizionario_invertito = {}
    
    #BODY
    for chiave, valore in dizionario.items():
        if valore not in dizionario_invertito.keys():
            dizionario_invertito[valore] = chiave
            
    
    #RETURN        
    return dizionario_invertito

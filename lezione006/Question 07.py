"""
ASSEGNAZIONE
Scrivi una funzione che verifica se in una stringa le parentesi 
'(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

"""


def check_parentheses(expression: str) -> bool:
    
    count = 0
    
    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        
        if count < 0:
            return False

    return count == 0
        

"""
CONSEGNA

ERRORE
la corrispondenza dei risultati c'è se l'ultimo if è all'interno del for,
ma se la stringsa comincia con parentesi chiuse va in false subito non 
consentendo al ciclo di proseguire il calcolo e verificare il risultato 
finale. questo presuppone che le parentesi non debbano solo essere in 
quantità bilanciate ma che siano logicamente disposte. 



def check_parentheses(expression: str) -> bool:
    
    count = 0
    
    for char in expression:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        
        if count < 0:
            return False

    return count == 0
        


"""
"""
CONSEGNA
4. Scrivi una funzione che determina se un numero è 'magico'. 
Un numero è considerato magico se è divisibile per 4 ma non per 6.
"""

def magico (numero):

    #BODY
    if numero%4 == 0 and numero%6 != 0:
        risposta = (f"{numero} è un numero magico")
    else:
        risposta = (f"{numero} non è un numero magico")
    
    print(risposta)

#CALL
magico(8)


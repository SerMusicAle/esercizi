"""
CONSEGNA
9. Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
"""

def convertitore (listadati):
    
    #INIT
    abbinamenti: dict = {}

    #BODY
    for chiave, valore in listadati:
        if chiave in abbinamenti:
            abbinamenti[chiave].append(valore)
        else:
            abbinamenti[chiave] = [valore]
    print(f"gli elementi del dizionario sono")
    for chiave, valore in abbinamenti.items():
        valori_str = ", ".join(valore)
        print (f"a {chiave} corrisponde/corrispondono: {valori_str}")

#INPUT
listadati = [
    (1, 'a'), 
    (2, 'b'), 
    (2, 'c'), 
    (3, 'd'), 
    (3, 'e'), 
    (3, 'f'), 
    (4, 'g'), 
    (4, 'h'), 
    (4, 'i'), 
    (4, 'j'), 
    (5, 'k'), 
    (5, 'l'), 
    (5, 'm'), 
    (5, 'n'), 
    (5, 'o')
]


#CALL
convertitore (listadati)
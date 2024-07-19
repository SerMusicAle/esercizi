"""
Q5
    Scrivi una funzione che 
        accetti un dizionario di prodotti con i prezzi 
        e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
    
    For example:

    Test	Result
    print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
    {'Zaino': 45.0, 'Quaderno': 19.8}
    print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
    {}
"""

def prodotti_prezzo(prodotti:dict [str,float]):
#INIT
    pricemin20:dict [str,float] = {}
    
#BODY
    for chiave, valore in prodotti.items():
        if valore >= 20.0:
            pricemin20[chiave] = valore

    return pricemin20
            
            
    
    
    
prodotti: dict[str,float] = {'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}
print (prodotti_prezzo(prodotti))
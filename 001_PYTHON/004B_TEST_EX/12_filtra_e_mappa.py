"""
    funzione(prodotti:dict) 
        return nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.
    For example:

        Test	Result
        print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
        {'Zaino': 45.0, 'Quaderno': 19.8}
        print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
    
    ris1 = filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})
print(ris1)

ris2 = filtra_e_mappa({'Zaino': 45.0, 'Quaderno': 19.8})
print (ris2)
    """
    
    
def filtra_e_mappa(prodotti: dict[str,float]) -> dict[str,float]:
    # cancella pass e scrivi il tuo codice
    nuovodic:dict[str,float] = {}
    for prodotto in prodotti:
        if prodotti[prodotto] > 20:
            nuovodic[prodotto] = prodotti[prodotto] * 0.9
    return nuovodic





"""
CONSEGNA
6. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

"""


def f_price (price):

    #INIT
    saldi = {}

    #BODY
    for prodotto,prezzo in price.items():
        if prezzo > 20:
            saldo = prezzo*0.9
            saldi[prodotto] = saldo
    
    offerta = print(f"la nuova lista prodotti è: \n")
    for prodotto,prezzo in price.items():
        print (f"{prodotto} costa {prezzo}")



#CALL
f_price({
    "panino": 20.99,
    "insalata": 4.49,
    "pizza": 8.99,
    "bibita": 23.99,
    "gelato": 3.49
})


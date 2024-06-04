"""
CONSEGNA
17. Scrivi una funzione che 
- calcola la media di una lista di numeri 
- ritorna il valore arrotondato all'intero più vicino.
"""


def f_media():


#INIT
    numeri: int = [1,2,3,4,5,6,7,8,9]
    tot = 0

#BODY
    for i in numeri:
        tot +=i
    
#RETURN
    print(f"il valore medio approssimato è: {round(tot/len(numeri))}")

#INPUT



#CALL
f_media()
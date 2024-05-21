"""
CONSEGNA
10. Scrivi una funzione che:
- prende una lista di numeri 
- ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
"""

def classifica (listanum):

#INIT
    orddict: dict = {"pari": [], "dispari": []}

#BODY
    for number in listanum:
        if number%2 == 0:
            orddict["pari"].append(number)
        else:
            orddict["dispari"].append(number)
    
    printpari = ", ".join(map(str, orddict["pari"]))
    printdispari = ", ".join(map(str, orddict["dispari"]))
    print(f"i numeri pari sono: ", printpari)
    print(f"i numeri dispari sono: ", printdispari)

#INPUT
listanum:list = [1,2,3,4,5,6,7,8,9]

#CALL
classifica(listanum)
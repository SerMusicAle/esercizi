"""
CONSEGNA
16. Scrivi una funzione che 
- ritorna il valore massimo, 
- valore minimo 
- velore medio di una lista di numeri interi.
"""


def ritorno():

#INIT
    lista:list = [1,2,3,4,5,6,7,8,9]
    tot = 0
#BODY
    for i in lista:
        tot+=i
    media = tot/len(lista)
#RETURN
    print(f"il minimo della lista è {min(lista)}, il massimo della lista è {max(lista)} e il valore medio della lista è {media}")

#INPUT


#CALL
ritorno()
"""
CONSEGNA
13. Scrivi una funzione che, 
- data una lista, 
ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

"""

def freqinlista ():

#INIT
    lista: list = [1,2,3,4,5,4,5,4,3,5,6,7,2,4,5,]
    counter: dict = {}

#BODY
    for i in lista:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for m,n in counter.items():
        print (f"{m} è contenuto nella lista {n} volte")

#INPUT  

#CALL
freqinlista ()

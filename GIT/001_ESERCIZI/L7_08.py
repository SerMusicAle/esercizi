"""
CONSEGNA
8. Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

"""

def f_menodati (listadati, rimozione):

    #BODY
    for num,quantity in rimozione.items():
        i = 0
        while i < quantity:
            if num in listadati:
                listadati.remove(num)
                i +=1
    print (listadati)

#INPUT
listadati: list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
rimozione: dict = {2:1, 3:2, 4:3, 5:4}

#CALL
f_menodati(listadati, rimozione)
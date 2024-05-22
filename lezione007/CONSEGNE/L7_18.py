"""
CONSEGNA
18. Scrivi una funzione che 
- rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.

"""


def removecopy():

#INIT
    lista:list = [1,2,2,3,3,4,4,5,6,7, "a","s","s","d","d","f","g","h","j","j"]
    listaunivoca:list = []

#BODY
    [listaunivoca.append(i) for i in lista if i not in listaunivoca]

#RETURN
    print(f"la lista pulita è: "+ ", ".join(str(i) for i in listaunivoca))
        

#CALL
removecopy()
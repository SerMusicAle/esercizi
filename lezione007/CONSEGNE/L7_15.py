"""
CONSEGNA
15. Scrivi una funzione che, 
- dato un insieme e una lista di numeri interi da rimuovere, 
- ritorni un nuovo insieme senza i numeri specificati nella lista.

"""

def insiememinor (rimuovere):


#INIT
    interi: list = [1,2,3,4,5,6,7,8,9]

#BODY
    for i in rimuovere:
        if i in interi:
            interi.remove(i)

#RETURN
    print(f"la nuova lista è: {', '.join(str(i) for i in interi)}")

#INPUT
rimuovere: list = [1,3,5,7,9]

#CALL
insiememinor(rimuovere)

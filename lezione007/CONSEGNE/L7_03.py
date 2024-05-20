"""
CONSEGNA
3. Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, 
e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.
"""


def filter():

     #INIT
    pari:list = [2,4,6,8]

     #BODY
    fattore = int(input(f"per quale numero vuoi moltiplicare i numeri della lista?"))
    print(f"la nuova lista è: ")
    for i in (pari):
        i*=fattore
        print (i)

#CALL    
filter()
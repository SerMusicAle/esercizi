"""
CONSEGNA
14. Scrivi una funzione che
- ritorna un dizionario che unisce due dizionari. 
- Se una chiave è presente in entrambi, somma i loro valori nel nuovo dizionario.

"""

def dictuniti (dizionario1, dizionario2):

#INIT


#BODY
    for chiave, valore in dizionario2.items():
        if chiave in dizionario1:
            dizionario1[chiave] += valore
        else:
            dizionario1[chiave] = valore

    print (f"il nuovo dizionario è: ")
    for chiave, valore in dizionario1:
        print (f"{chiave} = {valore}")
#INPUT
dizionario1: dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

dizionario2: dict = {
    "c": 30,
    "d": 40,
    "e": 50,
    "f": 60
}

#CALL
dictuniti(dizionario1, dizionario2)
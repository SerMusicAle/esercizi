"""
CONSEGNA
2. Scrivi una funzione che inverte le chiavi e i valori in un dizionario.
Se ci sono valori duplicati, scarta i duplicati.

"""
def f_inversioneKV ():
    
    #DEC
    diz_originale = {"uno": 1, "due": 2, "tre": 3}
    diz_invertito = {}

    #BODY
    for chiave,valore in diz_originale.items():
        diz_invertito[valore] = chiave
    print (f"il dizionario invertito contiene ")
    for k,v in diz_invertito.items():
        print (f"{k} : {v}")

#CALL
f_inversioneKV()
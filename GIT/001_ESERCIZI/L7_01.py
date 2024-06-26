"""
CONSEGNA
1. Scrivi una funzione che prenda un dizionario e un valore, 
e ritorni la prima chiave che corrisponde a quel valore, 
o None se il valore non è presente.

"""

def f_diz_val(dizionario:dict, valore:int):
    
    #DEC
    contatore:int = 0
    
    #BODY
    for chiave, val in dizionario.items():
        if val == valore:
            print(f"il valore {valore} era sotto la chiave {chiave}")

#INPUT
dizionario = {"uno": 1, "due": 2, "tre": 3}
valore = 2

#RETURN
f_diz_val(dizionario, valore)
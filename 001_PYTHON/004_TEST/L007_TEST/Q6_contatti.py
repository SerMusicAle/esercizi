"""
PARTE 1
    create_contact() 
        che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). 
        La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
    
PARTE 2
    update_contact() 
        che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. 
        Questa funzione dovrebbe aggiornare il dizionario del contatto.
    


"""
from typing import Union
         
def f_create_contact(nome:str, cognome:str, email:str = "", telefono:int = 0):
#INIT
    dati:dict[str, Union[str, int]] = {"nome": nome, "cognome": cognome, "e-mail": email, "telefono": telefono}
    return dati
    
def f_update_contact(dati:dict[str,Union[str,int]], nome:str = "", cognome:str = "", email:str = "", telefono:int = 0):
#INIT
    if nome:
        dati["nome"] = nome
    if cognome:
        dati["cognome"] = cognome
    if email:
        dati["e-mail"] = email
    if telefono:
        dati["telefono"] = telefono
    
    return dati
#EXE
contatto = f_create_contact("Mario", "Rossi", "mario.rossi@gmail.com", 3333333333)

contatto_aggiornato = f_update_contact(contatto, "Mario", "Rossi", telefono=123456789)

print (contatto_aggiornato)
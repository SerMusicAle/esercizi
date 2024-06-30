#DESCRIPTION FUNCTION
"""
"3-2. Saluti: 
    Parti dalla lista che hai usato nell'Esercizio 3-1, 
    invece di stampare solo il nome di ogni persona, 
    stampa un messaggio personalizzato per ognuna di loro. 
    Il testo di ciascun messaggio dovrebbe essere lo stesso, 
    ma ogni messaggio dovrebbe essere personalizzato con il nome della persona."
"""

class Names ():
#INIT
    def __init__ (self, nomi:list[str]):
        self.__lista_nomi = nomi
        self.messaggi: dict[str, str] = {}
        
    def f_stampa (self):
        
        for nome in self.__lista_nomi:
            self.messaggi [nome] = f"ciao {nome}, benvenuto tra i miei amici"


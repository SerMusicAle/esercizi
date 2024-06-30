
"""
2.5 Famous Quote
    trova una citazione di una persona che ammiri
    stampa citazione e nome autore    
"""

class FamousQuote ():
#INIT
    def __init__(self):
        self.__vips: dict  [str,str]= {
            'Einstein':'la vita è come una bicicletta', 
            'Mandela':'La istruzione è l\'arma più potente', 
            'Jobs':'Stay hungry, stay foolish'
        }
#BODY
    def f_quotes (self, vip:str):
        
        if vip in self.__vips:
        #if self.__vips[vip]: #non più corrispondente ma se esiste fa...
            quote: str = (f"{vip} una volta disse: \"{self.__vips[vip]}\"")
            return quote
        else: 
            return (f"inserisci il nome corretto")


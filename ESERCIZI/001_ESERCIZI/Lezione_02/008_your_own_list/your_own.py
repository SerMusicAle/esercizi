"""
3-3. La tua lista personale: 
    Pensa al tuo mezzo di trasporto preferito, come una motocicletta o un'auto, 
    crea una lista che contenga diversi esempi. 
    Usa la tua lista per stampare una serie di affermazioni su questi elementi, 
    come "Mi piacerebbe possedere una motocicletta Honda".
    
"""

class YourOwn ():
#INIT
    def __init__ (self, mezzi: list [str], pensieri: list [str]):
        self.__mezzi = mezzi
        self.__pensieri = pensieri
        
#BODY    
    def f_stampa (self):
        concetti: list [str] = []
        for mezzo in self.__mezzi:
            for pensiero in self.__pensieri:
                concetti.append (f"{mezzo} {pensiero}")
        return concetti
                

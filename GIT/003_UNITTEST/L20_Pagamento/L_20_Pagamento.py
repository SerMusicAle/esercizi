"""
#GESTIONE PAGAMENTO
"""

from abc import ABC, abstractmethod

class Pagamento(ABC):
#INIT
    def __init__(self, importo:float):
        self.__importo = round (importo,2)
    
    def f_set(self, importo:float):
        self.__importo = round (importo,2)
        
    def f_get(self) -> float:
        return self.__importo
        
    def f_dettagli_pagamento(self):
        a = (f"L'importo del pagamento è: {self.__importo:.2f}€")
        print (a)
        return (a)
    
class Pagamento_contanti(Pagamento):
#INIT
    def __init__ (self, importo:float):
        super().__init__(importo)
    
#BODY        
    def f_dettagli_pagamento(self):
        print ("Questo pagamento è in contanti: \n")
    
    def f_pezzi_da (self):
        self.importo = self.f_get()
        self.pezzi: list = [ 
            (500, "banconote"),
            (200, "banconote"),
            (100, "banconote"),
            (50, "banconote"),
            (20, "banconote"),
            (10, "banconote"),
            (5, "banconote"),
            (2, "monete"),
            (1, "monete"),
            (0.5, "monete"),
            (0.2, "monete"),
            (0.1, "monete"),
            (0.05, "monete"),
            (0.01, "monete")
        ]
        print (f"Per effettuare il pagamento in contanti di {self.importo:.2f} euro")
        for valore, tipo in self.pezzi:
            self.quantità = int (self.importo // valore)
            print (f"sono necessarie {self.quantità} {tipo} da {valore} euro \n")
            self.importo -= (valore * self.quantità)
        

class Pagamento_carta (Pagamento):
#INIT
    def __init__(self, importo:float, nome_titolare: str, cognome_titolare: str, data_scadenza: str, ncarta: int):
        super().__init__(importo)
        self.__nome_titolare = nome_titolare
        self.__cognome_titolare = cognome_titolare
        self.__data_scadenza = data_scadenza
        self.__ncarta = ncarta

#BODY       
    def f_dettagli_pagamento(self):
        dettagli_importo = super().f_dettagli_pagamento()
        a = (f"{dettagli_importo}. Il pagante è {self.__nome_titolare} {self.__cognome_titolare}. la sua carta n° {self.__ncarta} scade il {self.__data_scadenza}")
        print (a)
        return (a)

#TEST 1 
pagamento_contanti1 = Pagamento_contanti (928365.234)  

pagamento_contanti1.f_dettagli_pagamento()
pagamento_contanti1.f_pezzi_da()

#TEST 2    
pagamento_carta1 = Pagamento_carta(76523.8765, "Alessandro", "Sereni", "23-06-2030", 28363464934976)     

pagamento_carta1.f_dettagli_pagamento()



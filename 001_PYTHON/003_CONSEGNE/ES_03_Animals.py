#DESCRIPTION CLASSE
"""
    classe animali, due istanze animali
    stampa nomi oggetti
    funzione get legs per cambiare numero zampe
    funzione set legs ritorna numero zampe
    funzione print info come str per stampare gli attributi
    
"""

#CLASSE
class Animal:
    
    #FUNZIONE __init__
    def __init__ (self, animal:str, pedia:int):
        
        #DICHIARAZIONE
        self.animal = animal
        self.pedia = pedia

    #FUNZIONE get legs    
    def get_legs (self, animal, pedia):
        return f'il tipo di animale {self.animal}, ha {self.pedia} zampe'
    
    #FUNZIONE set legs
    def set_legs (self, animal, pedia):
        for animal in animals:
            animal.pedia -=1
            return  f'il tipo di animale {self.animal}, adesso ha {self.pedia} zampe'

animals = [
    Animal ("gatto", 4),
    Animal ("gufo", 2)
    ]


#return
Animal.set_legs()
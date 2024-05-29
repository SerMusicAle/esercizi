from abc import ABC, abstractmethod

class AbcAnimal (ABC):

    @abstractmethod
    def verso(self):
        pass

    @abstractmethod
    def movimento(self):
        pass

class Cane(AbcAnimal):

    def __init__(self, nome:str) ->None:
        
        super().__init__()

        self.nome: str = nome
        self.velocità: float = 10.0 #m/s
    
    def verso(self):
        print("Bau!")
    
    def movimento(self, t:int):
        print (self.velocità * t)

class Gatto(AbcAnimal):

    def __init__(self, nome:str) ->None:
        
        super().__init__()

        self.nome = nome
    
    def verso(self):
        return print("Miao!")

cane1: Cane = Cane(nome="Pluto")
cane1.verso ()
cane1.movimento(t=10)

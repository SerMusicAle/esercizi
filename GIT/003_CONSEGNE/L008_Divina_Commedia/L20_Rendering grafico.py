"""
#RENDERING GRAFICO

FORMA - ABS CLASS
    nome
    getArea() - calcola area
    render() - disegna

QUADRATO (FORMA)
    arg - lato
    
RETTANGOLO (FORMA)
    arg - base altezza

"""
from abc import ABC, abstractmethod

class Forma(ABC):

#INIT
    def __init__(self, nome:str):
        self.__nome = nome
        
#BODY
    @abstractmethod
    def f_get_area():
        pass
    
    @abstractmethod
    def f_render() :
        pass   
    
class Quadrato (Forma):
#INIT
    def __init__(self, nome: str, lato:int):
        super().__init__(nome)
        
        self.__lato = lato
        
    def f_get_area(self):
        quadrato_area = self.__lato * self.__lato
        
    def f_render(self):
        print ("*" * self.__lato)
    
        for _ in range (self.__lato - 2):
            print ("*" + " " * (self.__lato - 2) + "*")
            
        print ("*" * self.__lato)
        
class Rettangolo (Forma):
#INIT
    def __init__(self, nome: str, base: int, altezza: int):
        super().__init__(nome)
        
        self.__base = base
        self.__altezza = altezza
        
    def f_get_area(self):
        rettangolo_area = self.__base * self.__altezza
        
    def f_render(self):
        
        print ("*" * self.__base)
        
        for _ in range (self.__altezza - 2):
            print ('*' + ' ' * (self.__base - 2) + '*')
        
        print ("*" * self.__base)
        

#ESECUZIONE
quadrato = Quadrato ("Quadrato: ", 6)
rettangolo = Rettangolo ("Rettangolo: ", 6,3)

quadrato.f_get_area()
quadrato.f_render()

rettangolo.f_get_area()
rettangolo.f_render()
        
        
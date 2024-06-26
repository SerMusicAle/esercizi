"""
Creating an Abstract Class with Abstract Methods
Create an abstract class Shape with an abstract method area and 
another abstract method perimeter. 
Then, create two subclasses Circle and Rectangle that implement 
the area and perimeter methods.


"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def f_area (self):
        pass
    
    @abstractmethod
    def f_perimetro (self):
        pass
    
class Cerchio(Shape):
    
    def __init__ (self, raggio: float):
        self.raggio = raggio
    
    def f_area (self):
        self.area: float = math.pi * self.raggio ** 2
        
    def f_perimetro (self):
        self.perimetro: float = 2 * math.pi * self.raggio

class Rettangolo(Shape):
    
    def __init__ (self, altezza: float, base: float):
        self.altezza = altezza
        self.base = base
    
    def f_area (self):
        self.area: float = self.base * self.altezza
        
    def f_perimetro (self):
        self.perimetro: float = (self.base * 2) + (self.altezza * 2)

class Stampa:
    
    def __init__ (self, base: float, altezza: float, raggio: float):
        self.base: float = 2.00
        self.altezza: float = 3.00
        self.raggio: float = 3.00

    def f_stampa(self):
        cerchio = Cerchio (self.raggio)
        rettangolo = Rettangolo (self.base, self.altezza)
        print (f"Cerchio: l'area del cerchio di raggio {self.raggio} è vale {cerchio.f_area()} ed il paerimetro vale: {cerchio.f_perimetro()} ")
        print (f"Rettangolo: l'area del rettangolo con base {self.base} e altezza {self.altezza} vale {rettangolo.f_area()} e il perimetro vcale {rettangolo.f_perimetro()}")

stampa = Stampa(2.00, 3.00, 3.00)

stampa.f_stampa()
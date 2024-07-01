"""
9-1. Ristorante: Crea una classe chiamata Ristorante.
    Il metodo __init__() per Ristorante dovrebbe memorizzare due attributi: restaurant_name (nome del ristorante) e cuisine_type (tipo di cucina). 
    Crea un metodo chiamato describe_restaurant() che stampi queste due informazioni
    un metodo chiamato open_restaurant() che stampi un messaggio che indica che il ristorante è aperto. 
    Crea un'istanza chiamata ristorante dalla tua classe. 
    Stampa i due attributi individualmente e poi chiama entrambi i metodi.
"""
import unittest

class NomeClasse ():
#INIT
    def __init__ (self):
        pass
#BODY    
    def f_funzione (self):
        pass
    
class TestNomeClasse (unittest.TestCase):
#SETUP
    def setUp ():
        pass

#RUN
if __name__ == '__main__':
    unittest.main()        


#DESCRIPTION

#CLASS ENVELOPE
class Restaurant:

    #DEC
    def __init__(self,restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #BODY
    def describe_restaurant(self):
        print ("il ristorante " + self.restaurant_name + "serve " + self.cuisine_type)

    def open_restaurant(self):
        print ("il ristorante " + self.restaurant_name + "è aperto")


#ASSIGNEMENT
restaurant = Restaurant("Ristorante da Ciro ", "Cucina thailandese")

#RETURN
#print both attributes
print ("il nome del ristorante è " + restaurant.restaurant_name)
print ("il tipo di cucina servito da " + restaurant.restaurant_name + "è " + restaurant.cuisine_type)

#call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
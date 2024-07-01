#DESCRIPTION
"""
9-1. Restaurant: Make a class called Restaurant. 
    The __init__() method for Restaurant should store two attributes: 
    a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
    that prints these two pieces of information, and a method called open_restaurant() 
    that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. 
    Print the two attributes individually, and then call both methods.
    9-1. Ristorante: Crea una classe chiamata Ristorante. 
    Il metodo init() per Ristorante dovrebbe memorizzare due attributi: restaurant_name (nome del ristorante) e cuisine_type (tipo di cucina). 
    Crea un metodo chiamato describe_restaurant() che stampi queste due informazioni e un metodo chiamato open_restaurant() 
    che stampi un messaggio indicando che il ristorante è aperto. Crea un'istanza chiamata restaurant dalla tua classe. 
    Stampa i due attributi individualmente e poi chiama entrambi i metodi.
"""
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
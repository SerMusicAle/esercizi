"""
9-2. Three Restaurants: 
Start with your class from Exercise 9-1. 
Create three different instances from the class, 
and call describe_restaurant() for each instance.


9-2. Tre Ristoranti: 
Partendo dalla tua classe dell'Esercizio 9-1, 
crea tre diverse istanze della classe e 
chiama describe_restaurant() per ciascuna istanza.

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


#ASSIGNEMENT INSTANCE
restaurant = Restaurant("Ristorante da Ciro ", "Cucina thailandese")
restaurant2 = Restaurant("Ristorante da Mirko ", "Cucina africana")
restaurant3 = Restaurant("Ristorante da Manuel ", "Cucina coreana")


#RETURN
#print both attributes
print ("il nome del ristorante è " + restaurant.restaurant_name)
print ("il tipo di cucina servito da " + restaurant.restaurant_name + "è " + restaurant.cuisine_type)

#call both methods
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
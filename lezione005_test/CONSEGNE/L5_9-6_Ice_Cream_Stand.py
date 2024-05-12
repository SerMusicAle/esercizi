"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1  or Exercise 9-4. 
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 


9-6. Gelateria: Una gelateria è un tipo specifico di ristorante. 
Scrivi una classe chiamata IceCreamStand che eredita dalla classe Restaurant 
che hai scritto nell'Esercizio 9-1 o nell'Esercizio 9-4. 
Entrambe le versioni della classe funzioneranno; scegli quella che preferisci. 
Aggiungi un attributo chiamato flavors che memorizza una lista di gusti di gelato. 
Scrivi un metodo che visualizzi questi gusti. Crea un'istanza di IceCreamStand e chiama questo metodo.

"""
#CLASS RESTAURANT ENVELOPE
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


#CLASS CREAM ENVELOPE        
class IceCreamStand(Restaurant):

    #DEC
    def __init__ (self, restaurant_name:str, cuisine_type:str, flavors= []):
        super().__init__ (restaurant_name, cuisine_type)
        self.flavors = flavors
    
    #print flavors
    def display_flavors(self):
        print (f"I gusti di gelato pronti sono: ")
        for flavor in self.flavors:
            print(flavor)


#ASSIGNEMENT
gelateria = IceCreamStand ("mondo gelo", "gelati vegani", ["cioccolato", "crema", "pistacchio"])

#RETURN
gelateria.display_flavors()

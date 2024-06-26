"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 
Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to show 
that the import statement is working properly.


9-10. Ristorante Importato: 
Utilizzando l'ultima versione della classe Ristorante, memorizzala in un modulo. 
Crea un file separato che importi il modulo del Ristorante. 
Crea un'istanza di Ristorante e chiama uno dei metodi del Ristorante 
per mostrare che l'istruzione di importazione funziona correttamente.

NON SVOLGERE PER ORA

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

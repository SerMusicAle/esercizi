"""
9-1. Ristorante: Crea una classe chiamata Ristorante.
    Il metodo __init__() per Ristorante dovrebbe memorizzare due attributi: restaurant_name (nome del ristorante) e cuisine_type (tipo di cucina). 
    Crea un metodo chiamato describe_restaurant() che stampi queste due informazioni
    un metodo chiamato open_restaurant() che stampi un messaggio che indica che il ristorante è aperto. 
    Crea un'istanza chiamata ristorante dalla tua classe. 
    Stampa i due attributi individualmente e poi chiama entrambi i metodi.
"""

class Restaurant ():
#INIT
    def __init__ (self, restaurant_name:str, cuisine_type:str, status:bool):
        self.__restaurant_name = restaurant_name
        self.__cuisine_type = cuisine_type
        self.__status = status
#BODY    
    def f_describe_restaurant(self):
        descrizione: str = self.__restaurant_name
        tipo: str = self.__cuisine_type
        return descrizione, tipo
        
    def open_restaurant(self):
        if self.__status:
            return f"il ristorante è aperto"
        else:
            return f"il ristorante è chiuso"
                 

#CLASS CREAM ENVELOPE        
class IceCreamStand(Restaurant):

    #DEC
    def __init__ (self, restaurant_name:str, cuisine_type:str, status:bool, flavors: list [str]= []):
        super().__init__ (restaurant_name, cuisine_type, status)
        self.__flavors = flavors
    
    #print flavors
    def display_flavors(self):
        print (f"I gusti di gelato pronti sono: ")
        for flavor in self.flavors:
            print(flavor)
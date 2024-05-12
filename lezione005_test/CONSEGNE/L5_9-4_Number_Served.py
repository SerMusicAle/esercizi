"""
9-4. Number Served: Start with your program from Exercise 9-1. 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, 
and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again. 
Add a method called increment_number_served() 
that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how 
many customers were served in, say, a day of business. 



9-4. Numero di Clienti Serviti: Partendo dal programma dell'Esercizio 9-1, 
aggiungi un attributo chiamato number_served con un valore predefinito di 0. 
Crea un'istanza chiamata restaurant da questa classe. 
Stampa il numero di clienti che il ristorante ha servito, 
quindi cambia questo valore e stampalo nuovamente. 
Aggiungi un metodo chiamato set_number_served() che ti permetta di impostare 
il numero di clienti serviti. Chiama questo metodo con un nuovo numero e stampa di nuovo il valore. 
Aggiungi un metodo chiamato increment_number_served() che ti permetta di incrementare 
il numero di clienti serviti. 
Chiama questo metodo con un numero a tua scelta che potrebbe rappresentare 
quanti clienti sono stati serviti in un giorno di attività.
"""


#CLASS ENVELOPE
class Restaurant:

    #DEC
    def __init__(self,restaurant_name:str, cuisine_type:str, number_served:int=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    #BODY

    #number of clients
    def set_number_served(self):
        print(f"il numero di clienti serviti ora è: {self.number_served}")
        new_number = int(input("quale è il nuovo numero di clienti serviti?: "))
        self.number_served = new_number
        print(f"il nuovo numero di clienti serviti è aggiornato a {self.number_served}")
        
    
    def increment_number_served(self):
        increment = int(input("se hai bisogno di incrementare il numero dei clienti serviti dimmi di quanto incrementare: "))
        self.number_served += increment
        print(f"nuovo numero di clienti serviti è aggiornato a {self.number_served}")
    

#ASSIGNEMENT
restaurant = Restaurant("Ristorante da Ciro ", "Cucina thailandese", 123)


#CALL both methods
restaurant.set_number_served()
restaurant.increment_number_served()
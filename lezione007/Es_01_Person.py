#DESCRIPTION CLASSE
"""
    stampa età di bob con dot notation
    stampa il nome del più vecchio con una if
    crea altre 3 persone e inserisci tutti in una lista    
    crea un ciclo che trovi e stampi il nome della più giovane
    
"""

#CLASSE
class Person:
    
    #FUNZIONE __init__
    def __init__ (self, name, age):
        
        #DICHIARAZIONE
        self.name = name
        self.age = age

    #FUNZIONE __str__    
    def __str__ (self) ->str:
        return f'Person(name={self.name}), age={self.age}'

alice = Person ("Alice W.", 45)
bob = Person ("Bob M.", 36)

persons = [
    Person("Alice W.", 45),
    Person("Bob M.", 36),
    Person("Ale S.", 42),
    Person("Paolo S.", 47),
    Person("Daniele C.", 40)]


year: int = 0
younger: int = 0

#BODY - stampa nome bob
print (bob.name)

#oldest
if bob.age > alice.age:
    print (bob.age)
else:
    print (alice.age)

#youngest
for person in persons:
    if person.name > year: 
        younger = person.name
        year = person.age

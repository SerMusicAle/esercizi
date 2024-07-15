#DESCRIPTION FUNCTION
"""
    6-7. People: Start with the program you wrote for Exercise 6-1. 
    Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
    Loop through your list of people. As you loop through the list, print everything you know about each person.
"""


#FUNCTION
def f_identity ():
    
    #DECLARATION LOCAL VAR
    peolpe: list = []
    quantity= int(input(f"di quante persone vuoi inserire i dati? "))

    #BODY - input request
    for _ in range (quantity):
        #person's idendity
        identity: dict = {}

        #info
        identity['first_name'] = input("quale è il nome di battesimo? ")
        identity['last_name'] = input("quale è il cognome? ")
        identity['yy'] = input("quale è l'anno di nascita? ")
        identity['mm'] = input("quale è il mese in cui è nato/a in numeri? ")
        identity['dd'] = input("quale è il giorno in cui è nato/a ")
        identity['city'] = input("quale è la città dove è nato/a? ")
    
        peolpe.append(identity)
    
    #RETURN
    for index, person in enumerate(people):
        print(f"\n ùInformazioni su Persona {index}:")
        print(f"Nome: {person['first_name']} {person['last_name']}")
        print(f"Data di nascita: {person['dd']}-{person['mm']}-{person['yy']}")
        print(f"Città di nascita: {person['city']}")


#CALL FUNCTION
f_identity()
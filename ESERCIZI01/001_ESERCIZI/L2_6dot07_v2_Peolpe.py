#DESCRIPTION FUNCTION
"""
    6-7. People: Start with the program you wrote for Exercise 6-1. 
    Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
    Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

#FUNCTION
def f_identity():
    
    #DECLARATION LOCAL VAR
    people = []
    
    # ask how many people
    quantity = int(input("Di quante persone vuoi inserire i dati? "))

    #BODY - input request
    for _ in range(quantity):
        first_name = input("Qual è il nome di battesimo? ")
        last_name = input("Qual è il cognome? ")
        yy = input("Qual è l'anno di nascita? ")
        mm = input("Qual è il mese di nascita (in numeri)? ")
        dd = input("Qual è il giorno di nascita? ")
        city = input("Qual è la città di nascita? ")

        person = {
            'first_name': first_name,
            'last_name': last_name,
            'yy': yy,
            'mm': mm,
            'dd': dd,
            'city': city
        }

        people.append(person)
    
    #RETURN
    for index, person in enumerate(people):
        print(f"\nInformazioni su Persona {index + 1}:")
        print(f"Nome: {person['first_name']} {person['last_name']}")
        print(f"Data di nascita: {person['dd']}-{person['mm']}-{person['yy']}")
        print(f"Città di nascita: {person['city']}")

#CALL FUNCTION
f_identity()

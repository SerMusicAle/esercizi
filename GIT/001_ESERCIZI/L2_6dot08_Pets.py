#DESCRIPTION FUNCTION
"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet. 
"""
#FUNCTION
def f_pet():
    #DECLARATION LOCAL VAR
    quantity = int(input(f"di quanti animali mi fornisci i dati?"))
    pets = []
    
    #BODY input requests
    for _ in range (quantity):
        nome = input(f"quale è il nome di questo animale domestico? ")
        genere = input(f"a quale genere appartiene questo animale domestico? ") 
        razza = input(f"di quale razza è questo animale domestico? ")
        proprietario = input(f"quale è il nome del proprietario? ")

        pet = {
            'nome' : nome,
            'genere' : genere,
            'razza' : razza,
            'proprietario' : proprietario

        }
    
        pets.append(pet)
    
    #RETURN
    for index, pet in enumerate (pets):
        print (f"{pet['nome']}, il cui proprietario è {pet['proprietario']} è un {pet['genere']} di razza {pet['razza']}")


#CALL FUNCTION
f_pet()
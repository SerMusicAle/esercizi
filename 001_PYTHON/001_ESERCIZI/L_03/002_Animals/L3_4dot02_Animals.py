#DESCRIPTION FUNCTION
"""
    4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
    • Modify your program to print a statement about each animal, such as A dog would make a great pet.
    • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
"""
#FUNCTION
def f_animals ():

    #DECLARATION LOCAL VAR
    animals: list = []
    thoughts: dict = {}
    
    #request
    quantity = int(input(f"inseerisci quanti animali vuoi prendere in argomento. almeno 3 "))

    #BODY
    for _ in range(quantity):
        animal = input(f"dimmi un animale: ")
        animals.append(animal)
    
    #print animals
    print(f"riassumo gli animali: ")
    for i in animals:
        print (i)

    #insert comment
    for i in animals:
        thought  = input(f"inserisci una frase che descriva l'animale {i}: ")
        thoughts [i] = thought

    #print animals and comment
    print (f"descrizioni degli animali: ")
    for animal, thought  in thoughts.items():
        print (f"{animal}: {thought}")

    print (f"al di la delle osservazioni inserite hanno tutti 4 zampe")
#INPUT requests
#CALL FUNCTION
f_animals()
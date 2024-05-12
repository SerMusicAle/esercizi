#DESCRIPTION FUNCTION
"""
    6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
"""

#FUNCTION
def f_best_number ():
    
    #DECLARATION LOCAL VAR
    number_s_friend: dict = {}

    #BODY . input request

    #how many friends
    quantity = int(input ("quanti amici vuoi prendere in considedrazione?" ))

    for _ in range (quantity):

        #ask names and numbers
        name = input(f"dimmi il nome del tuo amico ")
        number = int(input(f"quale è il suo numero preferito? "))

        #assignment
        number_s_friend[name] = [number]
    #RETURN
    for name, numer in number_s_friend.items():
        print(f" il numero preferito di {name} è {number}")

#CALL FUNCTION
f_best_number()













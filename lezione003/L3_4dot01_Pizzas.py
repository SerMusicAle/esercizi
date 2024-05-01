#DESCRIPTION FUNCTION
"""
    4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
    • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
    • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
"""

#FUNCTION
def f_pizzas ():
    
    #DECLARATION LOCAL VAR
    pizzafixed: list = ["mele", "pere", "nutella"]
    pizzas: list = []
    quantity = int(input(f"quanti tipi di pizza ti piacciono? "))
    
    #BODY
    #memorizza pizze
    for i in range (quantity):
        pizza = input(f"dimmi una delle pizze che ti piace: ")
        pizzas.append(pizza)
        
    #stampa pizze
    print (f"hai inserito le pizze: \n")
    for i in pizzas:
        print (i)
    
    #stampa frase
    for i in pizzas:
        print (f" buona la pizza {i}")
    #RETURN

    print (f"mi piace la pizza {pizzafixed[0]}\n mi piace la pizza {pizzafixed[1]}\n mi piace la pizza {pizzafixed[2]}\n")
#INPUT requests
#CALL FUNCTION
f_pizzas()
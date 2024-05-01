#DESCRIPTION FUNCTION
"""
    4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
    • Add a new pizza to the original list.
    • Add a different pizza to the list friend_pizzas.
    • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""

#FUNCTION
def f_pizzas():
    
    # Original pizza's list
    pizzas: list = ["Margherita", "Prosciutto e Funghi", "Quattro Stagioni"]
    
    # pizza's list copy
    friend_pizzas = pizzas[:]  # Utilizziamo slicing per creare una copia della lista
    
    # add a pizza to a original list
    pizzas.append("Diavola")
    
    # add a pizza to a new list
    friend_pizzas.append("Quattro Formaggi")
    
    # print my favourite's pizza
    print("Le mie pizze preferite sono:")
    for pizza in pizzas:
        print(f"- I like {pizza} pizza.")
    
    # print my friend favourite's pizza
    print("\nLe pizze preferite dell'amico sono:")
    for pizza in friend_pizzas:
        print(f"- My friend likes {pizza} pizza.")

    # print thought
    print("\nMi piace davvero tanto la pizza!")

#CALL FUNCTION
f_pizzas()


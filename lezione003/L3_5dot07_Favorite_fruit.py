#DESCRIPTION FUNCTION
"""
    5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
    • Make a list of your three favorite fruits and call it favorite_fruits.
    • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!
"""

#FUNCTION
def f_frutta_preferita():

    #BODY
    #DECLARATION LOCAL VAR - fruits list
    frutta_preferita = ['mela', 'banana', 'fragola']


    #INPUT requests
    fruit = input(f"quale frutto ti piace? ")

    if fruit in frutta_preferita:
        print("è vero. {fruit} è uno dei tuoi frutti preferiti!")

#CALL FUNCTION
f_frutta_preferita()

   

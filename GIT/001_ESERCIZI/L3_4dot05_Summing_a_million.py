#DESCRIPTION FUNCTION
"""
    4-5. Summing a Million: Make a list of the numbers from one to one million, 
    and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
"""

#FUNCTION
def f_one_million ():

    #DECLARATION LOCAL VAR
    quantity = int(input(f"quanti numeri devo scrivere? "))
    
    #BODY
    million = list(range(1, quantity+1))

    print(f"il minimo è: {min(million)}")
    print(f"il massimo è: {max(million)}")
    
    million_sum = sum(million)
    print(f"La somma dei {len(million)} numeri della lita è {million_sum}")

#CALL FUNCTION
f_one_million()
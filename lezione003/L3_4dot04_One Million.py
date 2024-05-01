#DESCRIPTION FUNCTION
"""
    4-4. One Million: Make a list of the numbers from one to one million, 
    and then use a for loop to print the numbers. 
    (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
"""


#FUNCTION
def one_million ():

    #DECLARATION LOCAL VAR
    quantity = int(input(f"quanti numeri devo scrivere? "))
    million: list = []

    #BODY
    for i in range (1,quantity+1):
        million.append(i)

    for i in million:
        print (i)
    #RETURN

#INPUT requests
#CALL FUNCTION
one_million()
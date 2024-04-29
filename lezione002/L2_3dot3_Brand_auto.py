#DESCRIPTION FUNCTION
"""
    3-3. Your Own List: Think of your favorite mode of transportation, 
    such as a motorcycle or a car, 
    and make a list that stores several examples. 
    Use your list to print a series of statements about these items, 
    such as “I would like to own a Honda motorcycle.
”"""

#FUNCTION
def f_brand_auto():

    #DECLARATION LOCAL VAR
    catalogue = {}

    #BODY
    print (f"quante case produttrici di auto o moto consoci? ")
    quantity = int(input())
    
    for _ in range(quantity):

        brand: str = input (f"nominami una delle case produttrici di auto o moto che conosci")
        
        opinion: str = input (f"cosa ne pensi della {brand}? ")

        catalogue[brand] = opinion
    #RETURN
    return catalogue
    #INPUT requests



#CALL FUNCTION
res = f_brand_auto()

#EXECUTION - print phrases and models
for brand,opinion in res.items():
    print (f"Brand: {brand}, la mia opinione è : {opinion}")





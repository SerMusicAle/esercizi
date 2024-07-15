#DESCRIPTION FUNCTION
"""
3-3. La tua lista personale: 
    Pensa al tuo mezzo di trasporto preferito, come una motocicletta o un'auto, 
    crea una lista che contenga diversi esempi. 
    Usa la tua lista per stampare una serie di affermazioni su questi elementi, 
    come "Mi piacerebbe possedere una motocicletta Honda".
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





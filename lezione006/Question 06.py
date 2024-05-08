"""
ASSEGNAZIONE
Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
For example:

Test	Result
print(list_statistics([1, 2, 3, 4, 5]))
(5, 1, 3.0)

"""







"""
CONSEGNA
def list_statistics(numbers: list[int]) -> ... :
    
    #ASSEGNAZIONE
    middle = 0
    somma = 0
    
    #BODY
    massimo = max(numbers)
    minimo = min(numbers)
    
    for i in numbers:
        somma +=i
    middle = somma/len(numbers)
    
    return (massimo, minimo, middle)
    
    
    
"""
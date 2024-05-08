"""
ASSEGNAZIONE 3
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
For example:

"""
def find_element(lst: list[int], element: int) -> bool:
    
    #BODY
    for item in lst:
        if item == element:
            return True
    return False





lst = [1,2,3,4,5,6]
element = 7
risultato = find_element(lst,element)
print (risultato)
"""
CONSEGNA
def find_element(lst: list[int], element: int) -> bool:
    
    #BODY
    for item in lst:
        if item == element:
            return True
    return False
"""
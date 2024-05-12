#DESCRIPTION FUNCTION
"""
    ASSEGNAZIONE 2
    Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
"""

#FUNCTION
def sum_above_threshold(numbers: list[int], threshold) -> int:

    somma = 0

    #BODY
    for i in numbers:
        if isinstance (i,int) and i > threshold:
            somma +=i
    return somma

numbers = [1, 2, 3,4,5]
risultato = sum_above_threshold(list)
print(risultato)


# Esempio di utilizzo della funzione
numbers = [1, 2, 3, 4, 5, "ciao", 6.7, 8]  # Lista con diversi tipi di dati
threshold = 2  # Valore di soglia

# Chiamata alla funzione con la lista e il valore di soglia specificati
risultato = sum_above_threshold(numbers, threshold)
print(risultato)  # Output: 20

"""
CONSEGNA
def sum_above_threshold(numbers: list[int], threshold) -> int:
    somma = 0

    #BODY
    for i in numbers:
        if isinstance (i,int) and i > threshold:
            somma +=i
    return somma
"""
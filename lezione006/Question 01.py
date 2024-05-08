#DESCRIPTION FUNCTION
"""
    ASSEGNAZIONE 1
    La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
    Un errore nell'implementazione porta a risultati inaspettati.
    Trova l'errore e correggi il codice affinché soddisfi i casi di test.
"""

#FUNCTION
def calculate_average(numbers: list[int]) -> float:
    
    #BODY
    if not numbers:
        return 0  
    media = sum(numbers) / len(numbers)
    
    #RETURN
    return media


lista_numeri = [1, 2, 3,4,5]
risultato_media = calculate_average(lista_numeri)
print("Media:", risultato_media)


"""
CONSEGNA
def calculate_average(numbers: list[int]) -> float:
    
    #BODY
    if not numbers:
        return 0  
    media = sum(numbers) / len(numbers)
    
    #RETURN
    return media
"""
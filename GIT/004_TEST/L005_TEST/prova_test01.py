#DESCRIPTION FUNCTION
"""
    hai una lista di interi. 
    crea un set di valori della lista
    trova l'elemento al posto 3 di valore
    la funzione ha come parametro la lista
    verifica se ci sono almeno 3 valori distinti
    se non ci sono 3 valori distinti 
    restituisci il più alto
"""
#FUNCTION
def third_max(nuns):

    #DECLARATION LOCAL VAR
    nuns: list = [3,2,1]
    
    #stampa elemento 3
    nuns[2]
    count=1
    #verifica 3 valori
    for i in nuns:
        if i!= i+1:
            count+=1
        if count==3:
            break
    return ()


ddef third_max(nuns):
    # Converte la lista in un insieme per ottenere valori distinti
    nuns_set = set(nuns)
    
    # Verifica se ci sono almeno 3 valori distinti
    if len(nuns_set) >= 3:
        # Ordina l'insieme in ordine decrescente
        sorted_nuns = sorted(nuns_set, reverse=True)
        # Restituisce il terzo massimo valore
        return sorted_nuns[2]
    else:
        # Se ci sono meno di 3 valori distinti, restituisce il massimo valore
        return max(nuns_set)

# Esempio di utilizzo della funzione
lista = [3, 2, 1, 3, 5, 6, 2, 1]
result = third_max(lista)
print("Il terzo massimo valore nella lista è:", result)

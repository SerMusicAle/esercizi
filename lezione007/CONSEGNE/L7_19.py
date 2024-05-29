"""
CONSEGNA
19. Scrivi una funzione che 
- ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
- La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
- l'elemento iniziale viene spostato alla fine della lista. 
- Per la rotazione utilizzare lo slicing
- gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.
"""
def posizioni (quantity):


#INIT
    numeri:list = [1,2,3,4,5,6,7,8,9]
    vardep:int = 0

#BODY
    for i in range (quantity):
        vardep = numeri[0]
        for j in range(len(numeri)-1):
            numeri[j] = numeri[j+1]
        numeri[-1] = vardep
    
#RETURN
#    return numeri
    print(f"la nuova lista è: {', '.join(str(i) for i in numeri)}")
    

#INPUT
quantity = int(input("quante volte devo far ruotare la lista?"))


#CALL
posizioni(quantity)

#print(posizioni(quantity))

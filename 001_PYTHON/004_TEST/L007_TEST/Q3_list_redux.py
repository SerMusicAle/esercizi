"""
Q3 
    Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. 
    Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.
    For example:

    Test	Result
    print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
    [1, 3, 4]
    print(rimuovi_elementi([], {2: 1})) 
[]
"""

def f_list_redux(listadati:list[int], elementi:dict[int,int]):
    cont: int = 0
    i:int = 0    
    for chiave, valore in elementi.items():  
        for i in listadati:
            if i == chiave:
                listadati.remove(i)
                cont +=1
                if cont == valore:
                    return listadati
            
    
listadati:list[int] = [1, 2, 3, 2, 4]
elementi:dict[int,int] = {2: 2}
print(f_list_redux(listadati,elementi))

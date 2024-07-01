"""
    Si immagini una funzione che 
    - comprima i file all'80%
    - li salvi su un supporto di memorizzazione di 1000 blocchi. 
    - memorizzi il file, dividendolo in blocchi da 512 byte ciascuno.

    un algoritmo
    - prende in input una lista di valori interi che esprimono in byte la dimensione non compressa di un singolo file
    - che iteri la lista e, per ogni dimensione 
        - calcoli la dimensione compressa del file come l' 80% della dimensione originale
        - calcoli il numero di blocchi  da 512 byte arrotondato al numero intero più vicino
        - verifichi se lo spazio di memorizzazione rimanente è sufficiente a contenere i blocchi del file
    
    return true, 
    - memorizzare il file. 
    - stampare 
        - la dimensione originale del file, 
        - la dimensione compressa, 
        - i blocchi utilizzati per memorizzare il file 
        - i blocchi disponibili rimasti nel supporto. 
        - print: "File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
    
    return false
    - quando lo spazio non è sufficiente per salvare il file. 
    - stampa: "Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."
     
"""

###PERSO PARTE DEL CODICE. FINIRE DI NUOVO

import math

def memorizza_file(files: list[int]) -> None:

#INIT
    tot_block = 1000
    
#BODY
    for i in files:
        dep_i = i
        i *= 0.80
        blockn = round(i / 512)
        
#RETURN
        if tot_block >= blockn:
            tot_block -= blockn
            return (f"File di {dep_i} byte compresso in {i} byte e memorizzato. Blocchi usati: {blockn}. Blocchi rimanenti: {tot_block}.")
        
        else:
            return(f"Non è possibile memorizzare il file di {dep_i} byte. Spazio insufficiente.")
        break

#CALL
memorizza_file([1100, 20000, 1048576, 512, 5000])


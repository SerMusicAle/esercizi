"""
Sviluppare una funzione in Python per 
- calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
- L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro 
- l'azienda paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, 
- viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
- La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.

"""

def f_calcola_stipendio(ore_lavorate: int) -> float:

#INIT
    stipendio = 0
    
#BODY
    if ore_lavorate < 40:
            stipendio = 10* ore_lavorate
    else:
        stipendio = 400 + (ore_lavorate-40)*15

#RETURN
    #return stipendio
    print (stipendio)

#INPUT
ore_lavorate = 40

#CALL
f_calcola_stipendio(ore_lavorate)
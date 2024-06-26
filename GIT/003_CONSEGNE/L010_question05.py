"""
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!


"""

def f_integerPower (base:int, esponente:int):

#BODY
    if isinstance(base, int) and \
    isinstance(esponente, int) and \
    esponente>0 and esponente!=0:
        potenza:int = base**esponente   

#RETURN
    return potenza

base:int = 2
esponente:int = 3


#CALL
risultato = f_integerPower(base, esponente)
print (risultato)
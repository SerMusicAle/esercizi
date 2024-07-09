"""
Esercizio 2: Decorator
    Crea un decorator chiamato tempo_di_esecuzione che misuri e stampi il tempo di esecuzione di una funzione.
"""
import time

def f_test ():
    for _ in range(10000):
        print ("ciao")

#DECORATOR       
def f_calcola_tempo (func):
    
    #posizionali args e chiave #kwargs
    def wrapper (*args, **kwargs):
        #inizio
        start_time = time.time()    
        #passo la funzione
        dati_funzione = func (*args, **kwargs)
        #fine
        end_time = time.time()
        
        #calcolo
        tempo_esecuzione = end_time - start_time
        
        return tempo_esecuzione
        

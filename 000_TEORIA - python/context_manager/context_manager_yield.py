from contextlib import contextmanager

@contextmanager
def context_manager_decorator():
    import time
    start_time: float = time.time()
    
    yield 
    
    end_time: float = time.time()
    
    elapsed_time: float
        
def generatore():
    yield "A"
    yield "B"
    yield "C"
    
istanza = generatore()

#stampa A
print (next (istanza))
#riprendendo da dove ha lasciato stampa B
print (next (istanza))
#riprendendo da dove ha lasciato stampa C
print (next (istanza))

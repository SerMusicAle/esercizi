"""

Crea un context manager che permette di calcolare il tempo che
viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1


- enter, salva il tempo iniziale
- exit, implementa il tempo finale e fare la sottrazione

"""

class FileManager ():
    
    def __init__ (self, db_name, mode):
        self.file_name: str = file_name
        self.mode: str = mode
        
    
    def __enter__(self):
        self.file_wrapper = open (self.file_name, self.mode)
        return self.file_wrapper
        
                
    def __exit__(self, exc_type, exc_value, traceback):
        self.file_wrapper.close()

    start = time.time()
    
with FileManager (file_name = "prova.txt", mode= "w") as file:
    file.write ("ciao")
    
with open ("prova.txt", "a") as file:
    file.write ("ciao")
           
           
class Timer:
    def __enter__ (self):
        import time
        
        self.time = time.time()
        
    def __exit__(self, src_type, exc_value, traceback):
        import time
        
        print(f"time Elapsed: (time.time())")
        
        
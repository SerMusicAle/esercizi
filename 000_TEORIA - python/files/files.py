#CONTEXT MANAGER

"""
#apertura file nella stessa cartella
open ('esempio.txt')

#apertura file in una sottocartella

open ('sottocartella/esempio2.txt')

#stampa contenuto
print (open ('esempio.txt', encoding = utf-8))

#chiusura file
close  ('esempio.txt')

#apertura e chiusura
reader = open ('file.txt')


reader = open ('esempio.txt', encoding = 'utf-8')

try:
    reader.readLine()
    print (f"sono nella try")
    #codice da eseguire
    raise Exception ("Eccezione")
except Exception:
    print (f"sono nella except")
    #esecuzione alternativa    
finally:
    #esecuzione in conclusione
    print (f"sono nella finnaly")
    #chiusura del file
    reader.close()

 
#With, 
    # chiama implicitamente close
    # as     
nome = open ('esempio.txt', encoding = 'utf-8')

with open('esempio.txt') as nome:
    print (nome)

try:
    nome.readLine()
    print (f"sono nella try")
    #codice da eseguire
    raise Exception ("Eccezione")
except Exception:
    print (f"sono nella except")
    #esecuzione alternativa    
finally:
    #esecuzione in conclusione
    print (f"sono nella finnaly")
    #chiusura del file
    nome.close()

"""

#ENTER
class ContextManater():
    def __enter__ (self):
        print("ciao sono nell'enter")
        return self
    
    def __exit__ (self,exc_type, exc_value, traceback):
        if exc_type is not None:
            print ("eccezione")
        
        nome_file.close()
        
        return False 

#cm è il self di return di enter
with ContextManager() as cm:
    print ('Ciao')
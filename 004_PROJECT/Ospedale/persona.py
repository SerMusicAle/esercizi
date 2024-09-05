class Persona():
#INIT  
    def __init__(self, first_name:str, last_name:str):
        
        #name
        if isinstance(first_name, str): 
            if first_name != "":
                self.__first_name = first_name
            else:
                self.__first_name = None
                print(f"il nome non contiene nulla")
        else:
            self.__first_name = None
            print(f"il nome può contenere solo caratteri alfabetici")
        
        #last name
        if isinstance(last_name, str):
            if last_name != "":
                self.__last_name = last_name
            else:            
                self.__last_name = None
                print ("Il cognome non contiene nulla!")
        else:
            self.__last_name = None
            print (f"Il cognome inserito può contenere solo caratteri alfabetici!")
        
        #age
        if isinstance(last_name, str) and last_name != "" and isinstance(first_name, str) and first_name != "":
            age = 0
            self.__age = age
        else:
            self.__age = None
            
#BODY
    def setName(self, first_name):
        if isinstance (first_name, str) and self.first_name != "":
            self.__first_name = first_name
        else:
            self.__first_name = None
            print (f"il nome deve essere una stringa")

            
    def setLastname(self, last_name):
        if isinstance (last_name, str) and self.__last_name != "":
            self.__last_name = last_name
        else:
            self.__last_name = None
            print (f"il cognome deve essere una stringa")
    
            
    def setAge(self, age):
        if isinstance(self.__first_name, str) and self.__first_name != "" and isinstance(self.__last_name, str) and self.__last_name!= "":
            self.__age = age
        else:
            self.__age = None

        
    def getAge (self):
        return self.__age
    
    def getName (self):
        return self.__first_name
    
    def getLastname(self):
        return self.__last_name
    
    def greet(self):
        if self.__first_name and self.__last_name and self.__age is not None:
            greets:str =f"Ciao, sono {self.__first_name} {self.__last_name} Ho {self.__age} anni"
            print (greets)
            return greets
        else:
            greets:str = (f"informazioni incomplete")
            print (greets)
            return greets 
    """
    def greet(self):
        print (f"Ciao, sono {self.__first_name} {self.__last_name} Ho {self.__age} anni")
        
    """
"""
### CLASSE: Persona
attributi
- due di tipo String, uno per il nome ed uno per il cognome, 
- uno privato di tipo int per l'età.

metodi:
- init(first_name, last_name). 
    OK verificare che first_name, last_name siano stringhe; 
    OK in caso negativo, impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore, 
    Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; 
    se first_name e last_name non sono due stringhe, allora assegnare None all'età.
- setName(first_name): 
    impostare il nome di una persona, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passata al metodo una stringa. 
    In caso contrario, stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".
- setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
    Il valore viene modificato se e solo se viene passata al metodo una stringa. 
    In caso contrario, stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

- setAge(age): 
    consente di impostare l'età di una persona, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passato al metodo un numero intero. 
    In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

- getName(): consente di ritornare il nome di una persona.

- getLastname(): consente di ritornare il cognome di una persona.

- getAge(): consente di ritornare l'età di una persona.

- greet(): stampa il seguente saluto "Ciao, sono nome cognome! Ho età anni!"    
"""
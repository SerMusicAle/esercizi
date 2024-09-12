from persona import Persona

class Dottore (Persona):
#INIT  
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel:float):
        super().__init__(first_name, last_name)
        
        if isinstance (specialization, str) and specialization != "":
            self.__specialization = specialization
        else:
            specialization= None
            print (f"La specializzazione inserita non è un testo valido!")
        
        if isinstance (parcel, float) and parcel > 0.00:
            self.__parcel = parcel
        else:
            self.__parcel = None
            print (f"La parcella inserita non è un float!")

#BODY
    def setSpecialization (self, specialization):
        if isinstance(specialization, str) and specialization != "":
            self.__specialization = specialization
        else:
            print (f"La specializzazione inserita non è una stringa!")
    
        
    def setParcel (self, parcel):
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print (f"La parcella inserita non è un float!")
    
    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.getAge() is not None and self.getAge() >= 30:
            print (f"Doctor {self.getName} {self.getLastname} is valid!")
        else:
            print (f"Doctor {self.getLastname} {self.getName} is not valid!")
            
    def doctorGreet(self):
        dati_persona = self.greet()
        frase2 = f"Sono un medico {self.__specialization}"
        frase = dati_persona + frase2
        print(frase)
        return frase

"""
### CLASSE: Dottore
    Si derivi Dottore dalla classe Persona.

    Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona,
    una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale), 
    ed una parcella per le visite in studio (si usi il tipo float). 
    Gli attributi della classe dottore devono essere anch'essi privati.

    Definire i seguenti metodi:
    - init: 
        (specialization)
        (parcel)
        controllare che specialization sia una stringa e che parcel sia un float, 
        altrimenti assegna None all'attributo che non verifica la condizione richiesta, 
        mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".
        
    - setSpecialization(specialization): 
        imposta la specializzazione di un dottore, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passata al metodo una stringa. 
        In caso contrario, stampare un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".
    - setParcel(parcel): 
        impostare la parcella di un dottore, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passato al metodo un float. 
        In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".
    - getSpecialization(): 
        consente di ritornare la specializzazione del dottore.
    - getParcel(): 
        consente di ritornare la parcella del dottore.  
    - isAValidDoctor(): 
        stabilisce se un dottore è un dottore valido; 
        un dottore è valido se e solo se ha più di 30 anni, 
        Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. 
        In caso contrario, stampare "Doctor nome e cognome is not valid!".
    - doctorGreet():
        tale metodo richiama la funzione greet() della classe Persona. 
        Poi, stampa il seguente saluto "Sono un medico {specializzazione}"
"""
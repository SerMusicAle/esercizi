### CLASSE: Fattura
"""
  metodi:
    OK - init(patient,doctor): 
        lista di pazienti ed un dottore. 
        verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor(). 
          assegnare all'attributo fatture (di tipo intero) il numero di pazienti , 
          assegnare 0 all'attributo salary (di tipo int).  
        In caso contrario,
          assegnare il valore None a tutti i 4 gli attributi della classe 
          stampare un messaggio di errore: "Non è possibile creare la classe fattura poichè il dottore non è valido!".
    OK - getSalary(): 
        ritorna il salario calcolato moltiplicando la parcella del dottore per il numero di pazienti.
    OK - getFatture(): 
        assegna all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) 
        ritornare il suo valore.
    OK - addPatient(newPatient): 
        aggiunge un paziente alla lista di pazienti di un dottore, 
        aggiorna il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().  
        Stampa "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
    OK - removePatient(idCode): 
        dalla lista di pazienti rimuove un paziente ricevendo in input il suo ID
        aggiorna il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). 
        Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".
"""

from dottore import Dottore
from paziente import Paziente

class Fattura():
#INIT  
    def __init__(self, pazienti:list[Paziente], dottore: Dottore):
      self.__pazienti = pazienti
      self.__dottore = dottore

      if dottore.isAValidDoctor():
        self.__fatture = len(pazienti)
        self.__salario: int = 0
      else:
        self.__pazienti = None
        self.__dottore = None
        self.__salario = None
        self.__fatture = None
        print (f"Non è possibile creare la classe fattura poichè il dottore non è valido!")
        
    def getSalario(self):
      self.__salario = self.__dottore.getParcel() * self.fatture
      return self.__salario
    
    def getFatture(self):
      self.__fatture = len(self.__pazienti)
      return self.__fatture
    
    def addPatient (self, new_paziente):
      self.__pazienti.append(new_paziente)
      self.getFatture()
      self.getSalario()
      a = print (f"Alla lista del Dottor {self.__dottore.getLastname()} è stato aggiunto il paziente {new_paziente.getIdCode()}")
      return (a)
    
    def removePatient (self, id_code):
      if self.__patients is not None:
        self.__patients = [p for p in self.__patients if p.getIdCode() != id_code]
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato rimosso il paziente {id_code}")
        
          

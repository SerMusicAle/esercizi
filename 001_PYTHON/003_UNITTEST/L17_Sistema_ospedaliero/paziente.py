"""
### CLASSE: Paziente
    

    paziente 
        nome
        cognome
        età
        id (si usi il tipo String).
    metodi:
        init (__id_code)
    
        setIdCode(id_code)
        getidCode()
        patientInfo()
            output: stampa         
            "Paziente: {nome} {cognome}
            ID: {codice identificativo}"
"""
from persona import Persona

class Paziente(Persona):
#INIT  
    def __init__(self, first_name: str, last_name: str, id_code:str):
        #importa gli input dell'init della classe
        super().__init__(first_name, last_name)
        
        #codice paziente
        if isinstance (id_code, str):
            self.__id_code = id_code
   
    def setIdCode (self, id_code):
        self.__id_code = id_code
    
    def getIdCode (self):
        return self.__id_code
    
    def patentInfo(self):
        a: str = (f"Paziente: {self.getName()} {self.getLastname()} \n"
                   f"ID: {self.getIdCode()}") 
        print (a)
        return a
        

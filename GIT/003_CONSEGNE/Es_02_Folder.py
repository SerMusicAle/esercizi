#DESCRIPTION CLASSE
"""
    classe Student con attributi name str e study program str.
    crea 3 istanze, mia e di due colleghi
    aggiungi metodo printInfo che stampi nomi e programma di studi
    aggiungi età e genere agli attributi.
    
"""

#CLASSE
class Student:
    
    #FUNZIONE __init__
    def __init__ (self, name: str, study_program: str):
        
        #ASSIGMENT
        self.name = name
        self.age = study_program

    #FUNZIONE __str__    
    def __str__ (self):
        return f'il collega {self.name}), sta studiando {self.study_program}, age = {self.age}, gender = {self.gender})'
    
    def set_age (self, new age: int):
        self.age = new_age


    #FUNZIONE add year
    def year (self, name, year):
        self.Student.add(year)

    #FUNZIONE add gendre
    def gendre (self, name, gendre):
        self.Studend.add(gendre)


#ASSIGMENT
ale = Student ("Alice W.", "Basi dati")
francis = Student ("Bob M.", "Python")
gey = Student ("Gey", "java")

Student.printInfo()
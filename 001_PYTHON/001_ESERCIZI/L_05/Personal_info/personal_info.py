"""
3. Personal Info:
    funzione build_profile( name , surname,  occupation, location, and age)
        occupation, location, and age optional parameters. 
        create profiles for different people, demonstrating how it handles these optional parameters.
        Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
"""
import unittest

class Personal_info():
#INIT
    def __init__(self, name:str, surname: str, occupation: str, location:str, age:int):
        self.__name = name
        self.__surname = surname
        self.__occupation = occupation
        self.__location = location
        self.__age = age
#BODY
    def f_set_occupation(self, occupation:str):
        self.__occupation = occupation
        
    def f_set_location(self, location:str):
        self.__location = location
        
    def set_age(self, age:int):
        self.__age = age
        
    def get_occupation(self):
        return self.__occupation
    
    def get_location(self):
        return self.__location
    
    def get_age(self):
        return self.__age
        
#TEST
class TestPersonal(unittest.TestCase):
    
#SETUP
    def setUp(self):
        self.__oggetto = Personal_info ("John", "Doe", occupation="Developer", location="USA", age=30)
        self.__oggetto2 = Personal_info ("Giacomo", "Rossi", occupation="Sviluppatore", location="Italia", age=40)
        
#BODY
    def test_f_set_occupation(self):
        

import unittest

class Personal_info():
    # INIT
    def __init__(self, name: str, surname: str, occupation: str = "", location: str = "", age: int = 0):
        self.__name = name
        self.__surname = surname
        self.__occupation = occupation
        self.__location = location
        self.__age = age
    
    # Metodi per modificare i dati
    def set_occupation(self, occupation: str):
        self.__occupation = occupation
    
    def set_location(self, location: str):
        self.__location = location
    
    def set_age(self, age: int):
        self.__age = age
    
    # Metodo per costruire il profilo
    @classmethod
    def build_profile(cls, name: str, surname: str, occupation: str = "", location: str = "", age: int = 0):
        return cls(name, surname, occupation, location, age)

# Test
class TestPersonal(unittest.TestCase):
    # SETUP
    def setUp(self):
        self.__oggetto = Personal_info("John", "Doe", occupation="Developer", location="USA", age=30)
        self.__oggetto2 = Personal_info("Giacomo", "Rossi", occupation="Sviluppatore", location="Italia", age=40)
    
    # Test per la costruzione del profilo
    def test_build_profile(self):
        profile1 = Personal_info.build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
        profile2 = Personal_info.build_profile("Giacomo", "Rossi", occupation="Sviluppatore", location="Italia", age=40)
        
        self.assertEqual(profile1._Personal_info__name, "John")
        self.assertEqual(profile2._Personal_info__surname, "Rossi")
        
    # Test per la modifica dell'occupazione
    def test_set_occupation(self):
        self.__oggetto.set_occupation("Architect")
        self.assertEqual(self.__oggetto._Personal_info__occupation, "Architect")
        
if __name__ == "__main__":
    unittest.main()

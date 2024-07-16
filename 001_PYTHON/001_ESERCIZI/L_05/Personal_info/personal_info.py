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
    def __init__(self, name:str, surname: str, occupation: str = "", location: str = "", age: int = 0):
        self.__name = name
        self.__surname = surname
        self.__occupation = occupation
        self.__location = location
        self.__age = age
#BODY        
    def f_get_name(self):
        return self.__name
    
    def f_get_surname(self):
        return self.__surname
    
    def f_get_occupation(self):
        return self.__occupation
    
    def f_get_location(self):
        return self.__location
    
    def f_get_age(self):
        return self.__age
    
    def f_define_profile(self):
        profilo_aggiornato = [self.__name, self.__surname]
        if self.__occupation:
            profilo_aggiornato.append (self.__occupation)
        if self.__location:
            profilo_aggiornato.append (self.__location)
        if self.__age:
            profilo_aggiornato.append (str(self.__age))
            
        return " ".join(profilo_aggiornato)    
#TEST
class TestPersonal(unittest.TestCase):
    
#SETUP
    def setUp(self):
        self.__oggetto = Personal_info ("Alessandro", "Sereni")
        self.__oggetto1 = Personal_info ("John", "Doe", occupation = "Developer", age=30)
        self.__oggetto2 = Personal_info ("Giacomo", "Rossi", location="Italia")
        
#BODY*        
    def test_f_get_name(self):
        returned = f"{self.__oggetto.f_get_name()}"
        expected = "Alessandro" 
        self.assertEqual(returned, expected, "ERR F DEFINE PROFILE - valori non corrispondenti")
    
    def test_f_get_surname(self):
        returned = f"{self.__oggetto.f_get_surname()}"
        expected = "Sereni"
        self.assertEqual(returned, expected, "ERR F DEFINE PROFILE - valori non corrispondenti")
    
    def test_f_define_profile(self):
        
        self.assertEqual(self.__oggetto.f_define_profile(), "Alessandro Sereni")
        self.assertEqual(self.__oggetto1.f_define_profile(), "John Doe Developer 30")
        self.assertEqual(self.__oggetto2.f_define_profile(), "Giacomo Rossi Italia")

if __name__ == "__main__":
    unittest.main()
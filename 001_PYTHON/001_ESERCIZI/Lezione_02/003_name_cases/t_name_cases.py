
"""
    2-4. Name Cases: 
    Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
"""
"""
import unittest

class NameCases ():
#INIT
    def __init__(self, name):
        self.__name = name
        
#BODY       
    #function prints some character version of the name
    def f_name_cases(self):
        
        #print the name in uppercase
        self.__uppertext = self.__name.upper()
        #print the name in lowercase
        self.__lowertext = self.__name.lower()
        #print the name  in title case
        self.__titletext = self.__name.title()
        #print the name with the first letter capitalized
        self.__capitalizedtext = self.__name.capitalize()
        #print the name with uppercase letters converted to lowercase and vice versa
        self.__swapcasetext = self.__name.swapcase()

        #export the phrases
        list_name : list = [
            self.__uppertext, 
            self.__lowertext, 
            self.__titletext, 
            self.__capitalizedtext, 
            self.__swapcasetext
            ]

        return list_name
    
#TEST
class TestNamecases (unittest.TestCase):
#SETUP
    def setUp (self):
        self.name: str = "Alessandro"
        self.nometest = NameCases (self.name)
        self.nomi = ['ALESSANDRO', 'alessandro', 'Alessandro', 'Alessandro', 'aLESSANDRO']
#BODY
    def test_f_name_cases (self):
        result_test = self.nometest.f_name_cases()
        self.assertEqual(result_test, self.nomi, "return di una lista non corrispondente")        

#RUN
if __name__ == '__main__':
    unittest.main() 
    
"""
"""
import unittest

class Substract ():
#INIT
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
#BODY        
    def f_substract (self):
        differenza = self.a - self.b
        return differenza
    
class TestSubstract(unittest.TestCase):
#SETUP
    def setUp (self):
        self.a = 10
        self.b = 3
        self.numbers = Substract(self.a, self.b) 
#BODY
    def test_f_substract (self):
        self.assertEqual(self.numbers, (self.a,self.b), "return sottrazzione non corretto")
#RUN
if __name__ == '__main__':
    unittest.main()
        
        
"""
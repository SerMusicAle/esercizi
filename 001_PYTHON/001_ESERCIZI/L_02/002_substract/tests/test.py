import unittest
from substract import Substract

class TestSubstract(unittest.TestCase):
#SETUP
    def setUp (self):
        self.a = 10
        self.b = 3
        self.numbers = Substract(self.a, self.b) 
#BODY
    def test_f_substract (self):
        self.assertEqual(self.numbers.f_substract(), self.a - self.b, "return sottrazzione non corretto")
#RUN
if __name__ == '__main__':
    unittest.main()
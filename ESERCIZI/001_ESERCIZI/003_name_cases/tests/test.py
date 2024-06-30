
import unittest
from name_cases import NameCases

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
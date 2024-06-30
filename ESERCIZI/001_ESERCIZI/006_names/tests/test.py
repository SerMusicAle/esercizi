import unittest
from names import Names 


#RUN
class TestNames (unittest.TestCase):
#SETUP
    def setUp (self):
        self.nomi = ["Marco", "Francesco", "Luigi"]
        self.istanza_nomi = Names(self.nomi)
    
    def test_f_names(self):
        result = self.istanza_nomi.f_names()
        expected = ["Marco", "Francesco", "Luigi"]
        self.assertEqual(result, expected, "ERR. test_f_names. mancata corrispondenza" )    

if __name__ == '__main__':
    unittest.main()
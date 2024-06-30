import unittest
from greetings import Names

#TEST
class test_Names(unittest.TestCase):
#SETUP
    def setUp(self):
        self.nominativi = ["Marco", "Francesco", "Luigi"]
        self.istanza_nomi = Names (self.nominativi)
        
    def test_f_stampa (self):
        self.istanza_nomi.f_stampa()
        
        for nome in self.nominativi:
            expected:str = f"ciao {nome}, benvenuto tra i miei amici"
            self.assertEqual (self.istanza_nomi.messaggi[nome], expected, f"ciao {nome}, benvenuto tra i miei amici")

#RUN
if __name__ == '__main__':
    unittest.main()
    
    

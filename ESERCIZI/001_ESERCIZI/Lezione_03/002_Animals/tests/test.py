import unittest
from animals import Animals

class TestNomeClasse (unittest.TestCase):
#SETUP
    def setUp (self):
        self.__animali: list[str] = ["leone", "'antilope", "coccodrillo"]
        self.oggetto = Animals (self.__animali)
#BODY        
    def test_f_stampa (self):
        returned = self.oggetto.f_stampa()
        expected: list[str] = []
        for animale in self.__animali:
            expected.append(animale)
        self.assertEqual (returned, expected, "ERR. F STAMPA - elenco non corrispondente")
    
    def test_f_descrizione (self):
        expected: dict [str,str] = {
            "leone": "avere un leone come animale domestico mi piace", 
            "'antilope": "avere un 'antilope come animale domestico mi piace", 
            "coccodrillo": "avere un coccodrillo come animale domestico mi piace"
        }         
        returned = self.oggetto.f_descrizione()
        self.assertEqual (returned, expected, "ERR. F DESCRIZIONE - dizionari descrizione non corrispondenti")

    def test_conclusione(self):
        expected: str = "Qualsiasi di questi animali sarebbe un ottimo animale domestico!"
        returned = self.oggetto.conclusione()
        self.assertEqual (returned, expected, "ERR. CONCLUSIONE - messaggio conclusione non corrispondente")


#RUN
if __name__ == '__main__':
    unittest.main()        

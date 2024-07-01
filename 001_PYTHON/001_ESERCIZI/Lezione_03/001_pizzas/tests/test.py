import unittest
from pizzas import Pizzas

class TestNomeClasse (unittest.TestCase):
#SETUP
    def setUp (self):
        self.pizzas: list[str] = ["Salmone e zucchine", "Friarielli e salsiccie", "Boscaiola"]
        self.istanza = Pizzas (self.pizzas)
        
    def test_f_stampalist (self):
        expectedlist = self.pizzas
        returnedlist = self.istanza.f_stampalist()
        
        self.assertEqual (returnedlist, expectedlist, "ERR.F_STAMPALIST - il risultato prodotto non è corrispondente")

    def test_f_stampadict(self):    
        expecteddict: dict [str, str] = {}
        returneddict: dict [str,str] = self.istanza.f_stampadict()
        
        for pizza in self.pizzas:
            expecteddict[pizza] = f"mi piace la pizza {pizza}"
        self.assertEqual (returneddict, expecteddict, "ERR. F_STAMPADICT - il risultato prodotto non è corrispondente")

#RUN
if __name__ == '__main__':
    unittest.main()        



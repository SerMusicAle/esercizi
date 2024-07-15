import unittest
from your_own import YourOwn


class test_YourOwn (unittest.TestCase):

#SETUP
    def setUp (self):
        self.mezzi = ["auto Tesla", "motocicletta Ducati", "bicicletta Bianchi"]
        self.pensieri = ["è una ficata", "non mi fa impazzire", "mi è indifferente"]
        self.oggetto = YourOwn (self.mezzi, self.pensieri)
#BODY
    def test_f_stampa (self):
        expected: list[str] = []
        
        for mezzo in self.mezzi:
            for pensiero in self.pensieri:
                expected.append (f"{mezzo} {pensiero}")
        
        concetti = self.oggetto.f_stampa()
                
        self.assertEqual (concetti,  expected, "ERR. TEST F STAMPA. mancata coincidenza"  )
  

        
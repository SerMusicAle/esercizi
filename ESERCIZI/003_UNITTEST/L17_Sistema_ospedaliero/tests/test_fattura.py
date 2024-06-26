    
"""
Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista.
"""

import unittest
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

#TEST DOTTORE          
class TestFattura(unittest.TestCase):
  
    def setUp(self):
        paziente1 = Paziente(first_name= "Flavio", last_name= "Gilberti", id_code= "A001")
        paziente2 = Paziente(first_name= "Marco", last_name= "-Mareschi", id_code= "A002")
        paziente3 = Paziente(first_name= "Giuseppe", last_name= "Cicci", id_code= "A003")
        pazienti = [paziente1, paziente2, paziente3]
        dottore = Dottore ("Franco", "Verdi", "Odontoiatra", 3500.00)
        self.fattura= Fattura(pazienti,dottore)
        

    def test_init (self):
        self.pazienti = [
                {"nome": "Mario", "età": 30},
                {"nome": "Luigi", "età": 25},
                {"nome": "Anna", "età": 22}
        ]
        self.dottore = Dottore ("Franco", "Verdi", "Odontoiatra", 3500.00)
        
        self.assertEqual(self.fattura.__pazienti, self.pazienti)
        self.assertEqual(self.pazienti, self.pazienti)
        
    def test_addPatient(self):
        new_paziente = Paziente(first_name = "Alice", last_name = "Freschi", id_code = "A004")
        self.fattura.addPatient(self.newPatient)
        
    def test_removePatient (self):
        new_paziente = Paziente(first_name = "Alice", last_name = "Freschi", id_code = "A004")
        self.fattura.removePatient(self.new_paziente.getIdCode())
        
        
if __name__ == '__main__':
    unittest.main()
    
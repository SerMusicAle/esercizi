"""
Esercizio 7: Ereditarietà e Polimorfismo
    Aggiungi un metodo descrizione() alla classe Animale che descriva l'animale. 
    Sovrascrivi questo metodo nelle classi Cane e Gatto per fornire descrizioni specifiche.
"""

from abc import ABC, abstractmethod
import unittest

class Animale (ABC):
#INIT
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def f_verso (self):
        pass
    
    @abstractmethod
    def f_descrizione(self):
        pass

class Cane(Animale):
#INIT
    def __init__(self):
        super().__init__()
    
    def f_verso (self):
        verso: str = "abbaiare" 
        return (verso)
    
    def f_descrizione(self):
        descrizione: str = "il cane ha 4 zampe"
        return descrizione
        
class Gatto (Animale):
#INIT
    def __init__(self):
        super().__init__()
    
    def f_verso(self):
        verso: str = "miagolare"
        return (verso)
    
    def f_descrizione(self):
        descrizione: str = "il gatto ha 4 zampe"
        return descrizione
        
class TestAnimale(unittest.TestCase):
#SETUP
    def setUp (self):
        self.oggetto_cane = Cane()
        self.oggetto_gatto = Gatto()
    
    def test_f_verso(self):
        returned_verso_cane = self.oggetto_cane.f_verso()
        returned_verso_gatto = self.oggetto_gatto.f_verso()
        expected_verso_cane: str = "abbaiare"
        expected_verso_gatto: str = "miagolare"
        
        self.assertEqual(returned_verso_cane, expected_verso_cane, "ERR. FUNC VERSO CANE - verso non corrispondente")
        self.assertEqual(returned_verso_gatto, expected_verso_gatto, "ERR. FUNC VERSO GATTO - verso non corrispondente")
        
    def test_f_descrizione(self):
        returned_desc_cane = self.oggetto_cane.f_descrizione()
        returned_desc_gatto = self.oggetto_gatto.f_descrizione()
        expected_desc_cane = "il cane ha 4 zampe"
        expected_desc_gatto = "il gatto ha 4 zampe"
        
        self.assertEqual(returned_desc_cane, expected_desc_cane, "ERR. FUNC DESCRIZIONE CANE - descrizione non corrispondente")
        self.assertEqual(returned_desc_gatto, expected_desc_gatto, "ERR. FUNC DESCRIZIONE GATTO - descrizione non corrispondente")
        
#RUN
if __name__ == '__main__':
    unittest.main()   
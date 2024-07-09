"""
Esercizio 1: Ereditarietà tra Classi
    Crea una gerarchia di classi per rappresentare animali. 
    Includi una classe base Animale e due classi derivate Cane e Gatto. 
    Implementa un metodo fa_suono() per ogni classe che restituisca il suono fatto dall'animale.
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

class Cane(Animale):
#INIT
    def __init__(self):
        super().__init__()
    
    def f_verso (self):
        verso: str = "abbaiare" 
        return (verso)
    
class Gatto (Animale):
#INIT
    def __init__(self):
        super().__init__()
    
    def f_verso(self):
        verso: str = "miagolare"
        return (verso)
        
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

#RUN
if __name__ == '__main__':
    unittest.main()   
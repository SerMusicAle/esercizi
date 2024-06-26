    
"""
    Test della Classe Paziente
    - Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
    - Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
    - Scrivere test per verificare:
    - L'inizializzazione corretta degli attributi specifici di Paziente.        
            
"""

import unittest
from paziente import Paziente

#TEST PAZIENTE
class TestPersona(unittest.TestCase):

    def setUp(self):    
        self.paziente = Paziente(first_name = "Maurizio", last_name = "Cocci", id_code = "A001")

    def test_init(self):  
        self.assertEqual (self.paziente.getName(), "Maurizio","Errore init - nome")
        self.assertEqual (self.paziente.getLastname(), "Cocci", "Errore init - cognome")
        self.assertEqual (self.paziente.getIdCode(), "A001", "errore init - codice errato")
    
    def test_set_id (self):
        self.paziente.setIdCode("A001")
        self.assertEqual(self.paziente.getIdCode(), "A001", "Errore set id")
        
    def test_patient_info (self):
        self.assertEqual(self.paziente.patentInfo(), "Paziente: Maurizio Cocci \n"
                                                     "ID: A001")
    
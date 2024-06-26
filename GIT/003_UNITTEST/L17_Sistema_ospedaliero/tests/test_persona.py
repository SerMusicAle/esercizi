"""
  Test della Classe Persona
  - Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
  - Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
  - Scrivere test per verificare:
    - L'inizializzazione corretta degli attributi first_name, last_name e age.
    - Il funzionamento dei metodi setName, setLastName e setAge.      
      
"""
#TEST PERSONA
import unittest
from persona import Persona
#from dottore import Dottore
#from paziente import Paziente
#from fattura import Fattura

class TestPersona(unittest.TestCase):

    def setUp(self):
        self.persona = Persona(first_name = "Mario", last_name = "Rossi")

    def test_init(self):  
        self.assertEqual (self.persona.getName(), "Mario","Nome non impostato")
        self.assertEqual (self.persona.getLastname(), "Rossi","Cognome non impostato")
        self.assertEqual (self.persona.getAge(), 0)         

    def test_setName(self):
        self.persona.setName('Luigi')
        self.assertEqual(self.persona.getName(), 'Luigi', "il setName è fallito.")
        
    def test_setLastname(self):
        self.persona.setLastname('Verdi')
        self.assertEqual(self.persona.getLastname(), 'Verdi', "il setLastname è fallito")

    def test_setAge(self):
        self.persona.setAge(25)
        self.assertEqual(self.persona.getAge(), 25,"il setAge è fallito.")

    def test_greet(self):
        self.persona.setAge(30)
        greeting = self.persona.greet()
        self.assertEqual(greeting, 'Ciao, sono Mario Rossi Ho 30 anni')

if __name__ == '__main__':
    unittest.main()


"""

Test della Classe Paziente
- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Paziente.

Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista.

"""         

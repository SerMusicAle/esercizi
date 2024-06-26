"""
Test della Classe Dottore
- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Dottore 
  con nome, cognome, specializzazione e parcella.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Dottore.
  - Il funzionamento del metodo isValidDoctor con diverse età.      
      
"""

import unittest
from dottore import Dottore

#TEST DOTTORE          
class TestDottore(unittest.TestCase):
  
  #istanza dottore e variabili necessarie
  def setUp(self):
    self.dottore = Dottore ("Franco", "Verdi", "Odontoiatra", 3500.00)
    self.dottore.setAge(35)
  
  #verifica init  
  def test_init (self):
    self.assertEqual(self.dottore.getName(), "Franco")
    self.assertEqual(self.dottore.getLastname(), "Verdi")
    self.assertEqual(self.dottore.getSpecialization(),"Odontoiatra")
    self.assertEqual(self.dottore.getParcel(), 3500.00)
    self.assertEqual(self.dottore.getAge(), 40)
  
  #verifica immissione specializzazione  
  def test_set_specialization(self):
    #self.dottore = Dottore ("Franco", "Verdi", "Odontoiatra", 3500.00)
    self.dottore.setSpecialization("Dentista")
    self.assertEqual(self.dottore.getSpecialization(), "Dentista", "errore set Specialization") 

  #estrai specializzazione
  def test_get_specialization (self):
    self.assertEqual (self.dottore.getSpecialization(), "Odontoiatra", "specializzazione non corrispondente")
  
  #estrai parcella
  def test_get_parcel (self):
    self.assertEqual (self.dottore.getParcel(), 3500.00, "Parcella non corrispondente")
  
  #verifica se l'età sia valida
  def test_is_a_doctor (self):
    self.assertEqual (self.dottore.getAge(),self.dottore.getAge()>30, "non è un dottore" )
  
  def test_set_age (self):
    self.dottore.setAge(35)
    self.assertEqual (self.dottore.getAge(), 35, "errore set age")
  
  def test_doctor_greet (self):
    self.dottore.setAge(35)
    self.assertEqual (self.dottore.doctorGreet(), f'Ciao, sono Franco Verdi Ho 35 anni'
                                                  "Sono un medico Odontoiatra", "errore nel resoconto Greet delle informazioni")

if __name__ == '__main__':
    unittest.main()
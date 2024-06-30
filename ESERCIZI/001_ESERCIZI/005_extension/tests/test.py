import unittest
from extension import Extension 

#RUN
class TestExtension (unittest. TestCase):
#SETUP
    def setUp(self):
        self.try_case = Extension ("nome_file_testo.txt")
        
    def test_f_no_extension (self):
        expected = "nome_file_testo"
        result = self.try_case.f_no_extension()
        self.assertEqual(result, expected, "l'operazione non ha restituito il nome del file senza estensione")
        
# RUN
if __name__ == '__main__':
    unittest.main()
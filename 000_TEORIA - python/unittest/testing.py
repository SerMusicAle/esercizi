import unittest
from operatore.ripasso import Calc  # Correggi l'importazione secondo la struttura del tuo progetto

class TestCalculations(unittest.TestCase):

    def setUp(self):
        self.calculation = Calc(0, 2)
                                
    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 2, "The sum is wrong.")  # La somma di 0 e 2 è 2

if __name__ == "__main__":
    unittest.main()
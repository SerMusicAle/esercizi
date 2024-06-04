import unittest
from ..operatore.ripasso import Calc

class TestCalculations (unittest.TestCase):

    def setUp(self):
        self.calculation = Calc(0,2)
                                
    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(), 10, "The sum is wrong.")

if __name__ == "__main__":
    unittest.main()


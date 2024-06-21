import unittest

class TestUnittestAssertions(unittest.TestCase):

    def test_assertEqual(self):
        # Verifica che a e b siano uguali
        self.assertEqual(3 + 2, 5)

    def test_assertNotEqual(self):
        # Verifica che a e b non siano uguali
        self.assertNotEqual(3 + 2, 6)

    def test_assertTrue(self):
        # Verifica che x sia True
        self.assertTrue(1 + 1 == 2)

    def test_assertFalse(self):
        # Verifica che x sia False
        self.assertFalse(1 + 1 == 3)

    def test_assertIs(self):
        # Verifica che a e b siano lo stesso oggetto
        a = b = []
        self.assertIs(a, b)

    def test_assertIsNot(self):
        # Verifica che a e b non siano lo stesso oggetto
        a = []
        b = []
        self.assertIsNot(a, b)

    def test_assertIsNone(self):
        # Verifica che x sia None
        x = None
        self.assertIsNone(x)

    def test_assertIsNotNone(self):
        # Verifica che x non sia None
        x = 1
        self.assertIsNotNone(x)

    def test_assertIn(self):
        # Verifica che a sia in b
        self.assertIn(3, [1, 2, 3])

    def test_assertNotIn(self):
        # Verifica che a non sia in b
        self.assertNotIn(4, [1, 2, 3])

    def test_assertIsInstance(self):
        # Verifica che a sia un'istanza di b
        self.assertIsInstance(3, int)

    def test_assertNotIsInstance(self):
        # Verifica che a non sia un'istanza di b
        self.assertNotIsInstance(3, str)

    def test_assertGreater(self):
        # Verifica che a sia maggiore di b
        self.assertGreater(5, 3)

    def test_assertGreaterEqual(self):
        # Verifica che a sia maggiore o uguale a b
        self.assertGreaterEqual(5, 5)

    def test_assertLess(self):
        # Verifica che a sia minore di b
        self.assertLess(3, 5)

    def test_assertLessEqual(self):
        # Verifica che a sia minore o uguale a b
        self.assertLessEqual(3, 3)

    def test_assertRaises(self):
        # Verifica che venga sollevata l'eccezione exception quando si chiama callable
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_assertRaisesRegex(self):
        # Verifica che venga sollevata l'eccezione exception e che il messaggio dell'eccezione corrisponda a regex
        with self.assertRaisesRegex(ValueError, "invalid literal for int()"):
            int('abc')

    def test_assertWarns(self):
        # Verifica che venga emesso l'avviso warning quando si chiama callable
        import warnings
        with self.assertWarns(DeprecationWarning):
            warnings.warn("deprecated", DeprecationWarning)

    def test_assertWarnsRegex(self):
        # Verifica che venga emesso l'avviso warning e che il messaggio dell'avviso corrisponda a regex
        import warnings
        with self.assertWarnsRegex(DeprecationWarning, "deprecated"):
            warnings.warn("deprecated", DeprecationWarning)

    def test_assertLogs(self):
        # Verifica che vengano generati messaggi di log al livello specificato
        import logging
        logger = logging.getLogger('mylogger')
        with self.assertLogs(logger, level='INFO') as log:
            logger.info('Hello, world!')
            self.assertIn('INFO:mylogger:Hello, world!', log.output)

if __name__ == "__main__":
    unittest.main()


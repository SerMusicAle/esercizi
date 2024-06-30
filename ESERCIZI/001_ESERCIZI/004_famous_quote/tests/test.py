import unittest
from famous_quote import FamousQuote 

#TEST
class TestFamousQuote(unittest.TestCase):
#SETUP
    def setUp (self):
        self.famous_quote = FamousQuote()
    
    def test_f_quotes(self):
        # Test for Einstein
        expected = 'Einstein una volta disse: "la vita è come una bicicletta"'
        result = self.famous_quote.f_quotes('Einstein')
        self.assertEqual(result, expected, "La citazione non corrisponde a quella attesa per Einstein")
        
        # Test for Mandela
        expected = 'Mandela una volta disse: "La istruzione è l\'arma più potente"'
        result = self.famous_quote.f_quotes('Mandela')
        self.assertEqual(result, expected, "La citazione non corrisponde a quella attesa per Mandela")
        
        # Test for Jobs
        expected = 'Jobs una volta disse: "Stay hungry, stay foolish"'
        result = self.famous_quote.f_quotes('Jobs')
        self.assertEqual(result, expected, "La citazione non corrisponde a quella attesa per Jobs")
    
    # Test for invalid VIP
    def test_f_quotes_invalid(self):
        expected = 'inserisci il nome corretto'
        result = self.famous_quote.f_quotes('Unknown')
        self.assertEqual(result, expected, "Il messaggio per VIP sconosciuto non è corretto")

# RUN
if __name__ == '__main__':
    unittest.main()
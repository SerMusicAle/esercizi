import unittest
from L_20_Pagamento import Pagamento, Pagamento_contanti, Pagamento_carta


class Test_pagamento (unittest.TestCase):
    
    def setUp (self):
        self.test_importo = 76523.8765
        self.pagamento = Pagamento (self.test_importo)

    
    def test_init (self):
        self.assertEqual (self.pagamento.f_get(), round (self.test_importo,2) )
        
    def test_f_set (self):
        self.test_set_importo = 345.5566
        self.test_set_oggetto = Pagamento (self.test_set_importo)
        self.test_set_oggetto = Pagamento (876.7654)
        self.test_set_oggetto.f_set(self.test_set)
        self.assertEqual (self.pagamento.f_get(), round (self.test_f_set,2) )
             

class TestPagamentoContanti(unittest.TestCase):

    def setUp (self):
        importo_contanti = 928365.234
        importo_carta = 76523.8765
        pagamento_contanti1 = Pagamento_contanti (928365.234)  
        pagamento_carta1 = Pagamento_carta (
            importo = 76523.8765, 
            nome = "Alessandro", 
            cognome = "Sereni", 
            data = "23-06-2030", 
            ncarta = 28363464934976
        )     
    
    def test_init (self):
        test_importo = 928365.234
        self.
        
        self.assertequal(self.__importo, test_importo)
            
    def test_f_dettagli_pagamento(self):
        self.assertEqual(Pagamento.a, )
        pagamento_contanti = Pagamento_contanti(928365.234)
        expected_output = "Questo pagamento è in contanti:\n"
        
        with StringIO() as buffer, redirect_stdout(buffer):
            pagamento_contanti.f_dettagli_pagamento()
            self.assertEqual(buffer.getvalue(), expected_output)

    def test_f_pezzi_da(self):
        pagamento_contanti = Pagamento_contanti(928365.234)
        expected_output = [
            "sono necessarie 1856 banconote da 500 euro",
            "sono necessarie 1 banconote da 200 euro",
            "sono necessarie 1 banconote da 100 euro",
            "sono necessarie 1 banconote da 50 euro",
            "sono necessarie 1 banconote da 10 euro",
            "sono necessarie 1 banconote da 5 euro",
            "sono necessarie 1 monete da 0.20 euro",
            "sono necessarie 1 monete da 0.05 euro",
            "sono necessarie 1 monete da 0.01 euro"
        ]
        
        with StringIO() as buffer, redirect_stdout(buffer):
            pagamento_contanti.f_pezzi_da()
            output_lines = buffer.getvalue().strip().split("\n")
            for line, expected_line in zip(output_lines, expected_output):
                self.assertIn(expected_line, line)

class TestPagamentoCarta(unittest.TestCase):

    def test_f_dettagli_pagamento(self):
        pagamento_carta = Pagamento_carta(76523.8765, "Alessandro", "Sereni", "23-06-2030", 28363464934976)
        expected_output = [
            f"L'importo del pagamento è: 76523.88€",
            f"Il pagante è Alessandro Sereni. La sua carta n° 28363464934976 scade il 23-06-2030"
        ]
        
        with StringIO() as buffer, redirect_stdout(buffer):
            pagamento_carta.f_dettagli_pagamento()
            output_lines = buffer.getvalue().strip().split("\n")
            for line, expected_line in zip(output_lines, expected_output):
                self.assertIn(expected_line, line)

if __name__ == "__main__":
    unittest.main()


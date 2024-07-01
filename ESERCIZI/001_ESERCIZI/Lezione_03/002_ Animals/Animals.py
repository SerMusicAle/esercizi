"""
4-2. Animali: 
    Pensa ad almeno tre animali diversi che abbiano una caratteristica comune. 
    Memorizza i nomi di questi animali in una lista 
    e poi utilizza un ciclo for per stampare il nome di ciascun animale.
    • Modifica il tuo programma per stampare un'affermazione su ciascun animale, 
        come ad esempio "Un cane sarebbe un ottimo animale domestico".
    • Aggiungi una riga alla fine del tuo programma, indicando cosa hanno in comune questi animali. 
        Potresti stampare una frase come "Qualsiasi di questi animali sarebbe un ottimo animale domestico!"

"""
import unittest

class Animals ():
#INIT
    def __init__ (self, animali:list [str]):
        self.__animali = animali
#BODY    
    def f_stampa (self):
        return_animali: list[str] = []
        for animale in self.__animali:
            return_animali.append(animale) 
        
        return return_animali
            
    def f_descrizione (self):
        descrizione: dict [str,str] = {}
        for animale in self.__animali:
            descrizione[animale] = f"avere un {animale} come animale domestico mi piace" 
            
        return descrizione
    
    def conclusione (self):
        conclusione:str = "Qualsiasi di questi animali sarebbe un ottimo animale domestico!"
        
        return conclusione
    
class TestNomeClasse (unittest.TestCase):
#SETUP
    def setUp (self):
        self.__animali: list[str] = ["leone", "'antilope", "coccodrillo"]
        self.oggetto = Animals (self.__animali)
#BODY        
    def test_f_stampa (self):
        returned = self.oggetto.f_stampa()
        expected: list[str] = []
        for animale in self.__animali:
            expected.append(animale)
        self.assertEqual (returned, expected, "ERR. F STAMPA - elenco non corrispondente")
    
    def test_f_descrizione (self):
        expected: dict [str,str] = {
            "leone": "avere un leone come animale domestico mi piace", 
            "'antilope": "avere un 'antilope come animale domestico mi piace", 
            "coccodrillo": "avere un coccodrillo come animale domestico mi piace"
        }         
        returned = self.oggetto.f_descrizione()
        self.assertEqual (returned, expected, "ERR. F DESCRIZIONE - dizionari descrizione non corrispondenti")

    def test_conclusione(self):
        expected: str = "Qualsiasi di questi animali sarebbe un ottimo animale domestico!"
        returned = self.oggetto.conclusione()
        self.assertEqual (returned, expected, "ERR. CONCLUSIONE - messaggio conclusione non corrispondente")


#RUN
if __name__ == '__main__':
    unittest.main()        

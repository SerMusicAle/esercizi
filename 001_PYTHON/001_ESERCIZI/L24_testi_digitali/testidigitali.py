import unittest
# import os


class Documento ():
#INIT
    def __init__(self, testo:str):
        self.testo = testo

#BODY
    def f_get_testo(self):
        return self.testo

    def f_set_testo(self, testo:str):
        self.testo = testo
        return self.testo
    
    def f_is_in_testo (self, parola:str):
        return parola in self.testo
    
class Email(Documento):
#INIT
    def __init__(self, mittente:str, destinatario:str, titolo:str, testo:str):
        super().__init__(testo)
        self.__mittente = mittente
        self.__destinatario = destinatario
        self.__titolo = titolo
        self.__percorso = "file.txt"
        
    def f_get_testo(self):
        testo = super().f_get_testo()
        return testo
    
    def f_set_testo(self, testo:str):
        self.__testo = super().f_set_testo(testo)
        return self.__testo
    
    def f_get_mittente (self):
        return self.__mittente

    def f_get_destinatario (self):
        return self.__destinatario
    
    def f_get_titolo (self):
        return self.__titolo
    
    def f_get_email(self):
        self.email: str = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.f_get_testo()}"
        return self.email
    
    def f_set_to_file(self):        
        with open (self.__percorso, 'w') as file:
            file.write(self.f_get_email())
            

            

#TEST
class TestDocumento(unittest.TestCase):
#SETUP
    def setUp(self):
        #attriubuti oggetto
        self.__testo: str = "Mi è piaciuta l'esperienza di orienteering avuta insieme"
        #oggetto
        self.__oggetto = Documento (self.__testo)

    def test_init(self):
        returned = self.__oggetto.f_get_testo()
        
        self.assertEqual(self.__testo, returned, "ERR. TEST INIT - testo non corrispondente")
        
    def test_f_get_testo(self):
        returned = self.__oggetto.f_get_testo()
        
        self.assertEqual(self.__testo, returned, "ERR. TEST F_GET_TEXT - testo non corrispondente")
        
    def test_f_set_testo(self):
        self.__oggetto.f_set_testo(self.__testo)
        returned = self.__oggetto.f_get_testo()
        
        self.assertEqual(self.__testo, returned, "ERR. TEST F_SET_TEXT - testo non corrispondente")

    def test_f_is_in_testo(self):
        self.__oggetto.f_set_testo(self.__testo)
        returned = self.__oggetto.f_is_in_testo("piaciuta")
        
        self.assertEqual(returned, True, "ERR. F IF IS IN TEXT - risultato non corrispondente")
        
class TestEmail(unittest.TestCase):

    def setUp (self):
        #parametri
        self.__mittente: str = "Alessandro"
        self.__destinatario: str = "Flavia"
        self.__titolo:str = "Orienteering che passione"
        self.__testo:str = "Mi è piaciuta l'esperienza di orienteering avuta insieme"
        self.__mail_text: str = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.__testo}"
        
        #oggetto
        self.__email = Email (self.__mittente, self.__destinatario, self.__titolo, self.__testo)

        self.__file_path = 'file.txt'

    def test_init(self):
        ret_testo: str = self.__email.f_get_testo()
        ret_titolo: str = self.__email.f_get_titolo()
        ret_mittente:str = self.__email.f_get_mittente()
        ret_destinatario:str = self.__email.f_get_destinatario()
        
        self.assertEqual(ret_testo, self.__testo, "ERR INIT - testo non corrispondente")
        self.assertEqual(ret_mittente, self.__mittente, "ERR INIT - mittente non corrispondente")
        self.assertEqual(ret_destinatario, self.__destinatario, "ERR INIT - destinatario non corrispondente")
        self.assertEqual(ret_titolo, self.__titolo, "ERR INIT - titolo non corrispondente")
    
    def test_f_get_testo(self):
        returned: str = self.__email.f_get_testo()
        self.assertEqual(returned, self.__testo, "ERR. F GET TESTO - mancata corrispondenza")

    def test_f_set_testo(self):
        self.__email.f_set_testo(self.__testo)
        returned: str = self.__email.f_get_testo()
        self.assertEqual(returned, self.__testo, "ERR F. SET TESTO - mancata corrispondenza")

    def test_f_get_mittente(self):
        returned: str = self.__email.f_get_mittente()
        self.assertEqual (returned, self.__mittente, "ERR F. GET MITTENTE - mancata corrispondenza")

    def test_f_get_destinatario(self):
        returned: str = self.__email.f_get_destinatario()
        self.assertEqual (returned, self.__destinatario, "ERR F GET DESTINATARIO - mancata corrispondenza")
        
    def test_f_get_titolo(self):
        returned: str = self.__email.f_get_titolo()
        self.assertEqual(returned, self.__titolo, "ERR F GET TITOLO - mancata corrispondenza")

    def test_f_get_email(self):
        returned: str = self.__email.f_get_email() 
        self.assertEqual (returned, self.__mail_text, "ERR F GET EMAIL - mancata corrispondenza")

    def test_f_set_to_file(self):
        self.__email.f_set_to_file()
        
        with open(self.__file_path, 'r') as file:
            returned: str = file.read()
        
        self.assertEqual(returned,self.__mail_text, "ERR F SET TO FILE - risultato non corrispondente")

if __name__ == "__main__":
    unittest.main()
    
"""
        import unittest
# import os


class Documento ():
#INIT
    def __init__(self, testo:str):
        self.testo = testo

#BODY
    def f_get_testo(self):
        return self.testo

    def f_set_testo(self, testo:str):
        self.testo = testo
        return self.testo
    
    def f_is_in_testo (self, parola:str):
        return parola in self.testo
    
class Email(Documento):
#INIT
    def __init__(self, mittente:str, destinatario:str, titolo:str, testo:str):
        super().__init__(testo)
        self.__mittente = mittente
        self.__destinatario = destinatario
        self.__titolo = titolo
        self.__percorso = "file.txt"
        
    def f_get_testo(self):
        testo = super().f_get_testo()
        return testo
    
    def f_set_testo(self, testo:str):
        self.__testo = super().f_set_testo(testo)
        return self.__testo
    
    def f_get_mittente (self):
        return self.__mittente

    def f_get_destinatario (self):
        return self.__destinatario
    
    def f_get_titolo (self):
        return self.__titolo
    
    def f_get_email(self):
        self.email: str = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.f_get_testo()}"
        return self.email
    
    def f_set_to_file(self):        
        with open (self.__percorso, 'w') as file:
            file.write(self.email)
            

            

#TEST
class TestDocumento(unittest.TestCase):
#SETUP
    def setUp(self):
        #attriubuti oggetto
        self.__testo: str = "Mi è piaciuta l'esperienza di orienteering avuta insieme"
        #oggetto
        self.__oggetto = Documento (self.__testo)

    def test_init(self):
        returned = self.__oggetto.f_get_testo()
        
        self.assertEqual(self.__testo, returned, "ERR. TEST INIT - testo non corrispondente")
        
    def test_f_get_testo(self):
        returned = self.__oggetto.f_get_testo()
        
        self.assertEqual(self.__testo, returned, "ERR. TEST F_GET_TEXT - testo non corrispondente")
        
    def test_f_set_testo(self):
        self.__oggetto.f_set_testo(self.__testo)
        returned = self.__oggetto.f_get_testo()
        
        self.assertEqual(self.__testo, returned, "ERR. TEST F_SET_TEXT - testo non corrispondente")

    def test_f_is_in_testo(self):
        self.__oggetto.f_set_testo(self.__testo)
        returned = self.__oggetto.f_is_in_testo("piaciuta")
        
        self.assertEqual(returned, True, "ERR. F IF IS IN TEXT - risultato non corrispondente")
        
class TestEmail(unittest.TestCase):

    def setUp (self):
        #parametri
        self.__mittente: str = "Alessandro"
        self.__destinatario: str = "Flavia"
        self.__titolo:str = "Orienteering che passione"
        self.__testo:str = "Mi è piaciuta l'esperienza di orienteering avuta insieme"
        self.__mail_text: str = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.__testo}"
        
        #oggetto
        self.__email = Email (self.__mittente, self.__destinatario, self.__titolo, self.__testo)

        self.__file_path = 'file.txt'

    def test_init(self):
        ret_testo: str = self.__email.f_get_testo()
        ret_titolo: str = self.__email.f_get_titolo()
        ret_mittente:str = self.__email.f_get_mittente()
        ret_destinatario:str = self.__email.f_get_destinatario()
        
        self.assertEqual(ret_testo, self.__testo, "ERR INIT - testo non corrispondente")
        self.assertEqual(ret_mittente, self.__mittente, "ERR INIT - mittente non corrispondente")
        self.assertEqual(ret_destinatario, self.__destinatario, "ERR INIT - destinatario non corrispondente")
        self.assertEqual(ret_titolo, self.__titolo, "ERR INIT - titolo non corrispondente")
    
    def test_f_get_testo(self):
        returned: str = self.__email.f_get_testo()
        self.assertEqual(returned, self.__testo, "ERR. F GET TESTO - mancata corrispondenza")

    def test_f_set_testo(self):
        self.__email.f_set_testo(self.__testo)
        returned: str = self.__email.f_get_testo()
        self.assertEqual(returned, self.__testo, "ERR F. SET TESTO - mancata corrispondenza")

    def test_f_get_mittente(self):
        returned: str = self.__email.f_get_mittente()
        self.assertEqual (returned, self.__mittente, "ERR F. GET MITTENTE - mancata corrispondenza")

    def test_f_get_destinatario(self):
        returned: str = self.__email.f_get_destinatario()
        self.assertEqual (returned, self.__destinatario, "ERR F GET DESTINATARIO - mancata corrispondenza")
        
    def test_f_get_titolo(self):
        returned: str = self.__email.f_get_titolo()
        self.assertEqual(returned, self.__titolo, "ERR F GET TITOLO - mancata corrispondenza")

    def test_f_get_email(self):
        returned: str = self.__email.f_get_email() 
        self.assertEqual (returned, self.__mail_text, "ERR F GET EMAIL - mancata corrispondenza")

    def test_f_set_to_file(self):
        self.__email.f_set_to_file()
        
        with open(self.__file_path, 'r') as file:
            returned: str = file.read()
        
        self.assertEqual(returned,self.__mail_text, "ERR F SET TO FILE - risultato non corrispondente")

if __name__ == "__main__":
    unittest.main()
    

        """
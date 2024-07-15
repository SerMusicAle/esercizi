import os
import unittest

class Documento ():
#INIT
    def __init__(self, testo:str):
        self.__testo = testo

#BODY
    def f_get_testo(self):
        return self.__testo

    def f_set_testo(self, testo:str):
        self.__testo = testo
        return self.__testo
    
    def f_is_in_testo (self, parola:str):
        return parola in self.__testo
    
class Email(Documento):
#INIT
    def __init__(self, mittente:str, destinatario:str, titolo:str, testo:str):
        super().__init__(testo)
        self.__mittente = mittente
        self.__destinatario = destinatario
        self.__titolo = titolo
        
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
        email: str = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.f_get_testo()}"
        return email
    
    def f_set_to_file(self):
        email = self.f_get_email()
        
        os.makedirs('file_generato', exist_ok=True)
        with open ('file_generato/file.txt', 'w') as file:
            file.write(email)

class File (Documento):
#INIT
    def __init__(self, testo:str, percorso:str):
        super().__init__(testo)
        self.__testo = testo
        self.__percorso = percorso
    
    def f_get_percorso (self):
        return self.__percorso
        
    def f_create_file(self):
        os.makedirs(os.path.dirname(self.__percorso), exist_ok=True)
        with open(self.__percorso, 'w') as file:
            file.write(self.__testo)
            
    def f_leggi_testo_da_file (self):
        with open(self.__percorso, 'r') as file:
            self.contenuto = file.read()
            return self.contenuto
            
    def f_get_testo(self):
        concatenazione: str = f"{self.__percorso}, {self.__testo}"
        return concatenazione
        
    
    
       
"""
# Testi Digitali
    CLASS Documento 
        contiene una variabile  stringa chiamata testo e che memorizza qualsiasi contenuto testuale per il documento.

    METODI
        getText() che restituisca il testo.
        setText() per impostare il testo. 
        isInText() che restituisce True se un documento contiene la parola chiave specificata.
        
    CLASS Email (Documento) 
        var mittente, destinatario e titolo del messaggio.
    
    METODI EMAIL
        get() 
        set() aggiorna il testo.
        getText() concatena e ritorna (mittente, destinatario, titolo del messaggio, e messaggio) come di seguito:
    
        Da: alice@example.com, A: bob@example.com
        Titolo: Incontro
        Messaggio: Ciao Bob, possiamo incontrarci domani?
    
        writeToFile() scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
    
    CLASS File(Documento) 
        variabile per il nomePercorso.
    
    METODI FILE
        createfile() Crea document.txt con la stringa "Questo e' il contenuto del file." e salvalo in una directory
        leggiTestoDaFile() nella variabile ereditata testo leggi file.
        getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
    
"""
    
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
        #oggetto
        self.__email = Email (self.__mittente, self.__destinatario, self.__titolo, self.__testo)

        self.__file_path = 'file_generato/file.txt'

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
        expected: str = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.__testo}"
        returned: str = self.__email.f_get_email()
        
        self.assertEqual (returned, expected, "ERR F GET EMAIL - mancata corrispondenza")

    def test_f_set_to_file(self):
        self.__email.f_set_to_file()
        
        with open(self.__file_path, 'r') as file:
            returned = file.read() 
        
        expected = f"Da: {self.__mittente}, A: {self.__destinatario} \nTitolo: {self.__titolo} \nMessaggio: {self.__testo}"
        
        self.assertEqual (returned, expected, "ERR F GET TO FILE - file di ritorno non corrispondente")

class TestFile (unittest.TestCase):
#SETUP
    def setUp (self):
        #parametri
        self.__testo:str = "Mi è piaciuta l'esperienza di orienteering avuta insieme"
        self.__percorso_file: str = 'file_generato/file.txt'
        #oggetto
        self.__file = File (self.__testo, self.__percorso_file)
        

    def test_init(self):        
        self.ret_testo: str = self.__file.f_get_testo()
        self.ret_percorso:str = self.__file.f_get_percorso()
        
        self.assertEqual (self.ret_testo, self.__testo, "ERR INIT - valori testo non corrispondenti")
        self.assertEqual (self.ret_percorso, self.__percorso_file, "ERR INIT - valori percorso non corrispondenti")
        
    def test_f_get_percorso(self):   
        self.assertEqual(self.ret_percorso,self.__percorso_file, "ERR F GET PERCORSO - non corrispondente")
        
    def test_f_create_file(self):
        self.__file.f_create_file()
        
        with open(self.__percorso_file, 'r')as file:
            self.contenuto = file.read()
            
        self.assertEqual(self.contenuto, self.__testo, "ERR F CREATE FILE - file non corrispondente")

    def test_f_leggi_testo_da_file (self):
        returned = self.__file.f_leggi_testo_da_file()
        
        self.assertEqual(returned, self.__testo, "ERR F LEGGI TESTO DA FILE - non cirrispondente")

    def test_f_get_test(self):
        returned = self.__file.f_get_testo()
        
        self.assertEqual(returned, f"{self.__percorso_file}, {self.__testo}" )

if __name__ == "__main__":
    unittest.main()
    

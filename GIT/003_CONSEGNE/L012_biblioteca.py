import unittest 
from unittest import TestCase


class User():
#INIT
    def __init__ (self, id: int, name: str, surname:str ):
        pass

class Book():
#INIT
    def __init__ (self, title : str, author : str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre
        self.loan: bool = True
    
class Librarian():
#INIT
    def _init__ (self, id: int):
        self.id = id

class Library():
#INIT
    def __init__ (self):
        self.catalog: dict [str, Book] = {}   
        self.rent: dict [str, Book] = {}
#BODY       
    def f_add_book (self, book : Book): 
        self.catalog[book.title] = book
        return (f"il libro {book.title} è stato aggiunto al catalogo")
    
    def f_rent_book (self, book: Book):
        self.rent[book.title] = self.catalog.pop(book.title)
        self.loan: bool = False
    
    def f_return (self, book:Book):
        self.catalog [book.title] = self.rent.pop(book.title)
        self.loan: bool = True
        
    def f_print_catalog (self):
        if not self.catalog:                                # Se il catalogo è vuoto
            return (f"Nessun libro disponibile nel catalogo.")
        else:
            return (f"i libri disponibili sono: {self.catalog.keys()}")

    
class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Book1", "Author1", "Genre1")
        self.book2 = Book("Book2", "Author2", "Genre2")
        self.book3 = Book("Book3", "Author3", "Genre3")
        self.user = User(1, "John", "Doe")

    def test_add_book(self):
        self.library.f_add_book(self.book1)
        self.assertIn("Book1", self.library.catalog.keys())
        self.assertEqual(len(self.library.catalog), 1)

        self.library.f_add_book(self.book2)
        self.assertIn("Book2", self.library.catalog.keys())
        self.assertEqual(len(self.library.catalog), 2)

    def test_rent_book(self):
        self.library.f_add_book(self.book1)
        self.library.f_add_book(self.book2)
        
        self.library.f_rent_book(self.book1)
        self.assertNotIn("Book1", self.library.catalog.keys())
        self.assertIn("Book1", self.library.rent.keys())
        self.assertFalse(self.book1.loan)

    def test_return_book(self):
        self.library.f_add_book(self.book1)
        self.library.f_add_book(self.book2)
        self.library.f_rent_book(self.book1)

        self.library.f_return(self.book1)
        self.assertIn("Book1", self.library.catalog.keys())
        self.assertNotIn("Book1", self.library.rent.keys())
        self.assertTrue(self.book1.loan)

    def test_print_catalog_empty(self):
        result = self.library.f_print_catalog()
        self.assertEqual(result, "Nessun libro disponibile nel catalogo.")

    def test_print_catalog_nonempty(self):
        self.library.f_add_book(self.book1)
        self.library.f_add_book(self.book2)
        self.library.f_add_book(self.book3)
        
        result = self.library.f_print_catalog()
        self.assertIn("Book1", result)
        self.assertIn("Book2", result)
        self.assertIn("Book3", result)

if __name__ == "__main__":
    unittest.main()
    
    
"""

    utenti
    - aggiungere libri al catalogo, 
    - prestare libri
    - restituire libri 
    - visualizzare quali libri sono disponibili in un dato momento.
 

    Libro: 
    OK - Rappresenta un libro con titolo, autore, stato del prestito. 
    OK - Il libro deve essere inizialmente disponibile (non prestato).

    Biblioteca:
    OK - aggiungi_libro(libro): 
    OK Aggiunge un nuovo libro al catalogo della biblioteca. 
    OK Restituisce un messaggio di conferma.

    OK - presta_libro(titolo): 
    Cerca un libro per titolo e, se disponibile e non già prestato, 
    lo segna come non disponibile. 
    Restituisce un messaggio di stato.

    OK - restituisci_libro(titolo): 
    Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
    Restituisce un messaggio di stato.

    OK - mostra_libri_disponibili(): 
    Restituisce una lista dei titoli dei libri attualmente disponibili. 
    Se non ci sono libri disponibili, restituisce un messaggio di errore.

    Test Cases:
    - Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
    - Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
    - L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
    - un utente può visualizzare quali libri sono disponibili per il prestito.
    
    
"""   
"""
2. Book Collection:

    function add_book( author's name and a variable number of book titles authored by them) . 
        return a dictionary where the author's name is the key and the value is a list of their books. 
        Demonstrate this function by adding books for different authors.
        Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

    function delete_book( dictionary and the name of the author from whom to remove all details). 
        return an updated dictionary.
        Example: delete_book(dictionary, “Mark Twain”)

"""
import unittest

class Book_collection():
#INIT
    def __init__(self):
        self.__books_dict: dict [str, list[str]] = {}
#BODY
    def f_add_book(self, autore:str, libro:str):
        if autore in self.__books_dict:            
            self.__books_dict [autore].append (libro)
        else:
            self.__books_dict [autore] = [libro]
        
    def f_getter_book_dict(self):
        return self.__books_dict
    
    def f_delete_books(self, autore:str):
        if autore in self.__books_dict:
            del self.__books_dict[autore]
        
            

#TEST
class TestBook_collection(unittest.TestCase):
#SETUP
    def setUp(self):
        self.__name = "Coelho"
        self.__books = ["L'Alchimista", "Brida", "Veronika decide di morire", "Onze Minutos"]
        self.__name2 = "Gabriel García Márquez"
        self.__books2 = ["Cent'anni di solitudine", "L'amore ai tempi del colera", "Autunno del patriarca", "Cronaca di una morte annunciata"]
        self.__librocoelho = "il pellegrinaggio"
        
        self.__oggetto = Book_collection ()
        
        for book in self.__books:
            self.__oggetto.f_add_book(self.__name, book)
        for book in self.__books:
            self.__oggetto.f_add_book(self.__name2, book)
        
    def test_f_add_books(self):
        self.__oggetto.f_add_book(self.__name, self.__librocoelho)
        books_dict = self.__oggetto.f_getter_book_dict()
        self.__books += [self.__librocoelho]
        
        self.assertEqual(books_dict[self.__name], self.__books, "ERR. F ADD BOOK - valori non corrispondenti")
        
    def test_f_delete_books(self):
        self.__oggetto.f_delete_books(self.__name)
        books_dict = self.__oggetto.f_getter_book_dict()
        
        self.assertNotIn(self.__name, books_dict, "ERR F REMOVE BOOKS - l'autore non è stato rimosso correttamente")
        
if __name__ == "__main__":
    unittest.main()       


    
    
    
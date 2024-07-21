"""
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

Classe Book:
    Attributi:
    book_id: str - Identificatore di un libro.
    title: str - titolo del libro.
    author: str - autore del libro
    is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
    Metodi:
    borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
    return_book()- Contrassegna il libro come restituito.

Classe Member:
    Attributi:
    member_id: str - identificativo del membro.
    name: str - il nome del membro.
    borrowed_books: list[Book] - lista dei libri presi in prestito.
    Metodi:
    borrow_book(book): 
        aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
    return_book(book): 
        rimuove il libro dalla lista borrowed_books.
        
Classe Library:
    Attributi:
    books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
    members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
    Methodi:
    add_book(book_id: str, title: str, author: str): 
        Aggiunge un nuovo libro nella biblioteca.
    register_member(member_id:str, name: str):
        Iscrive un nuovo membro nella biblioteca.
    borrow_book(member_id: str, book_id: str): 
        Permette al membro di prendere in prestito il libro.
    return_book(member_id: str, book_id: str): 
        Permette al membro di restituire il libro.
    get_borrowed_books(member_id): list[Book] -
        restituisce la lista dei libri presi in prestito dal membro.
"""
import unittest

class Book():
    
#INIT
    def __init__(self,book_id:str, title:str, author:str,is_borrowed:bool = False):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__is_borrowed = is_borrowed
        
#BODY
    def borrow(self):
        if self.__is_borrowed == False:
            self.__is_borrowed = True
            
    def return_book(self):
        self.__is_borrowed = False
        
    def is_borrowed(self):
        return self.__is_borrowed
        
class Member():
#INIT
    def __init__(self, member_id:str, name: str, borrowed_books:list[Book] = None):
        self.__member_id: str = member_id
        self.__name:str = name
        self.__borrowed_books:list [Book] = borrowed_books 

#BODY
    def borrow_book(self, book:Book):
        if book.is_borrowed() == False:
            book.borrow()
            self.__borrowed_books.append (book)
            
    def return_book(self, book:Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
    
    def get_borrowed_books(self):
        return self.__borrowed_books
        
class Library():
#INIT
    def __init__(self):
        self.books: dict[str,Book] = {}
        self.members: dict[str,Member] = {}
#BODY
    def add_book(self,book_id: str, title: str, author: str):
        if book_id not in self.books:
            self.books[book_id] = Book (book_id, title, author)
        
    def register_member(self, member_id:str,  name:str):
        if member_id not in self.members:
            self.members[member_id] = Member (member_id, name, [])

    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            self.members[member_id].borrow_book(self.books[book_id])
    
    def return_book(self, member_id: str, book_id: str):
        if self.books[book_id] in self.members[member_id].get_borrowed_books():
            return self.members[member_id].return_book(self.books[book_id])
        else:
            return False
        
    def get_borrowed_books(self, member_id:str):
        if member_id in self.members:
            return self.members[member_id].get_borrowed_books()
        else:
            return None
        
    def get_all_books(self):
        lista_titoli: list[str] = []
        for key in self.books.keys():
            lista_titoli.append(key)
            
        return lista_titoli
        
            

#TEST
class TestBook(unittest.TestCase):
#SETUP
    def setUp(self):
        self.libro1 = Book ("B001", "The Great Gatsby", "F. Scott Fitzgerald", False)
        self.libro2 = Book ("B002", "1984", "George Orwell", False)
        self.libro3 = Book ("B003", "To Kill a Mockingbird", "Harper Lee", False)

    def test_borrow(self):
        returned = self.libro1.borrow()
        expected = True
        
        self.assertEqual(returned, expected, "ERR F BORROW - valore non corrispondente")

    def test_is_borrowed(self):
        self.assertEqual(self.libro2.is_borrowed, False, "ERR F IS BORROWED")

    def test_return_book(self):
        self.libro1.borrow()
        self.libro1.return_book()
        self.assertFalse(self.libro1.is_borrowed(), "ERR F RETURN BOOK - il libro non risulta prenotato")

class TestMembers(unittest.TestCase):
#SETUP
    def setUp(self):
        self.membro1 = Member ("M001", "Alice")
        self.membro2 = Member ("M002", "Bob")
        self.membro3 = Member ("M003", "Charlie")
        self.libro3 = Book ("B003", "To Kill a Mockingbird", "Harper Lee", False)

    def test_borrow_book(self):      
        self.membro1.borrow_book(self.libro3)
        self.assertIn(self.membro1.borrow_book(self.libro3), "ERR F BORROW BOOK - il libro non da corrispondenza")

    def test_return_book(self):
        self.membro1.borrow_book(self.libro3)
        self.membro1.return_book(self.libro3)
        self.assertNotIn(self.membro1.borrow_book(self.libro3), "ERR F RETURN BOOK - il libro non da corrispondenza")  

class TestLibrary(unittest.TestCase):
#SETUP
    def setUp(self):
        # Creazione di un'istanza della biblioteca
        self.library = Library()
    
        
        # Registrazione di membri alla biblioteca
        self.library.register_member("M001", "Alice")
        self.library.register_member("M002", "Bob")
        self.library.register_member("M003", "Charlie")

        # Recupero degli oggetti libro e membro per i test
        self.book1 = self.library.books["B001"]
        self.book2 = self.library.books["B002"]
        self.member1 = self.library.members["M001"]
        self.member2 = self.library.members["M002"]
        
    def test_add_book(self):
        # Aggiunta di libri alla biblioteca
        self.library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
        self.library.add_book("B002", "1984", "George Orwell")
        self.library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")
        
        self.assertIn("The Great Gatsby", self.library.get_all_books(), "ERR")
        self.assertIn("1984", self.library.get_all_books(), "ERR")
        self.assertIn("To Kill a Mockingbird", self.library.get_all_books(), "ERR")

"""
library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))
print(library.get_borrowed_books("M002"))

"""
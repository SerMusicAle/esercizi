"""
BOOK: (book_id: str, title: str, author: str, is_borrowed: boolean)

    borrow()
        Contrassegna il libro come preso in prestito se non è già preso in prestito.

    return_book()- 
        Contrassegna il libro come restituito.
MEMBER:(member_id: str, name: str, borrowed_books: list[Book])

    borrow_book(book):
        aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.

    return_book(book): 
        rimuove il libro dalla lista borrowed_books.

LIBRARY: (books: dict[str, Book] chiave l'id del libro e valore Book, members: dict[str, Member] chiave l'id del membro e valore  Membro)

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

For example:

    Test	Result
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

    print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
    print(library.get_borrowed_books("M002"))  # Expected output: ['1984']
    ['The Great Gatsby']
    ['1984']
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
from typing import Any
class Book():
#INIT
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool = False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
#BODY
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
        else:
            raise ValueError("Book is already borrowed")
        
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError(f"Il libro '{self.title}' non è attualmente in prestito.")
        
class Member():
#INIT
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []
#BODY        
    def borrow_book(self, book: Book) -> None:
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print (f"Book is already borrowed")
            
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            raise ValueError("Book not borrowed by this member")
               
class Library:
#INIT
    def __init__ (self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        
    def add_book(self, book_id: str, title: str, author: str) -> None:
        if book_id not in self.books:
            self.books[book_id] = Book (book_id, title, author)
        else:
            raise ValueError(f"Il libro con ID '{book_id}' esiste già nella biblioteca.")
            
    def register_member(self, member_id:str, name: str):
        if member_id not in self.members:
            self.members[member_id] = Member (member_id, name)
        else:
            raise ValueError(f"Il membro con ID '{member_id}' esiste già nella biblioteca.")
        
    def borrow_book(self, member_id: str, book_id: str): 
        if member_id in self.members:
            if book_id in self.books:
                self.members[member_id].borrow_book(self.books[book_id])
            else:
                raise ValueError (f"Book not found")
        else:
            raise ValueError("Member not found")
        
    def return_book(self, member_id: str, book_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        if book_id not in self.books:
            raise ValueError(f"Book with ID '{book_id}' not found")
        
        self.members[member_id].return_book(self.books[book_id])
    
    def get_borrowed_books(self, member_id:str) -> list[str]:
        if member_id not in self.members:
            raise ValueError("Member not found")
        
        return [book.title for book in self.members[member_id].borrowed_books]
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
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Methodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.


"""

class Book:

    #INIT
    def __init__(self, book_id:str, title:str, author:str, is_borrowed:bool):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow():
        if Book.book in Library.books:
            is_borrowed = True
        
    def return_book():
        is_borrowed = False


class Member:

    #INIT
    def __init__(self, member_id:str, name:str, borrowed_books:list[Book]) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self, book):
        if Book.book in Library.books:
            self.borrowed_books.append(Book.book)
            Library.book.remove(Book.book)

    def return_book(self, book):
        self.borrowed_books.remove(Book.book)
        Library.book.append(Book.book)

class Library:

    #INIT
    def __init__(self, books:dict[str,Book], members:dict[str, Member]) -> None:
        self.books = books
        self.members = members
        
        #DEC
        self.books:list = []

    def add_book(self, book_id:str, title:str, author:str):
        if Book.book.title != Book[title] and Book.book.author != Book[author]:
            book = {book_id, title, author}
            Library.books.append(book)

    def register_member(self, member_id:str, name:str):
        if name not in Member.members.values():
            member = {member_id, name}
            Member.member.append (member)
    
    def borrow_book(self, member_id:str, book_id:str):
        if Book.book in Library.books:
            Library.book.remove(Book.book)

    def return_book(self, member_id:str, book_id:str):
        Member.borrowed_book.remove(Book.book)
        Library.books.append(Book.book)
    
    def get_borrowed_books(self, member_id):
        pass 


#TEST
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


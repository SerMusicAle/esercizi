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
class Book():
#INIT
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        #Contrassegna il libro come preso in prestito se non è già preso in prestito.
        self.is_borrowed = True
        
    def return_book(self): 
        #Contrassegna il libro come restituito.
        self.is_borrowed = False

class Member():
#INIT
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book] = []):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books

    def borrow_book(self, book:Book):
        #aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            

    def return_book(self, book:Book): 
        #rimuove il libro dalla lista borrowed_books.
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

class Library (): 
#INIT
    def __init__(self):
        #chiave l'id del libro e valore Book
        self.books: dict[str, Book] = {}
        #chiave l'id del membro e valore  Membro
        self.members: dict[str, Member] = {}
    
    def add_book(self, book_id: str, title: str, author: str): 
        #Aggiunge un nuovo libro nella biblioteca.
        if book_id not in self.books:
            self.books[book_id] = Book (book_id, title, author, is_borrowed=False)

    def register_member(self, member_id:str, name: str): 
        #Iscrive un nuovo membro nella biblioteca.
        if member_id not in self.members:
            self.members[member_id] = Member (member_id, name)
        
    def borrow_book(self, member_id: str, book_id: str): 
        #Permette al membro di prendere in prestito il libro.
        if book_id in self.books:
            #creo l'oggetto libro e lo verifico se disponibile
            book = self.books[book_id]
            if book.is_borrowed:
                return
                print (f"il libro è gia stato preso in prestito")
            #se disponibile prendo il membro e lo presto
            member = self.members[member_id]
            #prenbdo in prestio il libro
            member.borrow_book(book)
            #segno il libro come preso
            book.borrow()
            #elimino il libro dalla biblioteca
            del self.books[book_id]

    def return_book(self, member_id: str, book_id: str): 
        #Permette al membro di restituire il libro.
        member = self.members[member_id] 
        for book in member.borrowed_books:
            if book.book_id == book_id:
                book.return_book()  # Contrassegna il libro come restituito
                self.books[book_id] = book  # Aggiungi il libro alla biblioteca
                member.return_book(book)  # Rimuovi il libro dalla lista dei libri presi in prestito dal membro
                return

    def get_borrowed_books(self, member_id:str):  
        #restituisce la lista dei libri presi in prestito dal membro.
        libri:list[str] = []
        
        for book in self.members[member_id].borrowed_books:
            
            libri.append(book.title)
            
            
        return libri
        
    

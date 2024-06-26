class Book():
    
#INIT
    def __init__ (self, titolo:str, autore:str, isbn: str):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    
    #scompattiamo la stringa in ingresso
    @classmethod
    def from_string(cls, book_str):
        titolo, autore, isbn = book_str.split(', ')
        return cls(titolo, autore, isbn)
        
    def __str__ (self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"      
    
class Member ():

#INIT
    def __init__ (self, name:str, member_id:int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        #self.borrowed_books = borrowed_books if borrowed_books is not None else []
        
    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        self.borrowed_books.remove(book)

    def __str__ (self):
        borrowed_books_str: str = ', '.join([str(book.title) for book in self.borrowed_books])
        return f"Nome: {self.name}, Id: {self.member_id}, lista in possesso: [{self.borrowed_books}]" 

    @classmethod 
    def from_string(cls, member_str):
        name, member_id = member_str.split (', ')
        return cls(name, member_id)
    
class Library(): 
    
    quantity_books: int = 0 
#INIT
    def __init__ (self):
        self.books = []
        self.members = []

#BODY
    def add_book(self, book: Book):
        self.books.append(book)
        Library.quantity_books += 1
        
    def remove_book(self, book: Book):
        if book in self.books:    
            self.books.remove(book)
            Library.quantity_books -=1
        else:
            print ("il libro non è disponibile")

    def register_member (self, member: Member):
        self.members.append (member)
    
    def remove_member (self, member: Member):
        if member in self.members:
            self.members.remove (member)
        else:
            print (f"il membro non esiste")
        
    def borrow_book(self, book: Book, member: Member):
        if book in self.books and member in self.members:
            self.books.remove (book)
            member.borrow_book (book)
        else:
            print ("o il libro non è disponibile o non registrato")
            
    def __str__(self):
        books_str: str = ', '.join ([str(book.titolo) for book in self.books])
        members_str: str = ', '.join ([str(member.name) for member in self.members])
        return f"Libri: [{books_str}], Membri: [{members_str}]"
        
    @classmethod
    def library_statistics(cls):
        print (f"totale libri: {cls.quantity_books}!")



#TEST
        
# Script per giocare con le classi
libro_str1 = "La Divina Commedia, D. Alighieri, 999000666"
libro_str2 = "Il Principe, N. Machiavelli, 123456789"
membro_str1 = "Giovanni Rossi, M001"
membro_str2 = "Maria Bianchi, M002"

divina_commedia = Book.from_string (libro_str1)
principe = Book.from_string (libro_str2)
giovanni = Member.from_string (membro_str1)
maria = Member.from_string (membro_str2)

library = Library()
library.add_book (divina_commedia)
library.add_book (principe)
library.register_member (giovanni)
library.register_member (maria)

print ("Stato della biblioteca prima del prestito:")
print (library)

library.borrow_book(divina_commedia, giovanni)

print("\nStato della biblioteca dopo il prestito:")
print(library)
Library.library_statistics()

"""

import unittest

class TestLibrarySystem(unittest.TestCase):

    def test_book_creation(self):
        book = Book("l'alchimista", "coelho", "9876578")
        self.assertEqual(book.titolo, "l'alchimista")
        self.assertEqual(book.autore, "coelho")
        self.assertEqual(book.isbn, "9876578")

    def test_book_from_string(self):
        book_str = "l'alchimista, coelho, 9876578"
        book = Book.from_string(book_str)
        self.assertEqual(book.titolo, "l'alchimista")
        self.assertEqual(book.autore, "coelho")
        self.assertEqual(book.isbn, "9876578")

    def test_member_creation(self):
        member = Member("Alice", 1)
        self.assertEqual(member.name, "Alice")
        self.assertEqual(member.member_id, 1)
        self.assertEqual(member.borrowed_books, [])

    def test_member_from_string(self):
        member_str = "Alice, 1"
        member = Member.from_string(member_str)
        self.assertEqual(member.name, "Alice")
        self.assertEqual(member.member_id, 1)

    def test_library_operations(self):
        library = Library()
        book1 = Book("Book1", "Author1", "ISBN1")
        book2 = Book("Book2", "Author2", "ISBN2")
        member = Member("Alice", 1)

        library.add_book(book1)
        self.assertIn(book1, library.books)
        self.assertEqual(Library.quantity_books, 1)

        library.add_book(book2)
        self.assertIn(book2, library.books)
        self.assertEqual(Library.quantity_books, 2)

        library.register_member(member)
        self.assertIn(member, library.members)

        library.borrow_book(book1, member)
        self.assertNotIn(book1, library.books)
        self.assertIn(book1, member.borrowed_books)

        library.remove_book(book2)
        self.assertNotIn(book2, library.books)
        self.assertEqual(Library.quantity_books, 0)

        library.remove_member(member)
        self.assertNotIn(member, library.members)

if __name__ == '__main__':
    unittest.main()




    Esercizio 3: Sistema di Gestione della Biblioteca
    OK Crea una classe Libro contenente i seguenti attributi: 
    titolo, autore, isbn. La classe Libro deve contenere i seguenti metodi:

    OK Il metodo __str__ per restituire una rappresentazione in formato stringa del libro.

    OK Il metodo di classe from_string(cls, book_str) per creare un'istanza di Libro 
    a partire da una stringa nel formato "titolo, autore, isbn". 
    Significa che devi usare il riferimento della classe cls per creare un nuovo oggetto 
    della classe Libro utilizzando una stringa.

    Esempio:

    python
    Copia codice
    book = "La Divina Commedia, D. Alighieri, 999000666"
    divina_commedia = Libro.from_string(book)
    Qui, divina_commedia deve contenere un'istanza della classe Libro con:

    titolo = "La Divina Commedia"
    autore = "D. Alighieri"
    isbn = "999000666"
    
    Crea una classe Membro con i seguenti attributi: nome, id_membro, libri_prestati. 
    La classe Membro deve contenere i seguenti metodi:

    Il metodo presta_libro(libro) 
    per aggiungere un libro alla lista dei libri prestati.

    Il metodo restituisci_libro(libro) 
    per rimuovere un libro dalla lista dei libri prestati.
    
    Il metodo __str__ 
    per restituire una rappresentazione in formato stringa del membro.

    Il metodo di classe from_string(cls, member_str) 
    per creare un'istanza di Membro a partire da una stringa nel formato "nome, id_membro".

    Crea una classe Biblioteca con i seguenti attributi: 
    libri, membri, totale_libri (attributo di classe per tenere traccia del numero totale di libri). 
   
       La classe Biblioteca deve contenere i seguenti metodi:

    Il metodo aggiungi_libro(libro) 
    per aggiungere un libro alla biblioteca e incrementare totale_libri.

    Il metodo rimuovi_libro(libro) 
    per rimuovere un libro dalla biblioteca e decrementare totale_libri.

    Il metodo registra_membro(membro) 
    per aggiungere un membro alla biblioteca.

    Il metodo presta_libro(libro, membro) 
    per prestare un libro a un membro. 
    Deve controllare se il libro è disponibile e se il membro è registrato.
    
    Il metodo __str__ per restituire una rappresentazione in formato stringa 
    della biblioteca con l'elenco dei libri e dei membri.

    Il metodo di classe statistiche_biblioteca(cls) 
    per stampare il numero totale di libri.

    Crea uno script e gioca un po' con le classi:

    Crea istanze di libri e membri utilizzando i metodi di classe.
    Registra membri e aggiungi libri alla biblioteca.
    Presta libri ai membri e mostra lo stato della biblioteca prima e dopo il prestito.  
    
"""
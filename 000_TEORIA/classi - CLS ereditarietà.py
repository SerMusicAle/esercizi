
class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    @classmethod
    def from_stringa(cls, libro_str):
        titolo, autore, isbn = libro_str.split(', ')
        return cls(titolo, autore, isbn)

class Ebook(Libro):
    def __init__(self, titolo, autore, isbn, formato):
        super().__init__(titolo, autore, isbn)
        self.formato = formato

ebook_str = "Python 101, M. Mustermann, 123456789"

#Ebook usa from_stringa di Libro
ebook = Ebook.from_stringa(ebook_str)
print(ebook)



class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, ISBN: {self.isbn}"
  
    @classmethod
    def from_stringa(cls, libro_str):
        #assegnamo i valori dalla stringa
        titolo, autore, isbn = libro_str.split(', ')
#CLS crea l'istanza di init
        return cls(titolo, autore, isbn)

#CLS crea un oggetto da dizionario
    @classmethod
    def from_dict(cls, libro_dict):
        return cls(libro_dict['titolo'], libro_dict['autore'], libro_dict['isbn'])

#CLS modifica attributi classe
class Biblioteca:
    totale_libri = 0

    def __init__(self):
        self.libri = []

    @classmethod
    def incrementa_totale_libri(cls):
        cls.totale_libri += 1

#SELF richiama metodi di classe
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        Biblioteca.incrementa_totale_libri()


libro_dict = {
    'titolo': 'La Divina Commedia',
    'autore': 'D. Alighieri',
    'isbn': '999000666'
}
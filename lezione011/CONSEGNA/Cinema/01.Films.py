class Film:
    
    def __init__(self, titolo: str, durata: int, genere: str):
        self.titolo: str = titolo
        self.durata: int = durata
        self.genere: str = genere

class Films:

    def __init__(self):
        self.elenco_films: dict[str, Film] = {}

    def f_add_film(self, film: Film) -> None:
        self.elenco_films[film.titolo] = film #chiave stringa e valore oggetto

class Stampa_step:
    
    def __init__(self, elenco_films: dict[str, Film]):
        self.elenco_films = elenco_films
        self.sorted_films: list[Film] = list (elenco_films.values())
        
    def f_stampa(self, sorted_films: list[Film]) -> None:
        sorted_films = sorted (self.elenco_films.values(), key=  lambda film: film.genere)
        
        for film in sorted_films:
            print(f"Genere: {film.genere} | Titolo: {film.titolo}, Durata: {film.durata} minuti")



#Crazione oggetti
films = Films()

# Aggiunta dei film
film1 = Film("Spiderman", 134, "Fantasy")
film2 = Film("Trolls", 94, "Animazione")
film3 = Film("Capitan America", 126, "Fantasy")

#funzioni elenco
films.f_add_film(film1)
films.f_add_film(film2)
films.f_add_film(film3)

#crea oggetto stampa
stampa = Stampa_step(films.elenco_films)

#metodo stampa dell'oggetto stampa
stampa.f_stampa([])
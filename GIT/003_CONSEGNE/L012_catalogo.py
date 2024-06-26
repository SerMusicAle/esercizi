class Catalog:
#INIT
    def __init__ (self):
        self.directors: dict = {}
        
    def f_add_movie(self, director_name, movies):
        #se è un nuovo regista
        if director_name not in self.directors:
            self.directors [director_name] = movies
        else:
            #aggiorna lista
            self.directors[director_name].extend(movies)
    
    def f_remove_movie(self, director_name, movie_name):
        if director_name in self.director[]:
            self.directors[director_name].remove(movie_name)
            if len(self.directors[director_name]) == 0:
                del self.directors[director_name]
    
    def f_list_directors(self):
        return list(self.directors.keys())
    
    def f_get_movies_by_director(self, director_name):
        if director_name in self.directors:
            return self.directors[director_name]  
        else:
            return
       
    def f_search_movies_by_title(self, title):
    results = []
    title_lower = title.lower()  # Converti una sola volta il titolo in minuscolo
    for director, movies in self.directors.items():
        matching_movies = [movie for movie in movies if title_lower in movie.lower()]
        if matching_movies:  # Aggiungi alla lista solo se ci sono film corrispondenti
            results.append((director, matching_movies))
    return results

    """
    SPIEGAZIONE DEASSEMBLATA DELLA COMPRHENSION
    
    def f_search_movies_by_title(self, title):
        results = {}
        title_lower = title.lower()  # Converti una sola volta il titolo in minuscolo
        
        for director, movies in self.directors.items():
            matching_movies = []
            for movie in movies:
                if title_lower in movie.lower():
                    matching_movies.append(movie)
                    
            if matching_movies:  # Aggiungi alla lista solo se ci sono film corrispondenti
                results[director] = matching_movies
        
        if results:
            return results
        else:
            return "non ci sono film corrispondenti a quella parola"
    """
catalogo = Catalog()

catalogo.f_add_movie("Steven Spielberg", ["Jurassic Park", "Schindler's List", "E.T. the Extra-Terrestrial"])
catalogo.f_add_movie("Christopher Nolan", ["Inception", "Interstellar", "Dunkirk", "The Dark Knight"])
catalogo.f_add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill: Vol. 1", "Django Unchained", "Once Upon a Time in Hollywood"])
catalogo.f_add_movie("Martin Scorsese", ["Taxi Driver", "Goodfellas", "The Wolf of Wall Street", "Raging Bull"])
catalogo.f_add_movie("James Cameron", ["Avatar", "Titanic", "Terminator 2: Judgment Day"])

# Esempi di richiami alle funzioni
print("Elenco dei registi nel catalogo:", catalogo.f_list_directors())

print("Film diretti da Christopher Nolan:", catalogo.f_get_movies_by_director("Christopher Nolan"))

catalogo.f_remove_movie("James Cameron", "Titanic")
print("Film diretti da James Cameron dopo la rimozione di 'Titanic':", catalogo.f_get_movies_by_director("James Cameron"))

print("Ricerca di film con 'Inception' nel titolo:", catalogo.f_search_movies_by_title("Inception"))

print("Ricerca di film con 'the' nel titolo:", catalogo.f_search_movies_by_title("the"))




"""
Catalogo Film 
- aggiungere, rimuovere e cercare film di un particolare regista. 
- visualizzare tutti i registi e i loro film.

MovieCatalog:
    - add_movie(director_name, movies): 
    Aggiunge uno o più film a un regista specifico nel catalogo. 
    Se il regista non esiste, viene creato un nuovo record. 
    Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): 
    Rimuove un film specifico dall'elenco dei film di un regista. 
    Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): 
    Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): 
    Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): 
    Trova tutti i film che contengono una certa parola nel titolo. 
    Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata 
    o un messaggio di errore se nessun film contiene la parola cercata nel titolo.
    










class Director:
#INIT
    def __init__ (self, name: Name, surname: Surname):
        self.name = name
        self.surname = surname
    
    def f_add_directors (self, director:Director)
        list_directors: list = 

class Movie:
#INIT
    def __init__ (self, title : str, durata : str, regista : str):
        self.title = title
        self.durata = durata
        self.regista = regista
        

class Catalog:
#INIT
    def __init__ (self, movie:Movie, director: Director):
        self.movie = movie
        self.movies:dict [str, Movie] = {}
        self.directors: dict [str, Movie] = {}
        
    def f_add_movie (self, movie : Movie):
        self.movies[movie.title] = movie
        
    def f_add_director (self, director : Director):
        self.directors [director.name] = director
        
"""
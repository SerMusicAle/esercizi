from typing import Any

class Gestore:
#INIT
    def __init__ (self, nome:str, cognome:str):
        self.nome = nome
        self.cognome = cognome

class Utente:   
#INIT
    def __init__ (self, nome:str, cognome:str):
        self.nome = nome
        self.cognome = cognome
        self.prenotazioni : dict[Any,Any]= {}
        
class Film:
#INIT    
    def __init__(self, titolo: str, durata: int, genere: str):
        self.titolo: str = titolo
        self.durata: int = durata
        self.genere: str = genere

class Films:
#INIT
    def __init__(self):
        self.elenco_films: dict[str, Film] = {}
#BODY
    def f_add_film(self, film: Film) -> None:
        self.elenco_films[film.titolo] = film #chiave stringa e valore oggetto
        
class Sala:   
#INIT
    def __init__ (self, id: int, nome: str, posti_totali: int): #definisco gli oggetti di tipo Sala
        self.id: int = id
        self.nome: str = nome
        self.posti_totali: int = posti_totali  
        self.posti_disponibili: int = posti_totali        

class Sale:
#INIT
    #l'oggetto sale ha 
    def __init__ (self):       
        self.elenco_sale: dict [int, Sala]= {}    #elenco vuoto dove memorizzare le sale
        self.proiezioni = Proiezioni ()
#BODY        
    def add_sala (self, sala: Sala):
        self.elenco_sale [sala.id] = sala #all'elenco self.sale aggiunge ogni sala impostando id come chiave
    
class Proiezione:
#INIT    
    def __init__ (self, sala:Sala, orario: str, film:Film):
        self.sala = sala
        self.orario : str = orario  
        self.film = film  

class Proiezioni:
#INIT    
    def __init__ (self):
        self.elenco_proiezioni : dict[tuple[str, int], Proiezione] = {} #proiezione: posti
#BODY    
    def add_proiezione(self, proiezione:Proiezione):
        chiave = (proiezione.orario, proiezione.sala.id)
        self.elenco_proiezioni [chiave] = proiezione
    
    def disponibilità (self, sale: Sale):
        for (sala, self.orario), proiezione in self.elenco_proiezioni.items(): 
            sala = sale.elenco_sale[proiezione.sala.id]
            proiezione.sala.posti_disponibili = sala.posti_totali

class Cinema:
#INIT
    def __init__(self, nome: str, sale: Sale):
        self.nome = nome
        self.sale = sale
        self.proiezioni_elenco = sale.proiezioni.elenco_proiezioni
        self.posti_prenotati = 0
#BODY
    def prenota_film(self, utente: Utente, sala_id: int, film_titolo: str, orario: str, posti_richiesti: int):
        chiave_proiezione = (orario, sala_id)
        if chiave_proiezione in self.proiezioni_elenco:
            proiezione = self.proiezioni_elenco[chiave_proiezione]
            if proiezione.film.titolo == film_titolo:
                if posti_richiesti <= proiezione.sala.posti_disponibili:
                    proiezione.sala.posti_disponibili -= posti_richiesti
                    chiave_prenotazione = (orario, sala_id, film_titolo)
                    utente.prenotazioni[chiave_prenotazione] = posti_richiesti
                    self.posti_prenotati += posti_richiesti
                    print(f"Prenotazione effettuata con successo")
                else:
                    print(f"Posti non disponibili per il film {film_titolo} nella sala {sala_id} all'orario {orario}")
            else:
                print(f"Film {film_titolo} non trovato nella sala {sala_id} all'orario {orario}")
        else:
            print(f"Proiezione non trovata per il film {film_titolo} nella sala {sala_id} all'orario {orario}")

class Stampa_step:
#INIT
    def __init__(self, sale: Sale, utente: Utente):
        self.elenco_sale = sale.elenco_sale
        self.elenco_proiezioni = sale.proiezioni.elenco_proiezioni
        self.utente = utente
#BODY
    def f_stampa(self) -> None:
        print(f"Elenco sale:\n")
        for sala in self.elenco_sale.values():
            print(f"Sala n° {sala.id} - {sala.nome}: Posti_totali: {sala.posti_totali}")

        print(f"\nElenco proiezioni:\n")
        for (orario, sala_id), proiezione in self.elenco_proiezioni.items():
            film = proiezione.film
            sala = proiezione.sala
            disponibilità = proiezione.sala.posti_disponibili
            print(f"Proiezione del film '{film.titolo}' nella Sala '{sala.nome}' alle ore {orario}: Disponibili {disponibilità} posti")

        print("\nStampa delle prenotazioni:")
        if self.utente.prenotazioni:
            for chiave, posti in self.utente.prenotazioni.items():
                orario, sala_id, film_titolo = chiave
                print(f"Film: {film_titolo}, Sala: {sala_id}, Orario: {orario}, Posti prenotati: {posti}")
        else:
            print("Nessuna prenotazione effettuata.")

# INPUT

# FILMS
films = Films()

film1 = Film("Spiderman", 134, "Fantasy")
film2 = Film("Trolls", 94, "Animazione")
film3 = Film("Capitan America", 126, "Fantasy")

films.f_add_film(film1)
films.f_add_film(film2)
films.f_add_film(film3)

# SALE
sale = Sale()

sala1 = Sala(1, "Sala Mastroianni", 200)
sala2 = Sala(2, "Sala Manfredi", 210)
sala3 = Sala(3, "Sala Sordi", 230)

sale.add_sala(sala1)
sale.add_sala(sala2)
sale.add_sala(sala3)

# PROIEZIONI
proiezioni = sale.proiezioni

proiezione1 = Proiezione(sala1, "14:00", film1)
proiezione2 = Proiezione(sala2, "16:00", film2)
proiezione3 = Proiezione(sala3, "18:00", film3)

proiezioni.add_proiezione(proiezione1)
proiezioni.add_proiezione(proiezione2)
proiezioni.add_proiezione(proiezione3)

proiezioni.disponibilità(sale)

# CINEMA
cinema = Cinema("Cinema ABC", sale)

# UTENTE
utente = Utente("Mario", "Rossi")

# PRENOTAZIONI
cinema.prenota_film(utente, 1, "Spiderman", "14:00", 2)
cinema.prenota_film(utente, 2, "Trolls", "16:00", 3)
cinema.prenota_film(utente, 3, "Capitan America", "18:00", 4)

# STAMPA
stampa = Stampa_step(sale, utente)
stampa.f_stampa()
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
        self.prenotazioni = {}

class Film:
    
#INIT
    def __init__ (self, titolo: str, durata: int): #definisce gli oggetti di tipo film
        self.titolo = titolo
        self.durata = durata



#Modo 1
class Films:

#INIT
    def __init__(self): #definisce l'oggetto dizionario film vuoto
        self.films: dict [str, Film] = {} #dall'esterno viene implementata
#BODY   
    def add_film (self, film: Film):
        self.films [film.titolo] = film #a lista self.films si aggiungono oggetti film precedenti 



class Sala:

    def __init__ (self, id: int, nome: str, posti_totali: int): #definisco gli oggetti di tipo Sala
        self.id = id
        self.nome = nome
        self.posti_totali = posti_totali


class Sale:

#INIT
    #l'oggetto sale ha 
    def __init__ (self):       
        self.sale: dict [int, Sala]= {}    #elenco vuoto dove memorizzare le sale
        self.proiezioni_elenco: dict [tuple[int,str,str], dict[str, int|str|Film]] = {} #elenco vuoto dove memorizzare le proiezioni

    def add_sale (self, sala: Sala):
        self.sale [sala.id] = sala #all'elenco self.sale aggiunge ogni sala impostando id come chiave

    def proiezioni (self, film : Film, sala: Sala, orario : str, posti_prenotati : int, posti_disponibili : int):            
        
        #creo una chiave unica di lettura(input per id) composta id-orario(localizzazione)
        self.proiezioni_elenco [(sala.id, orario, film.titolo)] = {  # type: ignore
            "sala": sala,
            "orario": orario,
            "film": film,       #carico l'intero oggetto film
            "posti disponibili": posti_disponibili,
            "posti prenotati": posti_prenotati,
        }
    def disponibilità (self):
        for _, proiezione in self.proiezioni_elenco.items(): 
            print (f"Per la proiezione del film {proiezione ['film'].titolo}, alle ore {proiezione['orario']}, in sala {proiezione['sala'].nome} restano {proiezione['posti_disponibili']} posti disponibili")

class Cinema:

    def __init__ (self, nome:str, sale: Sale): 
        
        self.nome = nome
        self.proiezioni_elenco = {}
        self.posti_prenotati = 0

    def programmazione (self):
        
        programmazione_elenco = "Le proiezioni in questo cinema sono:\n"
        for _, proiezione in self.proiezioni_elenco.items():
            programmazione_elenco += (f"Sala: {proiezione['sala'].nome} - ore: {proiezione['orario']} - {proiezione['film'].titolo}. Sono rimasti {proiezione['posti_disponibili']} posti disponibili \n")

        return programmazione_elenco

    def prenota_film (self, utente:Utente, sala_id: int, film_titolo: str, orario: str, posti_richiesti: int):

        prenotazione = self.proiezioni_elenco[(sala_id, orario, film_titolo)]

        if posti_richiesti <= prenotazione ['posti_disponibili']:
            prenotazione['posti_disponibili'] -= posti_richiesti
            prenotazione['posti_prenotati'] += posti_richiesti
            utente.prenotazioni[(sala_id, orario, film_titolo)] = posti_richiesti
            self.posti_prenotati += posti_richiesti 
            print (f"Prenotazione effettuata con successo")



"""
class Films:
#Modo 2
#INIT
    def __init__ (self): #definisce l'oggetto dizionario film vuoto
        self.films : dict [str,int] = {} #dall'esterno viene implementata  

#BODY
    def add_film (self, film: Film): #prende gli oggetti passati precedentemente all'oggetto films
        
        #aggiungo
        self.films.update({film.titolo: film.durata})
         #a lista self.films si aggiungono i singoli elementi degli oggetti film precedenti 
class Sala:

    def __init__ (self, id: int, nome: str, posti_totali: int): #definisco gli oggetti di tipo Sala
        self.id = id
        self.nome = nome
        self.posti_totali = posti_totali
"""

#INPUT

#gestore
gestore001 = Gestore ("Andrea", "Attili")

#utenti
utente001 = Utente ("Alessandro", "Sereni")
utente002 = Utente ("Marco", "Marzelli")

#FILMS

films = Films() #creo oggetto elenco film

#elenco istanze film
film1 = Film ("Spiderman", 134)
film2 = Film ("Trolls", 94)
film3 = Film ("Capitan America", 126)

#implemento l'elenco films
films.add_film(film1)
films.add_film(film2)
films.add_film(film3)

#SALE

sale = Sale() #creo l'oggeto elenco sale

#elenco istanze sala
sala1 = Sala (1,"Sala Mastroianni", 200)
sala2 = Sala (2, "Sala Manfredi", 210)
sala3 = Sala (3, "Sala Sordi", 230)

#implemento l'elenco sale
sale.add_sale(sala1)
sale.add_sale(sala2)
sale.add_sale(sala3)

#CINEMA

cinema01 = Cinema ("Stardust", sale)

# Visualizzazione della disponibilità delle proiezioni
sale.disponibilità()

# implemento le proiezioni
sale.proiezioni(film1, sala1, "15:00", 30)
sale.proiezioni(film1, sala1, "18:00", 40)
sale.proiezioni(film2, sala2, "16:00", 20)
sale.proiezioni(film2, sala2, "20:00", 50)

#prenotazioni
cinema01.prenota_film(utente001, film1, sale.proiezioni_elenco[(1, "15:00")], 3)
cinema01.prenota_film(utente002, film2, sale.proiezioni_elenco[(2, "17:30")], 2)




"""
Sistema di Prenotazione Cinema

- diverse sale, ognuna con un diverso film in programmazione. 
- utenti 
    - possono vedere quali film sono disponibili 
    - prenotare posti per un determinato spettacolo.

 
Classi:
- Film: titolo e durata. 

- Sala: numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
    - metodo prenota_posti(num_posti): 
        - disponibilità. Restituisce un messaggio di conferma o di errore.
    - metodo posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
    - metodo aggiungi_sala(sala): 
        Aggiunge una nuova sala al cinema.
    - metodo prenota_film(titolo_film, num_posti): 
        Trova il film desiderato
        tenta di prenotare posti. 
        Restituisce un messaggio di stato.

Test case:
- Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
- Un cliente sceglie un film e prenota un certo numero di posti.
- Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""
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
        
    def add_sala (self, sala: Sala):
        self.elenco_sale [sala.id] = sala #all'elenco self.sale aggiunge ogni sala impostando id come chiave
    
class Proiezione:
    
    def __init__ (self, sala:Sala, orario: str, film:Film):
        self.sala = sala
        self.orario : str = orario  
        self.film = film  

class Proiezioni:
    
    def __init__ (self):
        self.elenco_proiezioni : dict[tuple[str, int], Proiezione] = {} #proiezione: posti
    
    def add_proiezione(self, proiezione:Proiezione):
        chiave = (proiezione.orario, proiezione.sala.id)
        self.elenco_proiezioni [chiave] = proiezione
    
    def disponibilità (self, sale: Sale):
        for (sala, orario), proiezione in self.elenco_proiezioni.items(): 
            sala = sale.elenco_sale[proiezione.sala.id]
            proiezione.sala.posti_disponibili = sala.posti_totali

class Stampa_step:
    
    def __init__(self, sale: Sale):
        self.elenco_sale = sale.elenco_sale
        self.elenco_proiezioni = sale.proiezioni.elenco_proiezioni
        
    def f_stampa (self) -> None:
        
        #Sale
        print (f"Elenco sale: \n")
        for sala in self.elenco_sale.values():
            print(f"Sala n° {sala.id} - {sala.nome}: Posti_totali: {sala.posti_totali}")
            
        print(f" \n Elenco proiezioni: \n")
        for (sala, orario), proiezione in self.elenco_proiezioni.items():
            film = proiezione.film
            sala = proiezione.sala
            disponibilità = proiezione.sala.posti_disponibili
            print(f"Proiezione del film '{film.titolo}' nella Sala '{sala.nome}' alle ore {orario}: Disponibili {disponibilità} posti")





#INPUT

#FILMS

films = Films() #creo oggetto elenco film

#elenco istanze film
film1 = Film("Spiderman", 134, "Fantasy")
film2 = Film("Trolls", 94, "Animazione")
film3 = Film("Capitan America", 126, "Fantasy")

#implemento l'elenco films
films.f_add_film(film1)
films.f_add_film(film2)
films.f_add_film(film3)

#implemento proiezioni


#SALE

sale = Sale() #creo l'oggeto elenco sale

#elenco istanze sala
sala1 = Sala (1,"Sala Mastroianni", 200)
sala2 = Sala (2, "Sala Manfredi", 210)
sala3 = Sala (3, "Sala Sordi", 230)

#implemento l'elenco sale
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

# Disponibilità
proiezioni.disponibilità(sale)

#crea oggetto stampa
stampa = Stampa_step(sale)

#metodo stampa dell'oggetto stampa
stampa.f_stampa()
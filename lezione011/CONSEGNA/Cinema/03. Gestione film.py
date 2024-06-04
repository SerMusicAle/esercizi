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
        self.id = id
        self.nome = nome
        self.posti_totali = posti_totali

class Proiezione:

#INIT
    def __init__ (self):
        self.elenco_proiezioni: dict[int, tuple [sala:Sala, film:Film]] = {}
    
    

class Sale:

#INIT
    #l'oggetto sale ha 
    def __init__ (self):       
        self.elenco_sale: dict [int, Sala]= {}    #elenco vuoto dove memorizzare le sale
        self.elenco_proiezioni: dict [Film, tuple[str,str,int, int]] = {} #dizionario proiezioni con chiave Film e valore orario, sala, posti

    def add_sala (self, sala: Sala):
        self.elenco_sale [sala.id] = sala #all'elenco self.sale aggiunge ogni sala impostando id come chiave

    def proiezioni (self, film : Film, sala: Sala, orario : str, posti_disponibili : int, posti_totali : int):            
        
        chiave = film.titolo
        #creo una chiave unica di lettura(input per id) composta id-orario(localizzazione)
        #self.elenco_proiezioni [(sala.id, orario, film.titolo)] = {  # type: ignore
        self.elenco_proiezioni [film.titolo] = {  # type: ignore
            "film": film,       #carico l'intero oggetto film
            "sala": sala,
            "orario": orario,
            "posti disponibili": posti_disponibili,
            "posti_totali": posti_totali,
        }
    def disponibilità (self):
        for chiave, proiezione in self.elenco_proiezioni.items(): 
            self.elenco_proiezioni[]
            self.elenco_proiezioni [chiave]["posti disponibili"] = proiezione["posti_totali"]

class Stampa_step:
    
    def __init__(self, elenco_sale: dict[int, Sala], elenco_proiezioni: dict[tuple[int, str, str], dict]):
        self.elenco_sale = elenco_sale
        self.elenco_sale_list: list[Sala] = list (elenco_sale.values())
        self.elenco_proiezioni = elenco_proiezioni
        
    def f_stampa (self, elenco_sale_list: list[Sala]) -> None:
        
        #Sale
        print (f"Elenco sale: \n")
        for sala in self.elenco_sale_list:
            print(f"Sala n° {sala.id} - {sala.nome}: Posti_totali: {sala.posti_totali}")
            
        print(f"Elenco proiezioni: \n")
        for chiave, proiezione in self.elenco_proiezioni.items():
            film = proiezione["film"]
            sala = proiezione["sala"]
            orario = proiezione["orario"]
            disponibilità = proiezione["disponibilità"]
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

#crea oggetto stampa
stampa = Stampa_step(sale.elenco_sale, sale.elenco_proiezioni)

#metodo stampa dell'oggetto stampa
stampa.f_stampa([])

"""
    Obiettivo:
    classe Media 
    - rappresenti un media generico (ad esempio, un film o un libro) 
    
    classe Film 
    - rappresenti specificamente un film. 
    
    oggetti di queste classi, 
    - aggiungere valutazioni e visualizzare le recensioni.
    
    Specifiche della Classe Media:
    
    Attributi:
    - title (stringa): Il titolo del media.
    - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.
    Metodi:
    - set_title(self, title): Imposta il titolo del media.
    - get_title(self): Restituisce il titolo del media.
    - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
    - getMedia(self): Calcola e restituisce la media delle valutazioni.
    - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioniapprossimata
    - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
    - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
    
    Titolo del Film: The Shawshank Redemption
    Voto Medio: 3.80
    Giudizio: Bello
    Terribile: 10.00%
    Brutto: 10.00%
    Normale: 10.00%
    Bello: 30.00%
    Grandioso: 40.00%
    Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
    
"""
class Media:
#INIT
    def __init__ (self, title: str, reviews: list[int]):
        self.title = title
        self.reviews = reviews
        
    #assegna titolo
    def f_set_title (self, title:str):
        self.title = title
        
    #ritorna titolo
    def f_get_title (self, title:str):
        return self.title
    
    #aggiungi voto alla lista voti
    def f_add_review (self, vote:int):
        self.reviews.append(vote)
     
    #calcola media voti
    def f_get_medium_rate(self):

        media:float = sum(self.reviews) / len(self.reviews)
        return media
  
    #restituisce considerazione corrispondente al valore medio piu vicino
    def f_get_rate(self):
        valori: dict[int, str] = {1:"terribile", 2:"brutto", 3:"normale", 4:"bello", 5:"grandioso"}
        giudizio: float = round(self.f_get_medium_rate())
        if giudizio in valori:
            return valori[giudizio]
                       
    #percentuale di ogni voto
    def f_rate_percent(self, voto):
        conteggio_percent:dict[int, float] = {}
        
        for num in self.reviews:
            if num not in conteggio_percent:
                conteggio_percent[num] = 1
            else:
                conteggio_percent[num] +=1
        
        for num in conteggio_percent:
            conteggio_percent[num] = (conteggio_percent[num] / len(self.reviews)) * 100            
 
    #stampa riassunto valori
    def f_recensione (self):
        print (f"Titolo del film: {self.title} \n"
               f"Voto medio: {self.f_get_medium_rate()} \n"
               f"Giudizio medio: {self.f_get_rate()}"
               f"Terribile: {self.f_rate_percent(1)}"
               f"Brutto: {self.f_rate_percent(2)}")
        for valore in self.reviews:
            
        


class Film(Media):
    # INIT
    def __init__(self, title: str, reviews: list):
        super ().__init__(title, reviews)
        


media01: Film = Film ("Spiderman", [1,2,4,3,5,4,3,5,4])



#media01.add_review (2)
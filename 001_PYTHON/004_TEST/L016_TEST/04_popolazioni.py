class Specie():
#INIT
    def __init__ (self, nome:str, popolazione:int, tasso_crescita:float):
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
    
#BODY    
    def cresci(self):
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita / 100))
    
    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 0
        while self.popolazione < altra_specie.popolazione and anni < 1000:
            self.cresci()
            altra_specie.cresci()
            anni += 1
        return anni
    
    def getDensita(self, area_kmq: float) -> int:
        densità = 0
        anni = 0
        popolazione = self.popolazione
        
        while densità < 1 and anni <1000:
            popolazione : int = int(popolazione * (1 + self.tasso_crescita / 100))
            densità = popolazione / area_kmq
            anni += 1
            
        return anni
    
class BufaloKlingon(Specie):
#INIT
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__('Bufali Klingon', popolazione_iniziale, tasso_crescita)


class Elefante(Specie):
#INIT
   def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__('Elefanti', popolazione_iniziale, tasso_crescita)
    
    
    
#TEST
# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")


"""
una riserva naturale
- Due specie animali: i Bufali Klingon e gli Elefanti
- Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. 
output:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- in quanti anni la popolazione dei Bufali Klingon raggiungerà 
    una densità di 1 individuo per km².
 
Specifiche tecniche
1. Classe Specie

- Attributi:
OK nome (str): Nome della specie.
OK popolazione (int): Popolazione iniziale.
OK tasso_crescita (float): Tasso di crescita annuo percentuale.
- Metodi:
OK __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): 
    Costruttore per inizializzare gli attributi della classe.
OK cresci(self): 
    Metodo per aggiornare la popolazione per l'anno successivo.
OK anni_per_superare(self, altra_specie: 'Specie') -> int: 
    Metodo per calcolare in quanti anni la popolazione di questa specie 
    supererà quella di un'altra specie.
OK getDensita(self, area_kmq: float) -> int: 
    Metodo per calcolare in quanti anni la popolazione 
    raggiungerà una densità di 1 individuo per km².
 
2. Sottoclassi BufaloKlingon e Elefante

inizializzare il nome della specie rispettiva.
 
Formule Matematiche:
Aggiornamento della popolazione per l'anno successivo:
Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
Calcolo della densità di popolazione:
Formula: popolazione / area_kmq
Hint: Loop incrementale che continua ad aggiornare la popolazione finché 
la densità non raggiunge 1 individuo per km²
Calcolo degli anni necessari per superare la popolazione di un'altra specie:
Hint: Loop incrementale che continua ad aggiornare la popolazione di 
entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. 
Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000.     
    
"""
class Sala:
    
#INIT
    def __init__ (self, id: int, nome: str, posti_totali: int): #definisco gli oggetti di tipo Sala
        self.id = id
        self.nome = nome
        self.posti_totali = posti_totali

class Sale:

#INIT
    #l'oggetto sale ha 
    def __init__ (self):       
        self.elenco_sale: dict [int, Sala]= {}    #elenco vuoto dove memorizzare le sale

    def add_sala (self, sala: Sala):
        self.elenco_sale [sala.id] = sala #all'elenco self.sale aggiunge ogni sala impostando id come chiave

class Stampa_step:
    
    def __init__(self, elenco_sale: dict[int, Sala]):
        self.elenco_sale = elenco_sale
        self.elenco_sale_list: list[Sala] = list (elenco_sale.values())
        
    def f_stampa (self, elenco_sale_list: list[Sala]) -> None:
        
        #Sale
        print (f"Elenco sale: \n")
        for sala in self.elenco_sale_list:
            print(f"Sala n° {sala.id} - {sala.nome}: Posti_totali: {sala.posti_totali}")
            
        #Sale



#Crazione oggetti

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
stampa = Stampa_step(sale.elenco_sale)

#metodo stampa dell'oggetto stampa
stampa.f_stampa([])
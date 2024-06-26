class Veicolo():
#INIT
    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
#BODY   
    def descrivi_veicolo(self):
        print (f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")

class Auto(Veicolo):
#INIT
    def __init__ (self, marca:str, modello:str, anno:int, numero_porte:int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
#BODY
    def descrivi_veicolo(self) :
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")

    
class Moto(Veicolo):
#INIT
    def __init__ (self, marca:str, modello:str, anno:int, tipo:str):
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")
        
        # print (f"{super().descrivi_veicolo()}, Tipo: {self.tipo}")
    
    
#TEST
veicolo = Veicolo("Generic", "Model", 2020)
auto = Auto("Toyota", "Corolla", 2021, 4)
moto = Moto("Yamaha", "R1", 2022, "sportiva")

veicolo.descrivi_veicolo()
auto.descrivi_veicolo()
moto.descrivi_veicolo()

veicolo2 = Veicolo("Generic", "Model", 2020)
auto2 = Auto("Honda", "Civic", 2019, 5)
moto2 = Moto("Ducati", "Panigale", 2023, "superbike")

veicolo2.descrivi_veicolo()
auto2.descrivi_veicolo()
moto2.descrivi_veicolo()

"""
EXPECTED
Marca: Generic, Modello: Model, Anno: 2020
Marca: Toyota, Modello: Corolla, Anno: 2021, Numero di porte: 4
Marca: Yamaha, Modello: R1, Anno: 2022, Tipo: sportiva        

Marca: Generic, Modello: Model, Anno: 2020
Marca: Honda, Modello: Civic, Anno: 2019, Numero di porte: 5
Marca: Ducati, Modello: Panigale, Anno: 2023, Tipo: superbike
"""

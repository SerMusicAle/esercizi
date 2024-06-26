"""
Livello 1: Classi e Operazioni Aritmetiche
    Esercizio 2: Operazioni Aritmetiche in una Classe
    Crea una classe Operazioni.
    Definisci un metodo __init__ che inizializza due variabili x e y di tipo intero.
    Definisci un metodo somma che restituisce la somma di x e y.
    Definisci un metodo differenza che restituisce la differenza tra x e y.
    Definisci un metodo prodotto che restituisce il prodotto di x e y.
    Definisci un metodo quoziente che restituisce il quoziente intero e il resto della divisione di x per y.

    Una volta completata la classe, segui questi passaggi per testarla:
    Crea un oggetto della classe Operazioni passando i valori 10 e 5 come argomenti al costruttore.
    Richiama i metodi somma, differenza, prodotto, e quoziente sull'oggetto creato e stampa i risultati.
"""



class Operazioni:
#INIT
    def __init__(self, x: int, y: int):
        # inizializza le variabili
        self.x = x
        self.y = y
#BODY
    def somma(self) -> int:
        # restituisce la somma di x e y
        somma: int = self. x + self.y
        print (f"la somma è {somma}")
        return somma
        
    def differenza(self) -> int:
        # restituisce la differenza tra x e y
        differenza: int = self.x - self.y
        print (f"la differenza è {differenza}")
        return differenza
    
    def prodotto(self) -> int:
        # restituisce il prodotto di x e y
        prodotto: int = self.x * self.y
        print (f"il prodotto è {prodotto}")
        return prodotto
    
    def quoziente(self) -> float:
        # restituisce il quoziente di x diviso y
        quoziente_intero_int: int = self.x//self.y
        quoziente_intero_float: int = self.x/self.y 
        quoziente_resto: float = self.x % self.y
        print (f"il quoziente si può esprimere come {quoziente_intero_float}, {quoziente_intero_int}, con il resto di {quoziente_resto}")
        return quoziente_intero_int, quoziente_intero_float, quoziente_resto
    
    def stampa(self):
        print ("I risultati sono: \n")
        print (f"somma: ", self.somma())
        print (f"differenza: ", self.differenza())
        print (f"prodotto: ", self.prodotto())
        print (f"quoziente: ", self.quoziente())
        quoziente_int, quoziente_float, resto = self.quoziente()
        print(f"Quoziente intero: {quoziente_int}, Quoziente float: {quoziente_float}, Resto: {resto}")

        

#INPUT
oggetto_valori = Operazioni (2, 3)
oggetto_valori.somma()
oggetto_valori.differenza()
oggetto_valori.prodotto()
oggetto_valori.quoziente()

"""
Livello 1: Classi e Variabili
    Esercizio 1: Dichiarazione di Variabili in una Classe
    Crea una classe Variabili.
    Definisci un metodo __init__ che inizializza due variabili x e y di tipo intero.
    Definisci un metodo stampa_variabili che stampa i valori di x e y.
    
    Una volta completata la classe, segui questi passaggi per testarla:
    Crea un oggetto della classe Variabili passando i valori 10 e 5 come argomenti al costruttore.
    Richiama il metodo stampa_variabili sull'oggetto creato per stampare i valori delle variabili x e y.
"""

class Variabili:
#INIT
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
#BODY
    def stampa_variabili(self):
        print (f"x vale {self.x}")
        print (f"y vale {self.y}")

# input
oggetto_var = Variabili(10, 5)
oggetto_var.stampa_variabili()

"""
Esercizio 3: Operazioni con Tipi di Dati Diversi
    Crea una classe OperazioniMiste.
    Definisci un metodo __init__ che inizializza tre variabili: un intero, un float e una stringa.
    Definisci un metodo somma che somma l'intero e il float e restituisce il risultato.
    Definisci un metodo concatenazione che concatena la stringa con l'intero (convertito in stringa) e restituisce il risultato.
    
    Una volta completata la classe, segui questi passaggi per testarla:
    Crea un oggetto della classe OperazioniMiste passando i valori 10, 5.5 e "Numero: " come argomenti al costruttore.
    Richiama il metodo somma e stampa il risultato.
    Richiama il metodo concatenazione e stampa il risultato.
"""

class OperazioniMiste:
#INIT
    def __init__(self, x: int, y: float, z: str):
        self.x = x
        self.y = y
        self.z = z
#BODY
    def somma(self) -> float:
        self.intfloat: float = self.x + self.y
        return (f"la somma in float tra un int e un float è {self.intfloat}")

    def concatenazione(self) -> str:
        self.strfloat: str = (f"{self.z} {self.intfloat}")
        return self.strfloat
    
    def stampa (self):
        print (f" {self.strfloat} ")

valori = OperazioniMiste (10, 5.5, "la somma dei numeri int e float è: ")
valori.somma()
valori.concatenazione()
valori.stampa()
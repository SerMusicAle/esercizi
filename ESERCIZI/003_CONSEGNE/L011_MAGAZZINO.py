"""
Gestione di un magazzino
    metodi
    - aggiungere prodotti al magazzino, 
    - cercare prodotti per nome
    - verificare la disponibilità di un prodotto.

classe Prodotto attributi:
    - nome (stringa)
    - quantità (intero)
 
classe Magazzino metodi:
    - aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
    - cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
    - verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:
Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
Il sistema cerca un prodotto per verificare se esiste nell'inventario.
Il sistema verifica la disponibilità dei prodotti in inventario.
    
    """

class Prodotto:

#INIT   
    def __init__ (self, nome:str, quantity: int):
        self.nome = nome
        self.quantity = quantity

class Magazzino:
#INIT  
    def __init__ (self):
        self.elenco_prodotti: dict[str, Prodotto] = {}
        
    def add_prodotto (self, prodotto : Prodotto):
        self.elenco_prodotti [prodotto.nome] = prodotto   
 
    def cerca_prodotto (self, nome:str)-> bool:
        return nome in self.elenco_prodotti

    def verifica_disponibilità(self, nome:str):
        a : bool = self.cerca_prodotto(nome)
        if a:
            return f"il prodotto {nome} è disponibile"
        else:
            print(f"Il prodotto {nome} non esiste nel magazzino.")
            return None



# Creazione del magazzino
magazzino = Magazzino()

# Creazione di alcuni prodotti
prodotto1 = Prodotto("Mela", 10)
prodotto2 = Prodotto("Banana", 20)
prodotto3 = Prodotto("Arancia", 15)

# Aggiunta dei prodotti al magazzino
magazzino.add_prodotto(prodotto1)
magazzino.add_prodotto(prodotto2)

# Test di cerca_prodotto

print(magazzino.cerca_prodotto("Arancia"))  # Output: False
print(magazzino.cerca_prodotto("Mela"))  # Output: True
print(magazzino.cerca_prodotto("Banana"))  # Output: True

# Test di verifica_disponibilità
print(magazzino.verifica_disponibilità("Mela"))  # Output: Il prodotto Mela è disponibile
print(magazzino.verifica_disponibilità("Banana"))  # Output: Il prodotto Banana è disponibile
print(magazzino.verifica_disponibilità("Arancia"))  # Output: Il prodotto Arancia non esiste nel magazzino.

"""

#TEST CASE

import unittest
from unittest import TestCase
from magazzino import Prodotto, Magazzino

class TestMagazzino(TestCase):

    def setUp(self):
        self.magazzino = Magazzino()
        self.prodotto1 = Prodotto(nome="Mela", quantità=10)
        self.prodotto2 = Prodotto(nome="Banana", quantità=20)
        self.prodotto3 = Prodotto(nome="Arancia", quantità=15)
        
        self.magazzino.aggiungi_prodotto(self.prodotto1)
        self.magazzino.aggiungi_prodotto(self.prodotto2)
        self.magazzino.aggiungi_prodotto(self.prodotto3)

    def test_aggiungi_prodotto(self):
        prodotto4 = Prodotto(nome="Pera", quantità=5)
        self.magazzino.aggiungi_prodotto(prodotto4)
        self.assertEqual(self.magazzino.cerca_prodotto("Pera"), prodotto4)

    def test_cerca_prodotto(self):
        result = self.magazzino.cerca_prodotto("Mela")
        self.assertEqual(result, self.prodotto1)

    def test_verifica_disponibilità(self):
        result = self.magazzino.verifica_disponibilità("Banana")
        self.assertEqual(result, "Il prodotto Banana è disponibile in quantità: 20")
        
        result = self.magazzino.verifica_disponibilità("Uva")
        self.assertEqual(result, "Il prodotto Uva non è disponibile")

if __name__ == "__main__":
    unittest.main()
    
"""
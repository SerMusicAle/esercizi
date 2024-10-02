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
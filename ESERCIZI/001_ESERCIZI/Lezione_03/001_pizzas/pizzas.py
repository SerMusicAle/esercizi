"""
"4-1. Pizze: 
    Pensa a almeno tre tipi di pizza che ti piacciono. 
    Memorizza questi nomi di pizza in una lista e poi usa un ciclo for per stampare il nome di ciascuna pizza.
    • Modifica il tuo ciclo for per stampare una frase utilizzando il nome della pizza. 
        Per ogni pizza, una riga di output come: Mi piace la pizza al pepperoni.
    • Aggiungi una riga alla fine del tuo programma, fuori dal ciclo for, che indichi quanto ti piace la pizza. 
    L'output dovrebbe consistere in tre o più righe sui tipi di pizza che ti piacciono e poi una frase aggiuntiva, come Adoro davvero la pizza!"

    Questo esercizio ti chiede di lavorare con una lista di nomi di pizza e di stampare diverse frasi basate su questi nomi utilizzando un ciclo for. 
    Alla fine, aggiungi una frase generica che esprima quanto ami la pizza in generale.
    
"""

class Pizzas ():
#INIT
    def __init__ (self, pizzas:list [str]):
        self.__pizzas = pizzas

#BODY    
    def f_stampalist (self):
        pizzas: list [str] = []
        for pizza in self.__pizzas:
            pizzas.append(pizza)
        return pizzas

    def f_stampadict (self):
        pizzasdict: dict [str,str] = {}
        for pizza in self.__pizzas:
            pizzasdict[pizza] = f"mi piace la pizza {pizza}"
        return pizzasdict


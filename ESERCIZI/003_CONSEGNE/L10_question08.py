"""
Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.

"""


#VERSIONE INEFFICIENTE. NON PREVEDE I CASI IN CUI ORE1 > ORE2

def f_seconds_since_noon(ore1:int, minuti1:int, secondi1:int, ore2:int, minuti2:int, secondi2:int):

#INIT
    totale:int = 0

#BODY
    while ore1!=ore2 or minuti1!= minuti2 or secondi1 != secondi2:

        secondi1 +=1
        totale += 1

        if secondi1 == 60:
            secondi1 = 0
            minuti1 += 1        

        if minuti1 == 60:
            minuti1 = 0
            ore1 +=1

        if ore1 == 24:
            ore1 = 0

#RETURN
    print (totale)

#INPUT
ore1: int = 1
ore2: int = 3
minuti1: int = 0
minuti2: int = 15
secondi1: int = 0
secondi2: int = 30

#CALL

f_seconds_since_noon(ore1, minuti1, secondi1, ore2, minuti2, secondi2)


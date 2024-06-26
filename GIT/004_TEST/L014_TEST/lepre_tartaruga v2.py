"""
Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali per  una simulazione 
- Definire e utilizzare:
    OK - una funzione per visualizzare le posizioni sulla corsia di gara,
    OK - una funzione per calcolare la mossa della tartaruga,
    OK - una funzione per calcolare la mossa della lepre.
- Implementare un ciclo per simulare i tick dell'orologio. Ad ogni tick:
    - calcolare le mosse, 
    - mostrare la posizione sulla corsia di gara, 
    - determinare l'eventuale fine della gara.

Percorso 
    OK - 70 quadrati rappresentanti le posizioni di un percorso con una lista
    OK - Il traguardo è al quadrato 70 
    OK - inizia la gara dal quadrato \#1
    OK - Usate delle variabili per tenere traccia delle posizioni degli animali: (i numeri delle posizioni sono da 1 a 70).
    OK - C'è un orologio che conta i secondi. 
        OK - per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra:
            OK - la lettera 'T' nella posizione della tartaruga, 
            OK - la lettera 'H' nella posizione della lepre, 
            OK - il carattere '_' nelle posizioni libere.
    OK - Iniziate la gara stampando: 'BANG !!!!! AND THEY'RE OFF !!!!!'
    OK - Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.
    - Dopo la stampa di ogni tick, 
        OK - verificate se gli animali hanno raggiunto o superato il quadrato 70. 
            OK - Se è così, stampate il nome del vincitore e terminate la simulazione. 
            OK - Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". 
            OK - Se vince la lepre, stampate "HARE WINS || YUCH!!!". 
            OK - Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". 
            OK - Se non vince nessun animale, eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

- Tartaruga:
    OK- Passo veloce (50% di probabilità): avanza di 3 quadrati.
    OK- Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    OK- Passo lento (30% di probabilità): avanza di 1 quadrato.
    
- Lepre:
    OK - Riposo (20% di probabilità): non si muove.
    OK - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    OK - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    OK - Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    OK - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.
    OK - tecnica di movimento della tartarua seguendo le regole della lepre.

- Valori passi 
    OK    eseguite un "passo veloce" quando 1 ≤ i ≤ 5, 
    OK    una "scivolata" quando 6 ≤ i ≤ 7, 
    OK    un "passo lento" quando 8 ≤ i ≤ 10

- Animali
    OK - Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.
    OK - Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza").
    OK - i contendenti possono occasionalmente perdere terreno. 
    OK - Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10.
    OK - Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:
    OK- quando si troveranno sullo stesso quadrato la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione

    """

import random

def posizioni ():

#INIT
    percorso:list = ["*"] * 70
    traguardo = len (percorso)-1
    
    tartaruga: int = 1
    lepre: int = 1
    
    cont:int = 0
    lepre_energia = 100
    tartaruga_energia = 100

    bonusmalus: dict = {15: -1, 30: -3, 45: -5, 60: -7, 10: 5, 25: 3, 50: 10}

#BODY
    print (f"BANG !!!!!") 

    while lepre < traguardo and tartaruga < traguardo:

        cont+=1

        #lepre
        lepredep = lepre
        dado = random.randint (1, 10)

        if 1 <= dado <= 2 and lepre_energia <= 90:
            lepre_energia += 10
        elif 3 <= dado <= 4 and lepre_energia >= 15:
            lepre +=9
            lepre_energia -= 15
            if lepre > traguardo:
                lepre = lepredep
        elif 5 <= dado <= 6 and lepre_energia >= 20:
            if lepre <=13:
                lepre = 1
            else:
                lepre -= 12
                lepre_energia -= 20
                if lepre < 1:
                    lepre = lepredep
        elif 7 <= dado <= 8 and lepre_energia >= 5:
            lepre +=1
            lepre_energia -= 5
        elif 9 <= dado <= 10 and lepre_energia >= 8:
            if lepre <=2:
                lepre = 1
            else:
                lepre -= 2
                lepre_energia -=8

        #bonusmalus
        if lepre in bonusmalus:
            percorso[lepre] = "*"
            lepre += bonusmalus[lepre]
            percorso[lepre] = "L"

        if tartaruga in bonusmalus:
            percorso[tartaruga] = "*"
            tartaruga += bonusmalus[tartaruga]
            percorso[tartaruga] = "T"

        #tartaruga
        tartarugadep = tartaruga        
        dado = random.randint (1, 10)

        if 1 <= dado <= 5 and tartaruga_energia >= 5:
            tartaruga +=3
            tartaruga_energia -= 5
            if tartaruga > traguardo:
                tartaruga = tartarugadep
        elif 6 <= dado <= 7 and tartaruga_energia >= 10:
            if tartaruga <=6:
                tartaruga = 1
            else:
                tartaruga -= 6
                tartaruga_energia -=10
        elif 8 <= dado <= 10 and tartaruga_energia >= 3:    
            tartaruga +=1
            tartaruga_energia -=3
        
        #meteo
        if 1 < cont < 9 or 21 < cont < 29 or 41 < cont < 49 or 61 < cont < 69:
            tartaruga = max(1, tartaruga - 1)
            lepre = max(1, lepre - 2)


        #verifiche
        percorso = ["*"]*70
        if lepre == tartaruga:
            percorso [lepre] = "OUCH!!!"
        else:
            percorso [lepre] = "L"
            percorso [tartaruga] = "T"
        print (' '.join(percorso))
    
    if lepre == tartaruga:
        percorso[lepre] = (f"IT'S A TIE.")
    
    elif lepre == traguardo:
        print (f"HARE WINS || YUCH!!!")
        
    elif tartaruga == traguardo:
        print(f"TORTOISE WINS! || VAY!!!")

        


def tartaruga():
    pass

def lepre ():
    pass


posizioni()

    





"""
SFIDE AGGIUNTIVE:
1. Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o 
aumentare la probabilità di scivolate per entrambi i concorrenti. 
Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
OK - La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
OK - La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
 
2. Energia o Stamina:
Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. L'energia inziale per entrambi gli animali è 100.

Nuove regole di movimento:
- Tartaruga:
OK    - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, essa guadagna 10 di energia. Non può superare l'energia iniziale.
OK    - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
OK    - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
OK    - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

- Lepre:
OK    - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
OK    - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
OK    - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
OK    - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
OK    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
 
OK 3. Ostacoli e Bonus
Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, 
che influenzano direttamente il movimento degli animali quando vengono calpestati. 
Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

Dettagli Implementativi:
OK - Ostacoli:
Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), 
gli ostacoli riducono la posizione dell'animale di un numero specificato di quadrati (es: -3, -5, -7).
Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli 
sul percorso (chiave) ed i relativi effetti (valore). 
Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito di un ostacolo.

OK - Bonus:
Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), 
i bonus aumentano la posizione dell'animale di un numero determinato di quadrati (es: 5, 3, 10). 
I bonus sono rappresentati da un dizionario che mappa le posizioni dei bonus sul percorso (chiave)
ed i relativi effetti (valore). Consentire agli animali di beneficiare pienamente dei bonus, 
ma non oltrepassare il traguardo.


"""
"""
Logica
- Prenotazioni aeree. 
- diverse tipologie di voli, tra cui voli commerciali e voli charter.

 
Classe astratta Volo:
    - INIT: 
        codice del volo (stringa) 
        capacità massima di posti disponibili sul volo (numero intero) passati in input. 
        prenotazioni, nonpassato dal costruttore con valore iniziale pari a 0 
 
    - prenota_posto(abc)
    - posti_disponibili(abc)
    
Classe VoloCommerciale(Volo):
    - INIT (codice del volo, capacità massima) 
        posti_economica, parte di postitot 
        posti_business, parte di postitot
        posti_prima; . parte di postitot 
        Si può pensare di riservare il 70% dei posti alla classe economica, il 20% dei posti alla classe business ed i restanti posti alla prima classe. Inoltre, il costruttore deve creare tre valori interi pari a 0, chiamati prenotazioni_economica, prenotazioni_business, prenotazioni_prima.
 
    Metodi:
        posti_disponibili(): 
            ritornapostitot:dict con quattro chiavi: 'posti disponibili', 'classe economica', 'classe business', 'prima classe'. 
        prenota_posto(posti, classe_servizio): 
            prenotare un certo numero di posti sul volo in una determinata classe. 
            se possibile prenotare un posto stampare messaggio che notifichi  di aver riservato un tot di posti per una determinata classe su un dato volo (specificando il codice del volo). In caso contrario, stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti disponibili nella classe scelta. Se sul volo non ci sono più posti disponibili, il metodo deve stampare a schermo un messaggio notificando all'utente che il volo è al completo. Inoltre, se la classe passata come input del metodo non risulta essere una delle seguenti classi ("economica", "business", "prima"), il metodo deve stamapre a schermo un messaggio di errore, notificando all'utente che la classe richiesta non è valida. Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di prenotazioni ricevute per ogni classe di servizio, poi aggiornare gli attributi prenotazioni_economica, prenotazioni_business, prenotazioni_prima con l'esatto numero delle prenotaioni ricevute per ogni classe di servizio. Suggerimento: introdurre delle variabili locali d'appoggio per gestire le prenotazioni per ogni classe di servizio da azzerare all'inizio di ogni fase di prenotazione.

Classe VoloCharter(volo):
    INIT (codice, capacità massima di posti disponibili sul volo, costo del volo (numero float) charter
        acquisto tuttii posti  da un tour operator ad un certo prezzo.
    
    posti_disponibili(): che ritorna il numero di posti disponibili totali sul volo.
    
    prenota_posto(): 
        se posti =!0 prenota tutti e stampa volo ( codice del volo): prenotazione avvenuta. mostrando il prezzo.
        In caso contrario,stampa messaggio che il volo charter è gia prenotato.
        

Classe CompagniaAerea:
    INIT (nome compagnia, prezzo standard di un biglietto (numero float)), 
        lista vuota chiamata flotta. 
        
    aggiungi_volo(volo_commericiale): 
        il volo_commerciale deve essere aggiunto alla flotta della compagnia aerea.

    rimuovi_volo(volo_commericiale): 
        il volo_commerciale deve essere rimosso dalla flotta della compagnia aerea.

    mostra_flotta(): 
        tale metodo deve stampare a schermo tutti i voli che fanno parte della flotta della compagnia 
        specificando il codice di ogni volo.

    guadagno(): 
        questo metodo deve calcolare e ritornare (come float arrotondato alle prime due cifre decimali)
        il guadagno ricavato dalla vendita dei biglietti aerei dei voli nella sua flotta. 
        Su ogni aereo della flotta, il prezzo  per un posto in classe economica è pari a prezzo standard, 
        il prezzo per un posto in classe business è pari al doppio del prezzo standard, 
        mentre il prezzo per un posto in prima classe vale tre volte il prezzo standard.

Test con codice driver
Scrivere un codice driver che consenta di creare voli commerciali e voli charter.
Per il volo commerciale eseguire i seguenti passaggi:
mostrare su schermo tutti i posti disponibili sul volo
provare a prenotare un tot di posti in classe economica, esaurendo i posti disponibili in tale classe (70% dei posti totali dell'aereo).
provare a prenotare un tot di posti in classe business, esaurendo i posti disponibili in tale classe (20% dei posti totali dell'aereo).
provare a prenotare un tot di posti in prima classe maggiore della capacità di tale classe (70% dei posti totali dell'aereo), il codice avviserà l'utente non è possibile prenotare quel tot di posti (70%).
riprovare a prenotare un tot di posti in prima classe, esaurendo i posti disponibili in tale classe (10% dei posti totali dell'aereo).
effettuare un altro tentativo di prenotazione. Questa volta, la prenotazione non dovrebbe andare a buon fine in quanto il volo deve risultare completo!
NOTA: Per ogni tentativo di prenotazione, stampare i posti disponibili rimasti sul volo commerciale.
Per il volo charter eseguire i seguenti passaggi:
stampare a schermo i posti disponibili sul volo
provare a prenotare tutto il volo charter
provare ad effettuare un secondo tentativo di prenotazione. In questo caso, la prenotazione dovrebbe fallire, in quanto il volo charter dovrebbe essere già prenotato.
Successivamente, creare un secondo volo commerciale e provare a prenotare un tot di posti in economica.
 
Infine, creare una compagnia aerea. Aggiungere i due voli commerciali alla compagnia aerea. Stampare la flotta della compagnia aerea. Calcolare il guadagno della compagnia aerea ricavato dalla vendita dei biglietti aerei dei voli della sua flotta.
"""

from abc import ABC, abstractmethod

class Volo(ABC):
    def __init__(self, codfly: str, postitot: int, prenotazioni: int = 0):
        self.codfly = codfly
        self.postitot = postitot
        self.prenotazioni = prenotazioni

    @abstractmethod
    def prenota_posto(self, posti: int, classe: str):
        pass

    @abstractmethod
    def posti_disponibili(self):
        pass

class VoloCommerciale(Volo):
    def __init__(self, codfly: str, postitot: int):
        super().__init__(codfly, postitot)
        self.posti_eco = int(self.postitot * 0.7)
        self.posti_business = int(self.postitot * 0.2)
        self.posti_prima = int(self.postitot * 0.1)
        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0
        
    def posti_disponibili(self):
        return {
            'posti disponibili': self.postitot - self.prenotazioni,
            'classe economica': self.posti_eco - self.prenotazioni_economica,
            'classe business': self.posti_business - self.prenotazioni_business,
            'prima classe': self.posti_prima - self.prenotazioni_prima
        }
        
    def prenota_posto(self, posti: int, classe: str):
        if classe not in ["classe economica", "classe business", "prima classe"]:
            print(f"Classe {classe} non valida.")
            return
        
        posti_residui = self.posti_disponibili()
        
        if classe == 'classe economica':
            if posti_residui['classe economica'] >= posti:
                self.prenotazioni_economica += posti
            else:
                print(f"Non ci sono abbastanza posti disponibili in classe economica su {self.codfly}.")
                return
        elif classe == 'classe business':
            if posti_residui['classe business'] >= posti:
                self.prenotazioni_business += posti
            else:
                print(f"Non ci sono abbastanza posti disponibili in classe business su {self.codfly}.")
                return
        elif classe == 'prima classe':
            if posti_residui['prima classe'] >= posti:
                self.prenotazioni_prima += posti
            else:
                print(f"Non ci sono abbastanza posti disponibili in prima classe su {self.codfly}.")
                return

        self.prenotazioni += posti
        print(f"Sono stati prenotati {posti} posti in {classe} sul volo {self.codfly}.")

class VoloCharter(Volo):
    def __init__(self, codfly: str, postitot: int, costo_charter: float):
        super().__init__(codfly, postitot)
        self.costo_charter = costo_charter

    def posti_disponibili(self):
        return self.postitot - self.prenotazioni

    def prenota_posto(self, posti: int, classe: str = None):
        if self.prenotazioni == 0:
            self.prenotazioni = self.postitot
            print(f"Il volo {self.codfly} è stato prenotato per un costo di {self.costo_charter}.")
        else:
            print(f"Il volo {self.codfly} è già prenotato.")

class CompagniaAerea:
    def __init__(self, nome_compagnia: str, prezzo_standard: float):
        self.nome_compagnia = nome_compagnia
        self.prezzo_standard = prezzo_standard
        self.flotta = []

    def aggiungi_volo(self, volo: Volo):
        self.flotta.append(volo)

    def rimuovi_volo(self, volo: Volo):
        if volo in self.flotta:
            self.flotta.remove(volo)

    def mostra_flotta(self):
        for volo in self.flotta:
            print(volo.codfly)

    def guadagno(self):
        guadagno_totale = 0.0
        for volo in self.flotta:
            if isinstance(volo, VoloCommerciale):
                guadagno_totale += (self.prezzo_standard * volo.prenotazioni_economica +
                                    self.prezzo_standard * 2 * volo.prenotazioni_business +
                                    self.prezzo_standard * 3 * volo.prenotazioni_prima)
            elif isinstance(volo, VoloCharter):
                guadagno_totale += volo.costo_charter if volo.prenotazioni == volo.postitot else 0
        return round(guadagno_totale, 2)

# Codice driver per testare le classi

# Creare un volo commerciale
volo_commerciale = VoloCommerciale("VC123", 100)

# Mostrare su schermo tutti i posti disponibili sul volo commerciale
print("Posti disponibili su VC123:", volo_commerciale.posti_disponibili())

# Provare a prenotare 70 posti in classe economica
volo_commerciale.prenota_posto(70, 'classe economica')
print("Posti disponibili su VC123:", volo_commerciale.posti_disponibili())

# Provare a prenotare 20 posti in classe business
volo_commerciale.prenota_posto(20, 'classe business')
print("Posti disponibili su VC123:", volo_commerciale.posti_disponibili())

# Provare a prenotare 15 posti in prima classe (tentativo fallito)
volo_commerciale.prenota_posto(15, 'prima classe')
print("Posti disponibili su VC123:", volo_commerciale.posti_disponibili())

# Provare a prenotare 10 posti in prima classe
volo_commerciale.prenota_posto(10, 'prima classe')
print("Posti disponibili su VC123:", volo_commerciale.posti_disponibili())

# Effettuare un altro tentativo di prenotazione (tentativo fallito)
volo_commerciale.prenota_posto(5, 'prima classe')
print("Posti disponibili su VC123:", volo_commerciale.posti_disponibili())

# Creare un volo charter
volo_charter = VoloCharter("VC456", 150, 10000.0)

# Stampare a schermo i posti disponibili sul volo charter
print("Posti disponibili su VC456:", volo_charter.posti_disponibili())

# Provare a prenotare tutto il volo charter
volo_charter.prenota_posto(150)
print("Posti disponibili su VC456:", volo_charter.posti_disponibili())

# Provare ad effettuare un secondo tentativo di prenotazione (tentativo fallito)
volo_charter.prenota_posto(150)
print("Posti disponibili su VC456:", volo_charter.posti_disponibili())

# Creare un secondo volo commerciale
volo_commerciale2 = VoloCommerciale("VC789", 100)
volo_commerciale2.prenota_posto(70, 'classe economica')
print("Posti disponibili su VC789:", volo_commerciale2.posti_disponibili())

# Creare una compagnia aerea
compagnia = CompagniaAerea("AirTest", 100.0)

# Aggiungere i voli commerciali alla compagnia aerea
compagnia.aggiungi_volo(volo_commerciale)
compagnia.aggiungi_volo(volo_commerciale2)

# Stampare la flotta della compagnia aerea
print("Flotta della compagnia:")
compagnia.mostra_flotta()

# Calcolare il guadagno della compagnia aerea
print("Guadagno totale:", compagnia.guadagno())

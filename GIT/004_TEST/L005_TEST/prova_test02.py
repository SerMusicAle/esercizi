#DESCRIPTION FUNCTION
"""
mano = somma valori
carta tra 2 e 11
asso 1 o 11 a scelta
mani da 3 car} te

"""
def blackjack_hand_total(cards: list[int]) -> int:
    totaleprov = sum(cards)-1
    if totaleprov+10>21:
        pass
    else:
        for i in cards:
            if i==1 and (sum(cards)+10)==21:
                totale = sum(cards)+10
            else:
                totale=sum(cards)






    totale =0
    for i in cards:
        #verifica corrispondenza e doppio valore
        if i==1:
        
            #totale meno carta 1
            totaleprov = sum(cards)-1
            if (21-totaleprov) < 11:
                totale = sum(cards)
            elif totaleprov == sum(cards)-11:
                totale = sum(cards)+10
            else:
                totale = sum(cards)
    return totale



def blackjack_hand_total(cards: list[int]) -> int:
    total = sum(cards)  # Calcola la somma totale dei valori delle carte
    
    # Controlla se c'è almeno un asso (valore 1) nella mano
    has_ace = 1 in cards
    
    # Se c'è un asso nella mano e aggiungendo 10 non si supera 21, considera l'asso come 11
    if has_ace and total + 10 <= 21:
        total += 10
    
    return total

def blackjack_hand_total(cards: list[int]) -> int:
    total = sum(cards)  # Calcola la somma totale dei valori delle carte
    
    # Controlla se c'è almeno un asso (valore 1) nella mano e se aggiungendo 10 non si supera 21
    if 1 in cards and total + 10 <= 21:
        total += 10
    
    return total


def blackjack_hand_total(cards: list[int]) -> int:
    assert len(cards) == 3, "La mano deve consistere esattamente di 3 carte"
    
    total = sum(cards)  # Calcola la somma totale dei valori delle carte
    
    # Verifica se c'è un asso (valore 1) nella lista di carte
    if 1 in cards:
        # Calcola il totale considerando l'asso come 11 anziché 1 se non si supera 21
        if total + 10 <= 21:
            total += 10  # Fai valere l'asso come 11 per ottenere il totale ottimale
    
    return total


def blackjack_hand_total(cards: list[int]):
    
    totaleprov = sum(cards)
    totale=0
    if totaleprov+10>21:
        pass
    else:
        
        for i in cards:
            if i==1 and (sum(cards)+10)==21:
                totale = sum(cards)+10
                if i==1 and (sum(cards)+10<21):
                    totale=sum(cards)
    return (totale)


def blackjack_hand_total(cards: list[int]):
    # Inizializza il totale delle carte senza considerare l'asso
    total = sum(cards)
    has_ace = 1 in cards

    # Se c'è un asso e aggiungendo 10 non si sballa la mano, valuta l'asso come 11
    if has_ace and total + 10 <= 21:
        total += 10

    return total


def blackjack_hand_total(cards: list[int]):
    # Inizializza il totale delle carte senza considerare l'asso
    total = sum(cards)
    has_ace = 1 in cards

    # Se c'è un asso e aggiungendo 10 non si sballa la mano, valuta l'asso come 11
    if has_ace and total + 10 <= 21:
        total += 10

    return total

def blackjack_hand_total(cards: list[int]):
    # Calcola il totale dei valori delle carte senza considerare l'asso
    totale = sum(cards)
    
    # Se c'è un asso nella mano e aggiungendo 10 non si supera 21, valuta l'asso come 11
    if 1 in cards and totale + 10 <= 21:
        totale += 10

    return totale


def blackjack_hand_total(cards: list[int]):
    
    #dichiarazione
    totale = sum(cards)
    
    #istruzioni
    if totale+10>21:
        pass
    else:
        if 1 in cards:
            if totale + 10 <=21:
                totale += 10
    return totale


def blackjack_hand_total(cards: list[int]):
    
    #dichiarazione
    totale = sum(cards)
    
    #istruzioni
    if totale+10>21:
        pass
    else:
        if 1 in cards:
            if totale + 10 <21:
                totale += 10
            else:
                totale +=10
    return totale

for carta in cards:
    if conto + carta <=21:
        conto + carta
    else
        carta=1
        conto +=carta
return conto


    totale = sum(cards)
    
    #istruzioni
    if totale+10>21:
        pass
    elif 1 in cards:
        if totale + 10 <21:
            totale += 10
        else:
            totale +=10
    return totale
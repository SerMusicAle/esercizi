"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

"""

def anagram(s: str, t: str) -> bool:
    cont = 0
    for i in s:
        for l in t:
            if i == l:
        cont +=1
    else:
        False
    pass
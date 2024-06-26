"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

"""

#VERSION 1
def anagram(s: str, t: str) -> bool:
    
    #DEC
    cont = 0

    lista = list(t)
    t = t.lower()
    s = s.lower()
    #BODY
    for i in s:
        for l in lista:
            if i == l:
                lista.remove(l)
                cont += 1
    if cont == len(s):
        return True
    else:
        return False
    



    #VERSION.2

    def anagram(s: str, t: str) -> bool:
    
    #DEC
    lista = list(t)
    t = t.lower()
    s = s.lower()

    #BODY
    if len(s) == len(t):
        for i in s:
            if i in lista:
                lista.remove(i)
        if lista == []:
            True
        else:
            False
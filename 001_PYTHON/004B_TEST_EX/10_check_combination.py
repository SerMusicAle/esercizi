"""
    funzione(A, B, e C) 
        combinazione soddisfatta 
        L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
        La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

    For example:

        Test	Result
        print(check_combination(True, False, True))
        Operazione permessa
        print(check_combination(False, True, False))
        Operazione negata
"""
    
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    ok: str = "Operazione permessa"
    no:str = "Operazione negata"
    if conditionA or (conditionB and conditionC):
        return ok
    else:
        return no

    
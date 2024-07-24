"""
EX.02
    funzione (username, password e status bool)
        accesso consentito con 
            utente "admin", 
            password "12345"
            account True. 
        ritorna "Accesso consentito" oppure "Accesso negato".
    For example:

    Test	Result
    print(check_access("admin", "12345", True))
    Accesso consentito
    print(check_access("admin", "54321", True))
    Accesso negato

    
    """
    
def check_access(username: str, password: int, status: bool) -> str:
    conferma:str = "Accesso consentito" 
    negato: str = "Accesso negato"
    if username == "admin" and password == "12345" and status== True:
        return conferma
    else:
        return negato
        
# cancella ... è definisci il tipo di dato per password, successivamente cancella pass e scrivi il tuo codice
        
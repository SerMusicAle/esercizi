#DESCRIPTION FUNCTION
"""
    5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
    • If the list is empty, print the message We need to find some users!
    • Remove all of the usernames from your list, and make sure the correct message is printed.
"""

#FUNCTION
def f_saluto_utenti(utenti):
    
    #BODY 
    #verify is not empty
    if utenti:
        for utente in utenti:
            if utente == 'admin':
                print("Ciao admin, vuoi vedere un rapporto di stato?")
            else:
                print(f"Ciao {utente.title()}, grazie per esserti nuovamente connesso.")
    else:
        print("Dobbiamo trovare degli utenti!")


#EXECUTION 1 list empty
print(f"----- Sessione 1: Lista vuota -----")
utenti_vuoti = []

#CALL FUNCTION
f_saluto_utenti(utenti_vuoti)
print()

#EXECUTION 2 list full to empty
print("----- Sessione 2: Lista non vuota e poi svuotata -----")
utenti_iniziali = ['admin', 'alice', 'bob', 'charlie']
f_saluto_utenti(utenti_iniziali)
print()
    


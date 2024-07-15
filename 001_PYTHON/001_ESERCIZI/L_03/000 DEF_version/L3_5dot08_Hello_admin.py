#DESCRIPTION FUNCTION
"""
    5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
    • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
    • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
"""

#FUNCTION

def f_hello_admin():

    #BODY
    #DECLARATION LOCAL VAR
    utenti = ['admin', 'alice', 'bob', 'charlie', 'dave']

    # Loop for message
    for utente in utenti:
        if utente == 'admin':
            print("Ciao admin, vuoi vedere un rapporto di stato?")
        else:
            print(f"Ciao {utente.title()}, grazie per esserti nuovamente connesso.")

#CALL FUNCTION
f_hello_admin()



#DESCRIPTION FUNCTION
"""
    3-2. Greetings: Start with the list you used in Exercise 3-1, 
    but instead of just printing each person’s name, print a message to them. 
    The text of each message should be the same, but each message should be personalized with the person’s name.
"""
#FUNCTION
def f_invites (quantity):

    #DECLARATION LOCAL VAR - none
    
    #INPUT - verify quantity
    while True:
        try:
            #un input è sempre str quindi va convertito automaticamente
            if quantity > 0:
                break
            else:
                print("Inserisci un numero valido (maggiore di zero).")
        #errore di tipo errato
        except ValueError:
            print("Inserisci un numero valido, non altri caratteri.")
    #BODY - generate the list by input string
    
    #DECLARATION LOCAL VAR - none
    invites: dict = {}    

    #INPUT - names  
    for _ in range (quantity):
        name: str = input(f"dimmmi un nome di chi vuoi invitare ")
        message: str = input(f"inserisci un messaggio personale per ogni amico separando li da una virgola ")
        invites [name] = message
        lista: list = []

    #RETURN
    return invites 

#INPUT - quanti invitati?
quantity = int(input(f"quante persone vuoi invitare?"))
        
#CALL FUNCTION
res = f_invites(quantity)    

#EXECUTION
for name, message in res.items():
    print (f"Nome: {name}, Messaggio:{message}")




#DESCRIPTION FUNCTION
"""
    3-2. Greetings: Start with the list you used in Exercise 3-1, 
    but instead of just printing each person’s name, print a message to them. 
    The text of each message should be the same, but each message should be personalized with the person’s name.
"""
#FUNCTION
def f_names (names_input, messages_input):

    #DECLARATION LOCAL VAR - none

    #BODY - generate the list by input string
    names_list = [name.strip() for name in names_input.split(",")]
    message_list = [message.strip() for message in messages_input.split(",")]
    
    #DECLARATION
    messages: list = []

    #BODY
    for name, message in zip (names_list, message_list):
        messages.append (f"ciao {name}, {message}")

    #RETURN
    return messages
    
#INPUT requests

print (f"inserisci il nome di alcuni tuoi amici")
names_input: str = input()

messages_input: str = input(f"inserisci un messaggio personale per ogni amico separando li da una virgola")

#CALL FUNCTION
res = f_names(names_input, messages_input)    

#EXECUTION
#essendo il return di res una lista io scorro la lista di ritorno
for messaggio in res:
    print (res)




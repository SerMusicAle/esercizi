

#DESCRIPTION FUNCTION
"""
6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""

#FUNCTION
def f_identity ():
    
    #DECLARATION LOCAL VAR
    identity: dict = {}
    
    #BODY - input request
    identity ['first_name'] = input("quale è il nome di battesimo? ")
    identity ['last_name'] = input("quale è il cognome? ")
    identity ['yy'] = input("quale è l'anno di nascita? ")
    identity ['mm'] = input("quale è il mese in cui è nato/a in numeri? ")
    identity ['dd'] = input("quale è il giorno in cui è nato/a ")
    identity ['city'] = input("quale è la città dove è nato/a? ")
    
    #RETURN
    print(f"{identity['first_name']} {identity['last_name']} è nato/a il {identity['dd']}-{identity['mm']}-{identity['yy']} a {identity['city']}")



#CALL FUNCTION
f_identity()













#DESCRIPTION FUNCTION
"""
    3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
"""
 

#FUNCTION
def list3group ():
    
    #DECLARATION LOCAL VARù
    quantity = int(input(f"quante persone vuoi invitare a cena? Almeno 3. "))
    inv_list: list = []
    
    #BODY - input request
    for _ in range (quantity):
        name = input (f"inserisci il nome di un invitato")
        inv_list.append(name)
        
    for name in inv_list:
        print (f"ciao {name}, sei invitato a cena")

#CALL FUNCTION
list3group()










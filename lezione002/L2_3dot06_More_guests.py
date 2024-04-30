#DESCRIPTION FUNCTION
"""
    3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
    • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
    • Use insert() to add one new guest to the beginning of your list.
    • Use insert() to add one new guest to the middle of your list.
    • Use append() to add one new guest to the end of your list.
    • Print a new set of invitation messages, one for each person in your list.
"""

#FUNCTION
def f_addnew ():

    #DECLARATION LOCAL VAR - peolpe invited
    invites: list = ["mario", "luigi", "daisy"]

    #INPUT requests
    #ask user new names
    print (f"abbiamo trovato un tavolo più grande. invito altre 3 persone")
    invited_n1 = input(f"inserisci un nuovo ospite") 
    invited_n2 = input(f"inserisci un nuovo ospite")
    invited_n3 = input(f"inserisci un nuovo ospite")

    #BODY - insert last position
    invites.append(invited_n3)
    
    #insert middle position
    middle_position = len(invites)//2
    invites.insert(middle_position, invited_n2)
    
    #insert first position
    invites.insert(0, invited_n1)
    #RETURN

    #print new invites
    print(f"la nuova lista ospiti è")
    for i in invites:
        print(f"mio caro {i}, sei invitato a cena")


#CALL FUNCTION
f_addnew()







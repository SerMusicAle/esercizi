#DESCRIPTION FUNCTION
"""
    3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
    • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
    • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
    • Print a second set of invitation messages, one for each person who is still in your list.
"""

#FUNCTION
def changes ():

#DECLARATION LOCAL VAR - peolpe invited
    invites: list = ["mario", "luigi", "daisy"]

#BODY
    #INPUT requests
    #who can't come?
    invite_not = input(f"chi non viene più?")

    #veriry corrispondence and change invite
    if invite_not in invites:
        invite_new = input (f"chi è il nuovo ospite?")
        invite_id = invites.index(invite_not)
        invites[invite_id] = invite_new
    print (f"la nuova lista di inviti è")
    
    #stampo la nuova lista ospiti
    for guest in invites:
        print (f"ciao {guest}, sei invitato a cena")

#CALL FUNCTION
changes()







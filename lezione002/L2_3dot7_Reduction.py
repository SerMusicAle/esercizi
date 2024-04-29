#DESCRIPTION FUNCTION
"""
    3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
    • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
    • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
    • Print a message to each of the two people still on your list, letting them know they’re still invited.
    • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
"""
#FUNCTION
def reduction ():

    #DECLARATION LOCAL VAR - peolpe invited
    invites: list = ["mario", "luigi", "daisy", "marco"]

    #BODY - insert last position
    print(f"possiamo invitare solo due persone.... quindi invitiamo")
    while len(invites)>2:
        removed_guest = invites.pop()
        print(f"mi dispiace {removed_guest}, ma non puoi venire")
    
   
    #RETURN
    #print new invites
    print(f"la nuova lista ospiti è")
    for name in invites:
        print (f"{name} è invitato a cena")    
    
    #empty list
    del invites[:]
    print(f"la lista ora dovrebbe essere vuota")

#CALL FUNCTION
reduction()
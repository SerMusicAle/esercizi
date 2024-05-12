"""
        3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
    • Store the locations in a list. Make sure the list is not in alphabetical order.
    • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
    • Use sorted() to print your list in alphabetical order without modifying the actual list.
    • Show that your list is still in its original order by printing it.
    • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
    • Show that your list is still in its original order by printing it again.
    • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
    • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
    • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
    • Use sort() to change your list so it’s stored in reverse-alphabetical order.
    Print the list to show that its order has changed.
"""
def f_places (places):
    print(f"la lista originale è {places}")
    
    #verifico se la lista è ordinata alfabeticamente
    for i in range (len (places)-1):
        if places[i] < places[i+1]:
            print(f"la lista è ordinata alfabeticamente")
        else: 
            print(f"la lista non è ordinata alfabeticamente")

    #stampa lista originale e in ordine inverso
    print(f" l'ordine della lista originale è: ")
    for i in places:
        print(i)
    places2 = places[::-1]
    print(f"il nuovo ordine della lista è inverso: ")
    for i in places2:
        print(i)        
    places.sort()
    places3 = places[::-1]
    print(f"l'ordine della lista originale era: ")
    for i in places3:
        print(i)

f_places (["roma", "londra", "madrid", "parigi", "lisbona"])


"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.
"""
ospiti: list = (["marco", "luigi", "mario"])

def len_ospiti(ospiti):
    
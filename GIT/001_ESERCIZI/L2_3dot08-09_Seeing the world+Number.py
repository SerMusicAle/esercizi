#DESCRIPTION FUNCTION
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

#FUNCTION
def travel ():
    while True:
        try:
            #DECLARATION LOCAL VAR
            quantity = int(input(f"Quanti luoghi vorresti visitare? dimmene almeno 5:"))
            if quantity<5:
                print("devi inserire almeno 5 luoghi")
            else:
                places = []

                for i in range (quantity):
                    place = input (f"dimmi il nome del {i+1}° luogo ")
                    places.append(place)
                #BODY
                print(f"la lista in posizione originale è {places} ")
                #stampa ordinata
                sorted_p = sorted(places)
                print(f"la lista in posizione ordinata alfabeticamente è {sorted_p}")
                
                #stampa originale
                print(f"la lista in posizione originale è {places} ")
                
                #stampa in ordine inverso
                reversed = sorted(places, reverse = True)
                print ("Lista in ordine alfabetico inverso: ")
                for place in reversed:
                    print(place)

                #al termine esce dal ciclo
                break
        except ValueError:
            print (f"inserisci un intero valido")

#CALL FUNCTION
travel()

#EXTERNAL CALL
if __name__ == "__main__":
    travel ()


def number ():
    
    #DECLARATION LOCAL VAR
    places = travel()
    number = len(places)
    
    #BODY
    print (f"ci sono {number} luoghi nella tua lista.")
    
#CALL FUNCTION
number()
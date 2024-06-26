#DESCRIPTION FUNCTION
"""
    4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
    • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
    • Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
    • Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
"""

#FUNCTION

def f_slices():

    #DECLARATION LOCAL VAR
    numeri:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    #BODY
    # print full list
    print("Lista completa:")
    print(numeri)

    # print all elements
    print("\nElementi della lista:")
    for item in numeri:
        print(item)

    # print element from 1 to 3, 3 in the center, the last 3
    print("\nI primi tre elementi della lista sono:")
    print(numeri[:3])

    print("\nTre elementi dal centro della lista sono:")
    middle_start = len(numeri) // 2 - 1
    middle_end = middle_start + 3
    print(numeri[middle_start:middle_end])

    print("\nGli ultimi tre elementi della lista sono:")
    print(numeri[-3:])

#CALL FUNCTION
f_slices()

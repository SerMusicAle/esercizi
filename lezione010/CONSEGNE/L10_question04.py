"""
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51


"""

def f_print_seq(): 
    
#INPUT
    dizionario = {
    'a': [1, 2, 3, 4, 5, 6, 7],
    'b': [3, 8, 13, 18, 23],
    'c': [20, 14, 8, 2, -4, -10],
    'd': [19, 27, 35, 43, 51]
    }

#BODY
    print("Sequenza a):")
    
    for i in  dizionario['a']:
        print (i)

    print("Sequenza b):")

    for i in  dizionario['b']:
        print (i)

    print("Sequenza c):")

    for i in  dizionario['c']:
        print (i)

    print("Sequenza d):")

    for i in  dizionario['d']:
        print (i)

#RETURN
    return

#CALL
f_print_seq()
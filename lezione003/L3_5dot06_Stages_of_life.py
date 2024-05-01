#DESCRIPTION FUNCTION
"""
    5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
    • If the person is less than 2 years old, print a message that the person is a baby.
    • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
    • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
    • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
    • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
    • If the person is age 65 or older, print a message that the person is an elder.
"""


#FUNCTION
def f_stadi_della_vita():
    
    #DECLARATION LOCAL VAR
    #INPUT requests
    età = int(input(f"quanti anni hai? "))
    
    #BODY   
    if età < 2:
        print("La persona è un bambino.")
    elif età < 2:
        print("La persona è un bambino.")
    elif età < 4:
        print("La persona è un bambino piccolo.")
    elif età < 13:
        print("La persona è un bambino.")
    elif età < 20:
        print("La persona è un adolescente.")
    elif età < 65:
        print("La persona è un adulto.")
    else:
        print("La persona è un anziano.")

#CALL
f_stadi_della_vita()
#DESCRIPTION FUNCTION
"""
    8-3. T-Shirt: Write a function called make_shirt() that accepts a size
     and the text of a message that should be printed on the shirt. 
     The function should print a sentence summarizing the size of the 
     shirt and the message printed on it. Call the function once using 
     positional arguments to make a shirt. Call the function a second time
     using keyword arguments.
"""

#FUNCTION
# create a t-shirt
def f_make_shirt(size, message):

    #BODY
    print(f"Creo una maglietta di taglia {size} con il messaggio: {message}")

#CALL FUNCTION
f_make_shirt("L", "Python è fantastico!")

#CALL FUNCTION 2
f_make_shirt(size="M", message="I love coding!")
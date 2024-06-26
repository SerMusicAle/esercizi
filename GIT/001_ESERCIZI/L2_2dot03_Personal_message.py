"""
    2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
def f_message(name):
    #costruct the string to return using an f-string
    message = (f"ciao {name}")
    return message

#which name you choise?
name: str = "Alessandro"
#creat the var contains the function
res = f_message(name)
print (res)

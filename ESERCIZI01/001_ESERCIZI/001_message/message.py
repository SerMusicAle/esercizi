"""
    2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
class Message ():
#INIT
    def __init__(self, name:str):
        self.__name = name
        
    def f_message(self):
        #costruct the string to return using an f-string
        message = (f"ciao {self.__name}")
        return message


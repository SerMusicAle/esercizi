"""
    2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
import unittest

class Message ():
#INIT
    def __init__(self, name:str):
        self.__name = name
#BODY        
    def f_message(self):
        #costruct the string to return using an f-string
        self.message = f"ciao {self.__name}"
        return self.message


class TestMessage(unittest.TestCase):
#SETUP
    def setUp(self):
        self.name: str = "Alessandro"
        self.message = Message (self.name)
    
    def test_f_message(self):
        expected_message = "ciao Alessandro"
        product_message = self.message.f_message()
        self.assertEqual(product_message, expected_message, "return non corrispondente")

#RUN
if __name__ == '__main__':
    unittest.main()
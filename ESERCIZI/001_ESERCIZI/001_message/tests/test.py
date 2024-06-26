#TEST
import unittest
from message import Message

#TEST MESSAGE        
class TestMessage(unittest.TestCase):
#SETUP
    def setUp(self):
        self.name: str = "Alessandro"
        self.message = Message (self.name)
    
    def test_f_message(self):
        expected_message = "ciao Alessandro"
        product_message = self.message.f_message()
        self.assertEqual(product_message, expected_message, "return messaggio non corrispondente")

#RUN
if __name__ == '__main__':
    unittest.main()
        
    
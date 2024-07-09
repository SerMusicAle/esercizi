import unittest
from restaurant import Restaurant

class TestRestaurant (unittest.TestCase):
#SETUP
    def setUp (self):
        self.oggetto = Restaurant ("Bella Zi", "Cucina romana", True)
#BODY
    def test_f_describe_restaurant (self):
        expected = ("Bella Zi", "Cucina romana")
        returned = self.oggetto.f_describe_restaurant()
        self.assertEqual (returned, expected, "ERR. F_DESCRIBE - nome e descrizione non corrispondono")
        
    def test_f_open_restaurant (self):
        expected = "il ristorante è aperto"
        returned = self.oggetto.open_restaurant()
        self.assertEqual (returned, expected, "ERR. F_OPEM_RESTAURANT - lo stato di apertura del ristorante non corrisponde")
        


gelateria = Restaurant.IceCreamStand ("mondo gelo", "gelati vegani", ["cioccolato", "crema", "pistacchio"])

gelateria.display_flavors()


#RUN
if __name__ == '__main__':
    unittest.main()   
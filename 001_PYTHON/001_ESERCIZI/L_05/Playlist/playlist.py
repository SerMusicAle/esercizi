"""
1. Create a Playlist:

    function create_playlist(playlist name and a variable number of song titles):
        return a dictionary with the playlist name and a set of songs. 
        Call the function with different numbers of songs to demonstrate flexibility.
        Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

    function add_like(dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False).)   
        This function should return an updated dictionary.
        Example: add_like(dictionary, “Road Trip”, liked=True)    
"""
import unittest

class Playlist():
#INIT
    def __init__(self, name:str, songs:set[str], vote:bool):
        self.__name = name
        self.__songs = songs
        self.__vote = vote
        self.__playlist:dict[str, set[str]] = {}
        self.__liked:dict[str, bool] = {}
        
#BODY
    def f_create_playlist(self):
        self.__playlist[self.__name] = self.__songs
        return self.__playlist    
    
    def f_add_like(self):
        self.__liked [self.__name] = self.__vote
        return self.__liked

#TEST
class TestPlaylist(unittest.TestCase):
#SETUP
    def setUp(self):
        self.__name_italian:str = "musica italiana"
        self.__italian_list:set[str] = {"ti innamorerai", "baciami bambina", "l'aurora"}
        self.__name_english:str = "english music"
        self.__english_list:set[str] = {"your song", "wherever you will go", "omg"}
        self.__vote1: bool = True
        self.__vote2: bool = False
    
        self.__oggetto = Playlist (self.__name_italian, self.__italian_list, self.__vote1)
        self.__oggetto2 = Playlist (self.__name_english, self.__english_list, self.__vote2)

    def test_f_create_playlist(self):
        returned1 = self.__oggetto.f_create_playlist()
        returned2 = self.__oggetto2.f_create_playlist()
        
        self.assertEqual (returned1, {self.__name_italian : self.__italian_list})
        self.assertEqual (returned2, {self.__name_english : self.__english_list})
        
    def test_f_add_like(self):
        returned1 = self.__oggetto.f_add_like()
        returned2 = self.__oggetto2.f_add_like()
        
        self.assertEqual (returned1, {self.__name_italian : self.__vote1})
        self.assertEqual (returned2, {self.__name_english : self.__vote2})
    
if __name__ == "__main__":
    unittest.main()

#DESCRIPTION FUNCTION
"""
3-1. Nomi:
    Memorizza i nomi di alcuni dei tuoi amici in una lista chiamata nomi. 
    Stampa il nome di ciascuna persona accedendo a ogni elemento della lista, uno alla volta.
"""


class Names():
#INIT
    def __init__ (self, nomi: list[str]):
        self.nomi = nomi
    
    def f_names (self):
        #DECLARATION LOCAL VAR - none
        return self.nomi


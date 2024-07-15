
class NameCases ():
#INIT
    def __init__(self, name:str):
        self.__name = name
        
#BODY       
    #function prints some character version of the name
    def f_name_cases(self):
        
        #print the name in uppercase
        self.__uppertext = self.__name.upper()
        #print the name in lowercase
        self.__lowertext = self.__name.lower()
        #print the name  in title case
        self.__titletext = self.__name.title()
        #print the name with the first letter capitalized
        self.__capitalizedtext = self.__name.capitalize()
        #print the name with uppercase letters converted to lowercase and vice versa
        self.__swapcasetext = self.__name.swapcase()

        #export the phrases
        list_name : list [str] = [
            self.__uppertext, 
            self.__lowertext, 
            self.__titletext, 
            self.__capitalizedtext, 
            self.__swapcasetext
            ]

        return list_name

#DESCRIPTION FUNCTION
"""
2-8. File Extensions: 
    Python has a removesuffix() method that works exactly like removeprefix(). 
    Assign the value 'python_notes.txt' to a variable called filename. 
    Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""

class Extension ():
#INIT
    def __init__(self, file_name:str):
        self.__file_name = file_name
        
#BODY
    def f_no_extension (self):
        #DECLARATION LOCAL VAR
        file_name_no_ext = self.__file_name.removesuffix(".txt")
        return file_name_no_ext
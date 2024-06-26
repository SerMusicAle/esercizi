#DESCRIPTION FUNCTION
"""
    2-8. File Extensions: 
    Python has a removesuffix() method that works exactly like removeprefix(). 
    Assign the value 'python_notes.txt' to a variable called filename. 
    Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""
#FUNCTION
def f_no_extension (file_name):
    #DECLARATION LOCAL VAR
    file_name = file_name.removesuffix(".txt")

#INPUT requests
file_name: str = input()
#CALL
res = (f_no_extension(file_name))

#EXECUTION
print (res)







#ASSIGNMENTS


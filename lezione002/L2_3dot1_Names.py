
#DESCRIPTION FUNCTION
"""
    3-1. Names: 
    Store the names of a few of your friends in a list called names. 
    Print each person’s name by accessing each element in the list, one at a time.
"""
#FUNCTION
def f_names (names_list):
    #DECLARATION LOCAL VAR - none
    for name in names_list:
        print (name)

#INPUT requests
print (f"inserisci il nome di alcuni tuoi amici")
names: list = input()

#generate the list by input string
names_list = [names.strip() for name in names.split(",")]

#CALL
res = f_names(names_list)    

#EXECUTION
print (res)







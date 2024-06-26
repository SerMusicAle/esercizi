
"""
    2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
"""
#function prints some character version of the name
def f_name_cases(name):
    
    #print the name in uppercase
    print (name.upper())
    #print the name in lowercase
    print (name.lower())
    #print the name  in title case
    print (name.title())

    #extra

    #print the name with the first letter capitalized
    print (name.capitalize())
    #print the name with uppercase letters converted to lowercase and vice versa
    print (name.swapcase())

    #export the phrases
    list_name : list = [
        name.upper(), 
        name.lower(), 
        name.title(), 
        name.capitalize(), 
        name.swapcase()
        ]

    return list_name
#assign the person's name to print
name: str = "Alessandro"

#call the function to display name cases
res = f_name_cases(name)
print (res)


"""
this function doesn't have a var returned called response cause it print some messages directly 
and the stamps don't included in var to recall 
"""
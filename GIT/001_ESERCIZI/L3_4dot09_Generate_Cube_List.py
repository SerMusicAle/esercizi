#DESCRIPTION FUNCTION
"""
    4-9. Cube Comprehension: Use a list comprehension to generate a list
    of the first 10 cubes.
"""

#FUNCTION
def f_generate_cube_list():

    #BODY
    # use a comprehension list to generate a lsit of 10 cubes
    cubes = [num ** 3 for num in range(1, 11)]
    
    #RETURN
    return cubes

#CALL FUNCTION
cubes_list = f_generate_cube_list()

#EXECUTION
print(cubes_list)

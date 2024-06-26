#DESCRIPTION FUNCTION
"""
    4-7. Threes: Make a list of the multiples of 3, from 3 to 30. 
    Use a for loop to print the numbers in your list.

"""

#FUNCTION
def f_multiples_of_three():

    # creat a list
    multipli: list = []

    # find multilples
    for num in range(3, 31, 3):
        multipli.append(num)

    # print multiples
    for num in multipli:
        print(num)

#CALL FUNCTION
f_multiples_of_three()
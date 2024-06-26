#DESCRIPTION FUNCTION
"""
    4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
"""

# FUNCTION
def f_odd_numbers():
    # DECLARATION
    odd_list: list = []

    
    # BODY
    # create a range with a step of 2
    for num in range(1, 21, 2):  
        odd_list.append(num)

    # Print odd numbers
    for num in odd_list:
        print(num)

# CALL FUNCTION
f_odd_numbers()
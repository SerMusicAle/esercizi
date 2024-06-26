#DESCRIPTION 
"""
    5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
    ate to 10. If you want to try more comparisons, write more tests and add them

    to conditional_tests.py. Have at least one True and one False result for each of
    the following:
    • Tests for equality and inequality with strings
    • Tests using the lower() method
    • Numerical tests involving equality and inequality, greater than and less
    than, greater than or equal to, and less than or equal to
    • Tests using the and keyword and the or keyword
    • Test whether an item is in a list
    • Test whether an item is not in a list
"""

# Test 1 with strings eguals diseguals
name = "John"
print(name == "John")  # True
print(name != "Mary")  # True

# Test 2 with lower() method
name1 = "John"
name2 = "john"
print(name1.lower() == name2.lower())  # True

# Test 3 numeric
num1 = 10
num2 = 5
print(num1 > num2)      # True
print(num1 <= num2)     # False

# Test 4 eith and e or
age = 25
print(age > 18 and age < 30)  # True
print(age < 18 or age > 30)    # False

# Test 5 if is in list
fruits = ['apple', 'banana', 'orange']
print('banana' in fruits)  # True

# Test 6 if is not in list
print('grape' not in fruits)  # True

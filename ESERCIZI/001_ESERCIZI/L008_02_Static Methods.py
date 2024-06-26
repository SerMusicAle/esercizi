"""
Implementing Static Methods
Create a class MathOperations with a static method add 
that takes two numbers and returns their sum, 
and another static method multiply 
that takes two numbers and returns their product.

"""

class MathOperation:

#BODY      
    @staticmethod
    def add(a:int, b:int):
        sum = a + b
        return sum
    
    @staticmethod
    def multiply(a:int, b:int):
        multi = a * b
        return multi
        
    
    #TEST
somma = MathOperation.add(3, 5)
promultidotto = MathOperation.multiply(3, 5)

print(f"La somma di 3 e 5 è: {somma}")
print(f"Il prodotto di 3 e 5 è: {promultidotto}")
"""
classe Perone
    persona nome età cf
    student
classe animale specie età
    gatto specie età
    coniglio specie età


"""

class Living:

    #DEC
    def __init__(self, name:str, age:int,species:str) -> None:
        self.nome = name
        self.specie = species
    
class Humans(Living):
    
    #DEC
    def __init__(self, name:str, age:int, species:str, cf:str):
        super().__init__ (name, age, species)
        self.cf = cf

    #RETURN
    def __str__ (self):
        return f"{self.__class__.__name__}"

class Animals(Living):
    
    #DEC
    def __init__(self, species:str, pedigree:float):
        super().__init__ (species)

class Student(Humans):
    
    #DEC
    def __init__(self, name:str, age:int):
        super().__init__ (name, age)

class Cats(Animals):
    
    #DEC
    def __init__ (self, name:str, age:int, pedigree:float):
        super ().__init__ (name, age, pedigree)

class Rabbit(Animals):

    #DEC
    def __init__ (self, name:str, age:int, pedigree:float):
        super ().__init__ (name, age, pedigree)


"""
class Living:
    # Constructor
    def __init__(self, name: str, age: int, species: str) -> None:
        self.name = name
        self.age = age
        self.species = species

class Humans(Living):
    # Constructor
    def __init__(self, name: str, age: int, species: str, cf: str):
        super().__init__(name, age, species)
        self.cf = cf

    # String representation
    def __str__(self):
        return f"{self.__class__.__name__}"

class Animals(Living):
    # Constructor
    def __init__(self, name: str, age: int, species: str, pedigree: float):
        super().__init__(name, age, species)
        self.pedigree = pedigree

class Student(Humans):
    # Constructor
    def __init__(self, name: str, age: int, species: str, cf: str):
        super().__init__(name, age, species, cf)

class Cats(Animals):
    # Constructor
    def __init__(self, name: str, age: int, species: str, pedigree: float):
        super().__init__(name, age, species, pedigree)

class Rabbit(Animals):
    # Constructor
    def __init__(self, name: str, age: int, species: str, pedigree: float):
        super().__init__(name, age, species, pedigree)

# Creating instances
human = Humans(name="Alice", age=30, species="Homo Sapiens", cf="ABC123")
student = Student(name="Bob", age=20, species="Homo Sapiens", cf="DEF456")
cat = Cats(name="Whiskers", age=3, species="Felis Catus", pedigree=4.5)
rabbit = Rabbit(name="Thumper", age=2, species="Oryctolagus Cuniculus", pedigree=3.2)

# Printing class names, species, parameters, and attributes
print(f"Class: {human.__class__.__name__}, Species: {human.species}, Name: {human.name}, Age: {human.age}, CF: {human.cf}")
print(f"Class: {student.__class__.__name__}, Species: {student.species}, Name: {student.name}, Age: {student.age}, CF: {student.cf}")
print(f"Class: {cat.__class__.__name__}, Species: {cat.species}, Name: {cat.name}, Age: {cat.age}, Pedigree: {cat.pedigree}")
print(f"Class: {rabbit.__class__.__name__}, Species: {rabbit.species}, Name: {rabbit.name}, Age: {rabbit.age}, Pedigree: {rabbit.pedigree}")

"""
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



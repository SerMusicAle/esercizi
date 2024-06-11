
# Definizione delle classi base
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student:
    def __init__(self, student_id, courses):
        self.student_id = student_id
        self.courses = courses

    def get_courses(self):
        return f"Student ID: {self.student_id}, Courses: {', '.join(self.courses)}"

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def get_position(self):
        return f"Employee ID: {self.employee_id}, Position: {self.position}"

# Definizione della classe derivata che eredita da tutte e tre le classi base
class WorkingStudent(Person, Student, Employee):
    def __init__(self, name, age, student_id, courses, employee_id, position):
        # Inizializza i costruttori delle classi base
        Person.__init__(self, name, age)
        Student.__init__(self, student_id, courses)
        Employee.__init__(self, employee_id, position)

    def get_full_details(self):
        return f"{self.get_details()}\n{self.get_courses()}\n{self.get_position()}"

# Creazione di un'istanza di WorkingStudent
working_student = WorkingStudent(
    name="Alice",
    age=22,
    student_id="S12345",
    courses=["Math", "Science"],
    employee_id="E54321",
    position="Lab Assistant"
)

# Chiamata dei metodi
print(working_student.get_full_details())

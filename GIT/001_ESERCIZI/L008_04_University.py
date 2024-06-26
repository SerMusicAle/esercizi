"""
Exercise 4: University Management System

Create a system to manage a university with departments, courses, professors, and students. 

Create an abstract class Person:
Attributes:

name (string)
age (int)
Methods:

__init__ method to initialize the attributes.
Abstract method get_role to be implemented by subclasses.
__str__ method to return a string representation of the person.
Create subclasses Student and Professor that inherit from Person and implement the abstract methods:

Student:
Additional attributes: student_id (string), courses (list of Course instances)
Method enroll(course) to enroll the student in a course.
Professor:
Additional attributes: professor_id (string), department (string), courses (list of Course instances)
Method assign_to_course(course) to assign the professor to a course.


Create a class Course:
Attributes:

course_name (string)
course_code (string)
students (list of Student instances)
professor (Professor instance)
Methods:

__init__ method to initialize the attributes.
add_student(student) to add a student to the course.
set_professor(professor) to set the professor for the course.
__str__ method to return a string representation of the course.
Create a class Department:

Attributes:

department_name (string)
courses (list of Course instances)
professors (list of Professor instances)

Methods:

__init__ method to initialize the attributes.
add_course(course) to add a course to the department.
add_professor(professor) to add a professor to the department.
__str__ method to return a string representation of the department.
Create a class University:

Attributes:

name (string)
departments (list of Department instances)
students (list of Student instances)

Methods:

__init__ method to initialize the attributes.
add_department(department) to add a department to the university.
add_student(student) to add a student to the university.
__str__ method to return a string representation of the university.

Create a script:

Create instances of departments, courses, professors, and students.
Add them to the university.
Enroll students in courses and assign professors to courses.
Display the state of the university.

"""


"""
- get role ritorna la stringa ruolo (studente o prof)
- assign to coruse and arroll puntano allo stesso oggetto
- i prof appartengono a dei dipartimenti
- 
"""
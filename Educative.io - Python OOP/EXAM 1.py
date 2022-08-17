'''
EXAM 1 - putting on practice my coding skills
'''

# Examples that have an error
'''
class Student:
    # defining the properties
    ID = None
    GPA = None

# creating an object of the Student class
Peter = Student()

# assigning values to properties of Peter
Peter.ID = 3789
Peter.GPA = 3.5

# create a new attribute for Peter
Peter.department = "Computer Science" # ERROR


# Create another Student object
John = Student()
John.ID = 3790
John.GPA = 3.7


# Printing properties of Peter
print("ID =", Peter.ID)
print("GPA", Peter.GPA)
print("Department:", Peter.department)

# Printing properties of John
print("ID =", John.ID)
print("GPA", John.GPA)
print("Department:", John.department)


class Book:
    def __init__(self, ID, title):
        self.ID = ID
        self.__title = title


harry_potter = Book(3789, 'Harry Potter and the Chamber of Secrets')
print(harry_potter._Book__title)
'''
# EXAM EXERCISES - Educative.io

# Return the area of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def print_area(self):
        a = self.radius
        b = a ** 2
        c = 3.14 * b
        return (print(c))

area = Circle(3)
area.print_area()

# Get and Set exercise with private properties
class User:
    def __init__(self, name, ID, department):
        self.__name = name
        self.__ID = ID
        self.__department = department

    def get_name(self):
        return (self.__name)

    def set_name(self, name):
        self.__name = name

    def get_ID(self):
        return (self.__ID)

    def set_ID(self, ID):
        self.__ID = ID

    def get_department(self):
        return (self.__department)

    def set_department(self, department):
        self.__department = department

new = User('Michael', 2345, 'Human Rerources')
print('USER:', new.get_ID(), new.get_department(), new.get_name())

new.set_name('Fede')
new.set_ID(7986)
new.set_department('A')
print('NEW USER:', new.get_name(), new.get_ID(), new.get_department())

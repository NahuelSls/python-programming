'''
EXAM 2
'''

'''
class Vehicle:
    def displayType(self):
        print("This is a vehicle")

class Car(Vehicle):
    def displayType(self):
        print("This is a car")

class Bus(Vehicle):
    def displayType(self):
        print("This is a bus")


c = Car()
b = Bus()
v = Vehicle()

c.displayType()
b.displayType()
v.displayType()


class A:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, num):
        return A((self.x + num.x) * 2)

    def __sub__(self, num):
        return A((self.x - num.x) * 2)


obj1 = A(3)
obj2 = A(5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("obj.x = ", obj3.x)
print("obj3.y = :", obj3.y)
print("obj4.x = :", obj4.x)
print("obj4.y = ", obj4.y)

# EXAM EXERCISE 1
class Country:
    def __init__(self, name):
        self.name = name

    def print_continent(self):
        print("Something to print")

class India(Country):
    def print_continent(self):
        print ("Asia")

class France(Country):
    def print_continent(self):
        print("Europe")

class Nigeria(Country):
    def print_continent(self):
        print("Africa")

ind = India("name")
print(ind.print_continent())

fr = France("name")
print(fr.print_continent())

nig = Nigeria("")
print(nig.print_continent())


# EXAM EXERCISE 2
class Salary:
    def __init__(self, base_pay=0, bonus=0):
        self.__base_pay = base_pay
        self.__bonus = bonus

    def get_bonus(self):
        return (self.__bonus)

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_base_pay(self):
        return (self.__base_pay)

    def set_base_pay(self, base_pay):
        self.__base_pay = base_pay


class Employee:
    def __init__(self, name = '', base_pay = 0, bonus = 0):
        self.__name = name
        self.__salary = Salary(base_pay, bonus)

    def get_name(self):
        print("Name:", self.__name)
        print("Base pay:", self.__salary.get_base_pay())
        print("Bonus:", self.__salary.get_bonus())
    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return (self.__salary.get_base_pay() + self.__salary.get_bonus())

    def set_salary(self, base_pay, bonus):
        self.__salary.set_base_pay(base_pay)
        self.__salary.set_bonus(bonus)

emplo = Employee("Fede", 2500, 500)
emplo.get_name()

emplo.set_salary(1250, 250)
print("\nNew data:", emplo.get_salary())


'''

#EXAM EXERCISE 3
from abc import ABC, abstractmethod

class Metal(ABC):
    @abstractmethod
    def get_melting_point(self):
        pass

class Aluminium(Metal):
    def __init__(self, mpoint = 660):
        self.mpoint = mpoint
    def get_melting_point(self):
        print("Melting point for Aluminium:", self.mpoint)

class Copper(Metal):
    def __init__(self, mpoint = 1084):
        self.mpoint = mpoint

    def get_melting_point(self):
        print("Melting point for Copper:", self.mpoint)

class Gold(Metal):
    def __init__(self, mpoint = 1063):
        self.mpoint = mpoint

    def get_melting_point(self):
        print("Melting point for Gold:", self.mpoint)

clas = Aluminium()
clas.get_melting_point()

cop = Copper()
cop.get_melting_point()

gol = Gold()
gol.get_melting_point()




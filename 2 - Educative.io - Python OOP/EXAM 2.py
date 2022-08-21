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


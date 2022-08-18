'''
Implement rectangle class using the Encapsulation
'''

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__width * self.__length)

    def perimeter(self):
        return (2 * (self.__width + self.__length))

rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())

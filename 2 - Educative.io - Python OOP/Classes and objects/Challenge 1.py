'''
Square numbers and return their sum
'''

class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x ** 2
        b = self.y ** 2
        c = self.z ** 2
        return (a + b + c)

numbers = Point(2,4, 6)
print(numbers.sqSum())



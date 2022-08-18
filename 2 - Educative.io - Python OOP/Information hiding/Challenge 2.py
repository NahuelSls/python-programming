'''
Implement the complete student class
'''

class Student:
    #__name = None
    #__rollNumber = None

    def __init__(self, name, rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber

    def getName(self):
        return (self.__name)

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return (self.__rollNumber)

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

name = Student('Alex', 3789)
print('Name:', name.getName(), 'and Roll Number:', name.getRollNumber())

name.setName('Victor')
name.setRollNumber(1234)

print('Name:', name.getName(), 'and Roll Number:', name.getRollNumber())
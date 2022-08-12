'''
Trying to understand the class options with an example proposed by Educative.io
'''

Samuel = ["FF", 1250, 2500, 25]
Jackson = ["Doc", 2345, 2340, 20]

class Employee():
    def __init__(self):
        self.Job = ""
        self.ID = 0
        self.Salary = 0
        self.Old = 0

def prog(Emply):
    a = Employee()
    a.Job = Emply[0]
    a.ID = Emply[1]
    a.Salary = Emply[2]
    a.Old = Emply[3]
    return a

First = prog(Samuel)
Second = prog(Jackson)

print('pF SKLFCLKS:', First.Job)
print('pF SKLFCLKS:', First.ID)
print('pF SKLFCLKS:', First.Salary)
print('qwert:', First.Old)

print('\npF SKLFCLKS:', Second.Job)
print('pF SKLFCLKS:', Second.ID)
print('pF SKLFCLKS:', Second.Salary)
print('andbsms:', Second.Old)


class Job():
    First = [Samuel, 1234, 2500]
    def __init__(self, name, ID, Salary):
        self.name = name
        self.ID = ID
        self.Salary = Salary

    @classmethod
    def method(cls):
        return cls.First

    @staticmethod
    def static():
        print('Static method.')

Second = Job('Kerry', 2543, 2250)
Second.static()
Job.static()
print('Class method:', Job.method())

'''
Calculate the student's performance
'''

class Student():
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        s = self.name
        a = self.phy
        b = self.chem
        c = self.bio
        return s, (a + b + c)

    def percentage(self):
        s = self.name
        a = self.phy
        b = self.chem
        c = self.bio
        return s, ((a + b + c)/300 * 100)


    def total0bt(self):
        return (self.phy + self.chem + self.bio)

    def percetage(self):
        return self.name, (self.total0bt() / 300 * 100)

total = Student('Mark', 80, 90, 40)
print('YOUR MARKS:', total.totalObtained())
print('YOUR TOTAL MARK:', total.percentage())

print('MARKS:', total.total0bt())
print('TOTAL MARK:', total.percetage())
'''
Examples for the quiz
'''

class Parent:
    def prn(self):
        return (print("parent"))


class Child(Parent):
    def __init__(self):
        self.a = Parent()


    def prn(self):
        return (print("child"))

temp = Child()

temp.a.prn()
temp.prn()
'''
Implement an Animal Class
'''

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("\nName:", self.name)
        print("Sound:", self.sound)
        #return (self.name + ", " + self.sound)

class Dog(Animal):
    def __init__(self, name, sound, family):
        self.family = family
        super().__init__(name, sound)

    def Animal_details(self):
        super().Animal_details()
        print("Family:", self.family)
        #return print(super().Animal_details() + ", " + self.family)

class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print("Color:", self.color)

'''      
    def Animal_details(self):
        return print(super().Animal_details() + ", " + self.color)
'''

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()

c = Sheep("Billy", "Baaa Baaa", "White")
c.Animal_details()
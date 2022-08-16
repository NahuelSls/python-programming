'''
Implement a calculator class
'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)

    def subtract(self):
        return (self.num1 - self.num2)

    def multiply(self):
        return (self.num1 * self.num2)

    def divide(self):
        return (self.num1 / self.num2)

number = Calculator(int(input('Write a number: ')), int(input('Write another number: ')))

print('\nAdd:', number.add(),
      '\nSubtract:', number.subtract(),
      '\nMultiply:', number.multiply(),
      '\nDivide: ', number.divide())



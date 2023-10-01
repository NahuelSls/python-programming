'''
Element of Python:
    An explanation of the most important parts for Python like the reserved words that it can't be used for the variables or
    how we can work in different ways with the same number that it can be introduced for the user.
'''

#'float' for decimals and 'int' for integer numbers
number = float(input('Write a number: '))
#number = int(input('Write a number:'))

#Sequential steps
x = number
print('\nYour number: ', x)
x = x + 2
print('Your number + 2: ', x)

#Conditional steps
if number < 5:
    print(number, 'is smaller than 5')
if number > 10:
    print(number, 'is bigger than 10')

print('Finish\n')

#Repeated steps
while number >= 0:
    print('number: ', number)
    number = number - 1
print('\nFINISH.')

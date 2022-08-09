#Elements of python, a summary of the most important part for python like the reserved words or the python scripts

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
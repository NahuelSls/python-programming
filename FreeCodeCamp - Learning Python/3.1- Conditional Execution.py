'''
An explanation about the if conditions, comparison operators, indentation.
'''

# Greater or less than another number
user_number = int(input('Please, introduce a number: '))
number = int(input('Introduce another number: '))

if user_number:
    print('Your number is:', user_number)
    if user_number >= number:
        print('Your number is greater than', number)

    else:
        print('Your number is less than', number)

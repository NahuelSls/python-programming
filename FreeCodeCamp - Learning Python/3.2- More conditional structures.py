'''
This part explains how it works the elif conditions, try/except structure to compensate errors,...
'''

user_number = input('Introduce a number: ')

try:
    number = float(user_number)

except:
    number = -1

if number >= 10:
    print('Your number is greater than 10.')

elif 5 <= number < 10:
    print('Your number is between 5 and 10')

else:
    print('Not a number')


# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours
# worked above 40 hours.
print('\nEXERCISE 1:')
hours = int(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    print('More than 40 hours.')
    extra_hours = hours - 40
    regular = (hours - extra_hours) * rate
    pay = regular + extra_hours * rate * 1.5
    print('Pay: ', pay)

else:
    print('Regular time.')
    pay = hours * rate
    print('Pay: ', pay)

# Exercise 2: Rewrite your program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program.
print('\nEXERCISE 2:')
user_hours = input('Enter Hours: ')
user_rate = input('Enter Rater: ')

try:
    new_hour = int(user_hours);
    new_rate = float(user_rate);

    if (new_hour > 40):
        print('More than 40 hours.')
        extra_hour = new_hour - 40
        regular = (new_hour - extra_hour) * new_rate
        new_pay = regular + extra_hour * new_rate * 1.5
        print('Pay: ', new_pay)

    else:
        print('Regular time.')
        new_pay = new_hour * new_rate
        print('Pay: ', new_pay)

except:
    print("Error, please enter numeric input")




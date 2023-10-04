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
hours = int(input('\nEnter Hours: '))
rate = float(input('Enter Rater: '))

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



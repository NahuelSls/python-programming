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
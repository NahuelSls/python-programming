'''
In general, expands the information about expressions adding important things about 'input' command or how we can make comments
in Python using #.
We can see that there are more operators that we can use in Python without external libraries or how we can work with
strings and integers at the same time.

For example, using 'input' the user can introduce some numbers that the program will recognise like an string but in another
line we can convert the same string number introduced by the user into an integer.
That means that we can make operations with this changes and print the result as a nunmber at the output.

Something that we can't do is to convert some letters into an integer because we can't add numbers to letters.

An extra for this part of the course, there are an order evalutation whose name is "operator precedence".
That means that some operator are going to be calculated before another, the highest precedence rule to the lowest.
For example: parenthesis >> power or multiplication
'''

#An example of how we can use 'input' command for interact with the user
name = input('What is your name? ')
age = input('How old are you? ')

print('Your name is', name)
print('Your age is', age)

#Numbers introduced like text and converted into an integer for making the operation
random = int('234')
waste = random + 1
print('\nrandom number + 1:', waste)

#Little examples with some operators that we can use without libraries
aa = 25
bb = 10
cc = 2
zz = aa * bb
xx = aa / cc
yy = aa + bb ** cc / (cc - 3 ** bb)

print('\nFirst result:', zz)
print('Second result:', xx)
print('Third result:', yy)

#Extra exercises for this part of the lesson
name_2 = input('\nEnter your name: ')
print('Hello', name_2)

hours = int(input('\nEnter Hours: '))
rate = float(input('Enter Rater:'))
pay = hours * rate
print('Pay:', pay)


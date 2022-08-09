'''
Remembering the reserved words in Python that can't be used like a variable and an introduction of how we can work with
variables.
There are some rules for this variables because we can't do something like "Your.name" instead of "Your_name".

Another thing that we can learn here is how to use some mathematical expression or the assignment statement. Some basic
information that is going to be expanded in the future.
'''

#Variables: how to store some data in a named place
x = 24
Number = 12
Your_name = 'Arturito'

print(x)
print(Number)
print(Your_name + '\n')

#How completely different variables can mean the same
print("Different variables but the same results:")
p1e3p6it90 = 25
p2e23pit0 = 2
art12uri4to = p1e3p6it90 * p2e23pit0
print('Variable 1:', art12uri4to)

a = 25
b = 2
c = a * b
print('Variable 2:', c)

price = 25
day = 2
total = price * day
print('Variable 3:', total)

#Expressions and assignment statements
#We can update the value stored in a variable with a new value using expressions or changing the value in other line
x = 25
print('\nValue for the variable x =', x)

x = 3 * x * (x - 10)
print('New value for the same variable x =', x)





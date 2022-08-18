'''
Two exercises that put our knowledge of functions
'''

#Two integer number, x must repeat X times and y must repeat Y times
def repetition(x, y):
    return str(x) * 3 + str(y) * 2

print(repetition(input('Write x: '), input('Write y: ')))

#Use the factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return -1
    else:
        return n * factorial(n - 1)

print(factorial(int(input('Introduce a number: '))))




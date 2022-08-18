'''
Some exercises related with loops.
'''

#A code that return true or false if 'sum1 + sum2 = 0'
num_list = [10, -14, 26, 5, -3, 13, -5]
sum  = False

for sum1 in num_list:
    for sum2 in num_list:
        if sum1 + sum2 == 0:
            sum = True
            break
    if sum:
        break

print('Suma = 0: ', sum)

#Same exercise but using functions
def check_num(num_list):
    for first in range(len(num_list)):
        for second in range(first + 1, len(num_list)):
            if num_list[first] + num_list[second] == 0:
                return True
    return False

print('Sum = 0:', check_num(num_list))

#Check if there are the same number of brackets or not.
def check_brack(brackets):
    check = 0
    for bracket in brackets:
        if bracket == '[':
            check = check + 1
        elif bracket == ']':
            check = check - 1
        elif check < 0:
            break

    return check == 0

bracket_ = input('\nWrite some brackets: ')
print('Same number of brackets:', check_brack(bracket_))

#Fibonacci number: 0 1 1 2 3 5 8 13 ... I want to know the Fibonacci number for the position introduced by the user.
def fibonacci_num(number):
    first_num = 0
    second_num = 1

    if number < 1:
        return -1
    elif number == 1:
        return first_num
    elif number == 2:
        return second_num

    count = 3
    while count <= number:
        fibona_num = first_num + second_num
        first_num = second_num
        second_num = fibona_num
        #count = count + 1
        count += 1
    return fibona_num

numb = int(input('\nIntroduce a number: '))

print('Results:', fibonacci_num(numb))










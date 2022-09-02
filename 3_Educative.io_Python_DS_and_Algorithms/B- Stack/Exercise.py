'''
Convert Decimal Integer to Binary
'''
from Stack import Stack

def convert_int_to_bin(dec_num):

    # if the dec_num is 0 then the pogram will end with a 0
    if dec_num == 0:
        return 0

    # an object for the Stack class
    s = Stack()

    # while the dec_num > 0 the program will work with the number in a loop
    while dec_num > 0:
        remainder = dec_num % 2 # we save the 0 or 1 value on remainder
        s.push(remainder)   # we push this value to an empty stack
        dec_num = dec_num // 2  # the current dec_num is divided by 2 each time

    bin_num = ""    # we create an empty reversed string
    while not s.is_empty(): # this loop will work until the stack is empty
        bin_num += str(s.pop()) # bin_num will save the value of the popped elements for the binary num

    return bin_num  # return this value

# some examples to know if this program works
print(convert_int_to_bin(56))   # 111000
print(convert_int_to_bin(2))    # 10
print(convert_int_to_bin(32))   # 100000
print(convert_int_to_bin(10))   # 1010

# it prints True or False if the left number is equal to the right
print(int(convert_int_to_bin(56), 2) == 56) # True

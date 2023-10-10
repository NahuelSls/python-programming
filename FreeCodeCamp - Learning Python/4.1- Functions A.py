'''
An introduction about functions and max/min.
'''

def Something(a, b, c, d):
    print('Something function')
    sum = a**2 - b * c + d**3 # sum = 114
    big_letter = max('max number') # big_letter = 'x'

    return sum, big_letter

def Nothing(a, b, c, d):
    print('\nThere are nothing here')
    nothing = a - b*c + d**2 # nothing = 4
    tiny_letter = min('max number') # tiny_letter = ' '

    return nothing, tiny_letter


print(Something(2, 5, 3, 5))
print(Nothing(3, 2, 4, 3))
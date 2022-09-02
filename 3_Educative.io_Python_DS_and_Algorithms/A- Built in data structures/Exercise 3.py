'''
Highs and lows
'''

def count_low_high(num_list):
    if len(num_list) == 0:
        return None

    high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
    low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])

    return [low_list, high_list]

num_list = [20, 70, 10, 30, 50, 40, 90]

print("Result for the first way:", count_low_high(num_list))

# An alternative way to do the same exercise but using lambda and filter

def new_count_low_high(num_list):
    if len(num_list) == 0:
        return none

    h_list = list(filter(lambda num: num > 50 or num % 3 == 0, num_list))
    l_list = list(filter(lambda num: num <= 50 and not num % 3 == 0, num_list))

    return [len(l_list), len(h_list)]

print("Alternative way:", new_count_low_high(num_list))


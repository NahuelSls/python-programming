
def cuenta(number):
    print(number)
    if number == 0:
        return 0
    interm = cuenta(number - 1)

    print(number)

cuenta(5)

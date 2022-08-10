
def numbers(min, max):
    if min < max:
        print('Your number is correct')
        return min
    return max

def conditional(price):
    while price >= 0:
        if price >= 25:
            new_price = price - price * 5 / 100
            print('Your new price:', new_price)
        else:
            new_price = price + price ** 2
            print('Future price for this product:', new_price)
        return new_price

conditional(int(input('Introduce a price: ')))

numbers(input('Introduce two numbers:'), input('Another number:'))
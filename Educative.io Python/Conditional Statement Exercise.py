'''
This is an exercise to apply discounts to a price introduced by the user.
While the price introduced by the user >= 0 the program will show us the applied discount for X price.
If the user put a price < 0 then the program will ask for another price.

An extra for this part I decided to try the function options to avoid to use 'break' in each condition and the different type of loops that are explaining in this part.
'''

#Using a loop for this exercise
'''while True:
    price = int(input('\nWrite the price and check the discounts: '))

    if price >= 300:
        discount = price * 30 / 100
        new_price = price - discount
        print('30% discounts applied:', new_price)
        break
    elif price >= 200 and price < 300:
        discount_1 = price * 20 / 100
        new_price_1 = price - discount_1
        print('20% discounts applied:', new_price_1)
        break
    elif price >= 100 and price < 200:
        discount_2 = price * 10 / 100
        new_price_2 = price - discount_2
        print('10% discounts applied:', new_price_2)
        break
    elif price >= 0 and price < 100:
        discount_3 = price * 5 / 100
        new_price_3 = price - discount_3
        print('5% discounts applied:', new_price_3)
        break
    else:
        print('Sorry, you need to try again.')


#Using function for the same exercise
def correct_price(price):
    while True:
        if price >= 300:
            discount = price * 30 / 100
            new_price = price - discount

        elif price >= 200 and price < 300:
            discount = price * 20 / 100
            new_price = price - discount

        elif price >= 100 and price < 200:
            discount = price * 10 / 100
            new_price = price - discount

        elif price < 100:
            discount = price * 5 / 100
            new_price = price - discount

        return new_price

def wrong_price(again):
        print('Wrong number. Please, try again.')
        return

while True:
    price_0 = int(input('\nIntroduce a price: '))
    if price_0 >= 0:
        print('Discount applied:', correct_price(price_0))
        break
    else:
        wrong_price(price_0)
        '''

while True:
    price = int(input('\nIntroduce another price: '))
    prices = [price - price * 30 / 100, price - price * 20 / 100, price - price * 10 /100, price - price * 5 / 100]

    if price >= 0:
        for i in range(0, len(prices)):
            if price >= 300 and i == 0:
                new_pr = prices[i]
                print('30% discounts applied: ', new_pr)
            elif price >= 200 and price < 300 and i == 1:
                new_pr = prices[i]
                print('20% discounts applied: ', new_pr)
            elif price >= 100 and price < 200 and i == 2:
                new_pr = prices[i]
                print('10% disocunts applied:', new_pr)
            elif price < 100 and i == 3:
                new_pr = prices[i]
                print('5% disocunts applied:', new_pr)
        break

    else:
         print('No discounts applied, try again.')



















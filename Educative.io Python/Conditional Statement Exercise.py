#Discounted price exercise

while True:
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















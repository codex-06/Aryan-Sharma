prices = (input('prices of products ').split(" "))
eight_off = int(input("number of 800 rs off coupons "))
four_off = int(input("number of 400 rs of coupons "))
two_off = int(input("number of 200 rs off coupons "))
discount = 0
for price in prices:
    price = int(price)
    if price >= 1600 and eight_off != 0:
        discount += 800
        eight_off -= 1
    elif price >= 800 and four_off != 0:
        discount += 400
        four_off -= 1
    elif price >= 400 and two_off != 0:
        discount += 200
        two_off -= 1
print(f'max discount is rs{discount}')



days = int(input())
nights = days - 1
type_of_room = input()
review = input()
price = 0
price_with_discount = 0

if type_of_room == 'room for one person' and nights > 0:
    price_with_discount = nights * 18
elif type_of_room == 'apartment':
    if 0 < nights < 10:
        price = nights * 25
    elif nights == 10:
        price = nights * 25
        price_with_discount = price - (price * 0.3)
    elif 10 < nights <= 15:
        price = nights * 25
        price_with_discount = price - (price * 0.35)
    elif nights > 15:
        price = nights * 25
        price_with_discount = price - (price * 0.50)
elif type_of_room == 'president apartment':
    if 0 < nights < 10:
        price = nights * 35
    elif nights == 10:
        price = nights * 35
        price_with_discount = price - (price * 0.1)
    elif 10 < nights <= 15:
        price = nights * 35
        price_with_discount = price - (price * 0.15)
    elif nights > 15:
        price = nights * 35
        price_with_discount = price - (price * 0.20)

if review == 'positive':
    price_with_discount = price_with_discount + (price_with_discount * 0.25)
else:
    price_with_discount = price_with_discount - (price_with_discount * 0.1)

print(f'{price_with_discount:.2f}')
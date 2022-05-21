price = input()
total = 0

while price != 'special' and price != 'regular':
    price = float(price)
    if price >= 0:
        total += price
    else:
        print('Invalid price!')
        pass
    price = input()

total_with_tax = total + total * 0.2
taxes = total_with_tax - total
if price == "special":
    special_customer = total_with_tax - (total_with_tax * 0.1)

if total < 0:
    print('Invalid order!')
else:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total:.2f}')
    print(f'Taxes: {taxes:.2f}')
    print("-----------")

print(special_customer)
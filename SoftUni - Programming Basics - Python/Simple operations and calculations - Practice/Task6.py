days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

price_of_cakes = cakes * 45
price_of_waffles = waffles * 5.80
price_of_pancakes = pancakes * 3.20

price_per_day = (price_of_cakes + price_of_pancakes + price_of_waffles) * bakers
total_price = price_per_day * days
costs = total_price - (total_price / 8)

print(f'{costs:.2f}')
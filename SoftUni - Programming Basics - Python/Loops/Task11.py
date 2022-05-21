age = int(input())
price_of_washer = float(input())
price_of_toy = float(input())
number_of_toys = 0
sum_of_money = 0

for index in range(1, age + 1):
    if index % 2 == 0:
        sum_of_money += (index * 5) - 1
    else:
        number_of_toys += 1

sum_of_money = sum_of_money + (number_of_toys * price_of_toy)

if sum_of_money >= price_of_washer:
    print(f'Yes! {sum_of_money - price_of_washer:.2f}')
else:
    print(f'No! {price_of_washer - sum_of_money:.2f}')
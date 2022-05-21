items = input().split("|")
budget = int(input())
money_left = budget
new_budget = 0

for index in range(len(items)):
    item_element = items[index].split("->")
    type = item_element[0]
    price = float(item_element[1])
    if budget - price >= 0:
        if type == "Clothes" and price <= 50:
            print(f"{(price + (price * 0.4)):.2f}", end=" ")
            budget -= price
            new_budget += price + (price * 0.4)
        elif type == "Shoes" and price <= 35:
            print(f"{(price + (price * 0.4)):.2f}", end=" ")
            budget -= price
            new_budget += price + (price * 0.4)
        elif type == "Accessories" and price <= 20.50:
            print(f"{(price + (price * 0.4)):.2f}:", end=" ")
            budget -= price
            new_budget += price + (price * 0.4)
        else:
            continue
    else:
        break

new_budget += budget

print(f'\nProfit: {(new_budget - money_left):.2f}')
if new_budget >= 150:
    print('Hello, France!')
else:
    print('Time to go.')
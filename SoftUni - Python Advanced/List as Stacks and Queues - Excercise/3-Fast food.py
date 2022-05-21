total_food = int(input())
orders = [int(x) for x in input().split()]

print(max(orders))

while len(orders) > 0:
    if total_food <= orders[0]:
        break
    total_food -= orders[0]
    orders.pop(0)

orders_to_str = [str(x) for x in orders]

if len(orders) > 0:
    print(f"Orders left: {', '.join(orders_to_str)}")
else:
    print('Orders complete')
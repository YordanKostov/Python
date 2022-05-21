command = input()
total_price = {}
total_quantity = {}

while command != 'buy':
    command = command.split(" ")
    name = command[0]
    price = float(command[1])
    quantity = float(command[2])
    if name not in total_price:
        total_price[name] = price
        total_quantity[name] = quantity
    else:
        if total_price[name] != price:
            total_price[name] = price
        total_quantity[name] += quantity
    command = input()

for item in total_price:
    print(f"{item} -> {(total_price[item] * total_quantity[item]):.2f}")
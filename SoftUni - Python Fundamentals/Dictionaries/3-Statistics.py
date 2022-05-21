command = input()
dic = {}

while command != 'statistics':
    command = command.split(": ")
    product = command[0]
    quantity = command[1]
    if product in dic.keys():
        dic[product] += int(quantity)
    else:
        dic[command[0]] = int(quantity)
    command = input()

if command == 'statistics':
    print('Products in stock:')
    for product in dic:
        print(f"- {product}: {dic[product]}")
    print(f"Total Products: {len(dic.keys())}")
    print(f'Total Quantity: {sum(dic.values())}')

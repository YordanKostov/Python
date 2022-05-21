data = input().split()
products = input().split()
d = {}

for index in range(0, len(data), 2):
    d[data[index]] = int(data[index +1])

for product in products:
    if product in d.keys():
        print(f'We have {d[product]} of {product} left')
    else:
        print(f"Sorry we don't have {product}")

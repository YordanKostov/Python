import re

command = input()
pattern = r">>([A-Z][a-z]+|[A-Z]+)+<<([\d.]+)!([\d.]+)"
items = []
price = 0

while command != 'Purchase':
    matches = re.match(pattern, command)
    if matches:
        matches = re.findall(pattern, command)
        items.append(matches[0][0])
        price += float(matches[0][1]) * float(matches[0][2])
    command = input()
print('Bought furniture:')
for item in items:
    print(item)
print(f'Total money spend: {price:.2f}')
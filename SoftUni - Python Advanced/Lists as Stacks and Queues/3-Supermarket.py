command = input()
names = []

while command != 'End':
    if command == 'Paid':
        for name in names:
            print(name)
        names.clear()
    else:
        names.append(command)
    command = input()

print(f'{len(names)} people remaining.')

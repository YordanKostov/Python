quantity_water = int(input())
command = input()
names = []

while command != 'Start':
    names.append(command)
    command = input()

while command != 'End':
    command.split()
    if command[0].isdigit():
        if int(command[0]) <= quantity_water:
            print(f"{names[0]} got water")
            names.pop(0)
            quantity_water -= int(command[0])
        else:
            print(f"{names[0]} must wait")
            names.pop(0)
    elif command[0] == 'refill':
        quantity_water += command[1]
    command = input()

if quantity_water < 0:
    print("0 liters left")
else:
    print(f"{quantity_water} liters left")

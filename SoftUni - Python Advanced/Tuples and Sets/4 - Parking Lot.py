command = input().split(", ")
s = set()

while command != 'END':
    command = str(command).split(", ")
    info = command[0]
    number = command[1]
    if info == "IN":
        s.add(number)
    elif number in s:
        s.remove(number)
    command = input()

if len(s) > 0:
    print("\n".join(s))
else:
    print('Parking Lot is Empty')
lines = int(input())
tank = 255
filled = 0

for index in range(lines):
    current_number = int(input())
    if filled + current_number > tank:
        print('Insufficient capacity!')
    else:
        filled += current_number

print(filled)
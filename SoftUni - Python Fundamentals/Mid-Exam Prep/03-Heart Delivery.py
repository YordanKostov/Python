neighborhood = [int(house) for house in input().split("@")]
current_house = 0
command = input()
while command != 'Love!':
    command = command.split()
    current_house += int(command[1])
    while current_house >= len(neighborhood):
        current_house = 0
    neighborhood[current_house] -= 2
    if neighborhood[current_house] == 0:
        print(f"Place {current_house} has Valentine's day.")
    elif neighborhood[current_house] < 0:
        print(f"Place {current_house} already had Valentine's day.")
    command = input()

print(f"Cupid's last position was {current_house}")
counter = 0

for number in neighborhood:
    if number > 0:
        counter += 1
print(f"Cupid has failed {counter} places")
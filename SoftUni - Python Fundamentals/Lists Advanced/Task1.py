wagons = int(input())
data = input()
train = [0] * wagons

while data != 'End':
    command = data.split()
    if command[0] == 'add':
        people = int(command[1])
        train[-1] += people
    elif command[0] == 'insert':
        people = int(command[2])
        index = int(command[1])
        train[index] += people
    elif command[0] == 'leave':
        people = int(command[2])
        index = int(command[1])
        train[index] -= people
    data = input()

print(train)
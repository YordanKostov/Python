groceries = [grocerie for grocerie in input().split("!")]

command = input()
while command != 'Go Shopping!':
    command = command.split()
    if command[0] == "Urgent":
        if command[1] not in groceries:
            groceries.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in groceries:
            groceries.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in groceries:
            for i, word in enumerate(groceries):
                if word == command[1]:
                    groceries[i] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in groceries:
            groceries.remove(command[1])
            groceries.append(command[1])

    command = input()

print(", ".join(groceries))
friends = input().split(", ")
command = input().split()
lost = 0
blacklisted = 0
while command[0] != 'Report':
    if command[0] == "Blacklist":
        if command[1] in friends:
            print(f"{command[1]} was blacklisted.")
            blacklisted += 1
            for index in range(len(friends)):
                if friends[index] == command[1]:
                    friends[index] = 'Blacklisted'
        else:
            print(f"{command[1]} was not found.")

    elif command[0] == 'Error':
        index = int(command[1])
        if friends[index] != 'Blacklisted' and friends[index] != 'Lost':
            print(f"{friends[index]} was lost due to an error.")
            lost += 1
            friends[index] = 'Lost'
    elif command[0] == 'Change':
        index = int(command[1])
        new_Name = command[2]
        if 0 <= index < len(friends):
            if friends[index] != 'Blacklisted' and friends[index] != 'Lost' and friends[index] != new_Name:
                print(f"{friends[index]} changed his username to {new_Name}.")
                friends[index] = new_Name

    command = input().split()

print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost}")
print(" ".join(friends))

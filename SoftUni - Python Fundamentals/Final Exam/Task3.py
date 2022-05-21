command = input()
guests_dict = {}
count_of_unliked = 0

while command != "Stop":
    command = command.split("-")
    action = command[0]
    guest = command[1]
    meal = command[2]
    if action == "Like":
        if guest not in guests_dict.keys():
            guests_dict[guest] = []
            guests_dict[guest].append(meal)
        else:
            if meal not in guests_dict[guest]:
                guests_dict[guest].append(meal)
    if action == "Unlike":
        if guest in guests_dict.keys():
            if meal in guests_dict[guest]:
                guests_dict[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")
                count_of_unliked += 1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

    command = input()

guests_dict = dict(sorted(guests_dict.items(), key=lambda g: (-len(g[1]), g[0])))


for key in guests_dict:
    if len(guests_dict[key]) > 0:
        print(f"{key}: {', '.join(guests_dict[key])}")
    else:
        print(f"{key}:")
print(f"Unliked meals: {count_of_unliked}")

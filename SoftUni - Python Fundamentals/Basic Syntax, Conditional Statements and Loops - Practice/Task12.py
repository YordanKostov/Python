word = input()
capitals = []

for index in range(len(word)):
    if word[index] == word[index].upper():
        capitals.append(index)

print(capitals)

data = input().split()
dicktionary = {}

for index in range(0, len(data), 2):
    dicktionary[data[index]] = int(data[index +1])

print(dicktionary)

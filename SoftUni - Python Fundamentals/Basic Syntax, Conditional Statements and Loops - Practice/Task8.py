first = input()
second = input()

for index in range(len(first)):
    if first[index] != second[index]:
        first = first.replace(first[index], second[index], 1)
        print(first)
    else:
        continue
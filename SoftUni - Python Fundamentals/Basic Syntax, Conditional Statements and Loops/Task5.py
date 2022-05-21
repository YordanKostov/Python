number = int(input())

for index in range(1, number + 1):
    print("*" * index)
for index in range(number - 1, 0, -1):
    print("*" * index)
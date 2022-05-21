number = int(input())

for count in range(0, number+1):
    if count % 2 == 0:
        print(2 ** count)

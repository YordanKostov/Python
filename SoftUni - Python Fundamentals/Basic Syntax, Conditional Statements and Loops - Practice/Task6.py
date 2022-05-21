number = int(input())

while True:
    number += 1
    year = str(number)
    if len(set(year)) == len(year):
        print(year)
        break

import sys

maximum = -sys.maxsize

for index in range(3):
    number = int(input())
    if number > maximum:
        maximum = number

print(maximum)
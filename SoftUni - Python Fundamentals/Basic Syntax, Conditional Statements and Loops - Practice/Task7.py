import sys

divisor = int(input())
bound = int(input())
biggest = -sys.maxsize

for number in range(1, bound + 1):
    if number % divisor == 0 and bound >= number > 0:
        if number >= biggest:
            biggest = number

print(biggest)

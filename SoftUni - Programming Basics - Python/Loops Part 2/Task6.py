import sys

times = int(input())
minimum_number = sys.maxsize

while times > 0:
    current_number = int(input())
    if current_number < minimum_number:
        minimum_number = current_number
    times -= 1

print(minimum_number)
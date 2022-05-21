import sys

times = int(input())
maximum_number = -sys.maxsize

while times > 0:
    current_number = int(input())
    if current_number > maximum_number:
        maximum_number = current_number
    times -= 1

print(maximum_number)
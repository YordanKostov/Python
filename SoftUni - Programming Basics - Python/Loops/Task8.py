import sys

number = int(input())

maximum_number = -sys.maxsize
minimum_number = sys.maxsize

for index in range(number):
    current_number = int(input())
    if current_number >= maximum_number:
        maximum_number = current_number
    if current_number <= minimum_number:
        minimum_number = current_number

print(f"Max number: {maximum_number}")
print(f'Min number: {minimum_number}')
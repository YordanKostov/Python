import sys

number = int(input())
max_number = -sys.maxsize
sum_of_low = 0

for index in range(number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    sum_of_low += current_number
if sum_of_low - max_number == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    sum_of_low -= max_number
    print(f'No\nDiff = {abs(max_number - sum_of_low)}')
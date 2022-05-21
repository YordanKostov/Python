number = int(input())
sum_first = 0
sum_second = 0
for index in range(0, number * 2):
    current_number = int(input())
    if index < number:
        sum_first += current_number
    else:
        sum_second += current_number

if sum_first == sum_second:
    print(f"Yes, sum = {sum_first}")
else:
    print(f"No, diff = {abs(sum_second-sum_first)}")

number = int(input())
sum_even = 0
sum_odd = 0

for index in range(number):
    current_number = int(input())
    if index % 2 == 0:
        sum_odd += current_number
    else:
        sum_even += current_number

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_even}")
else:
    print(f"No\nDiff = {abs(sum_even-sum_odd)}")
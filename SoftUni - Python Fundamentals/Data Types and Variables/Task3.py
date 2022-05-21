number = int(input())

for index in range(1, number + 1):
    sum_of_digits = 0
    digits = index
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits / 10)
    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f'{index} -> True')
    else:
        print(f'{index} -> False')
        
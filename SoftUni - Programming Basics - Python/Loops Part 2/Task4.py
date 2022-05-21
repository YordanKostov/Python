deposits = int(input())
money = 0
sum_of_money = 0

while deposits != 0:
    money = float(input())
    if money <= 0:
        print('Invalid operation!')
        break
    else:
        print(f"Increase: {money}")
    sum_of_money += money
    deposits -= 1

print(f'Total: {sum_of_money:.2f}')

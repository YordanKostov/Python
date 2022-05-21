budget = float(input())
people = int(input())
price_of_clothes = float(input())

decor = budget * 0.1

if people > 150:
    price_of_clothes = price_of_clothes - (price_of_clothes * 0.1)

budget = budget - decor - (price_of_clothes * people)

if budget >= 0:
    print(f'Action!\nWingard starts filming with {budget:.2f} leva left.')
else:
    print(f'Not enough money! \n Wingard needs {abs(budget):.2f} leva more.')
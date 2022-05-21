budget = float(input())
season = input()
fishers = int(input())
cost = 0

if season == 'Spring':
    cost = 3000
    if 0 < fishers <= 6:
        cost = cost - (cost * 0.10)
    elif 6 < fishers <= 11:
        cost = cost - (cost * 0.15)
    elif fishers > 11:
        cost = cost - (cost * 0.25)
elif season == 'Summer' or season == "Autumn":
    cost = 4200
    if 0 < fishers <= 6:
        cost = cost - (cost * 0.10)
    elif 6 < fishers <= 11:
        cost = cost - (cost * 0.15)
    elif fishers > 11:
        cost = cost - (cost * 0.25)
elif season == 'Winter':
    cost = 2600
    if 0 < fishers <= 6:
        cost = cost - (cost * 0.10)
    elif 6 < fishers <= 11:
        cost = cost - (cost * 0.15)
    elif fishers > 11:
        cost = cost - (cost * 0.25)

if season != 'Autumn':
    if fishers != 0 and fishers % 2 == 0:
        cost = cost - (cost * 0.05)

if cost < budget:
    print(f'Yes! You have {budget - cost:.2f} leva left.')
else:
    print(f'Not enough money! You need {(cost - budget):.2f} leva.')
drinks = input()
quantity = int(input())


def price(drink, times):
    if drink == 'coffee':
        print(f"{1.50 * times:.2f}")
    elif drink == 'water':
        print(f'{1 * times:.2f}')
    elif drink == 'coke':
        print(f'{1.40 * times:.2f}')
    elif drink == 'snacks':
        print(f'{2 * times:.2f}')


price(drinks, quantity)

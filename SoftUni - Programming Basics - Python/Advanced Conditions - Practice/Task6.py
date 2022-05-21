budget = float(input())
season = input()
destination = ''
vacation = ''
cost = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation = 'Camp'
        cost = budget * 0.3
    elif season == 'winter':
        vacation = 'Hotel'
        cost = budget * 0.7
elif 1000 >= budget > 100:
    destination = 'Balkans'
    if season == 'summer':
        vacation = 'Camp'
        cost = budget * 0.4
    elif season == 'winter':
        vacation = 'Hotel'
        cost = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    vacation = 'Hotel'
    cost = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{vacation} - {cost:.2f}')



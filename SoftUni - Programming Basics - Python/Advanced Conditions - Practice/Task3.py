temperature = int(input())
time = input()
outfit = ''
shoes = ''

if time == 'Morning':
    if 10 <= temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature > 24:
        outfit = 'T-shit'
        shoes = 'Sandals'
elif time == 'Afternoon':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temperature > 24:
        outfit = 'Swim suit'
        shoes = 'Barefoot'
elif time == 'Evening':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature > 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'


print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")

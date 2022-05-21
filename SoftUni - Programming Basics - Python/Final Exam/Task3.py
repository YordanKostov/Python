flower = input()
number_of_flowers = int(input())
season = input()
honey_made = 0
total_honey = 0
honey_seasonal = 0

if season == 'Spring':
    if flower == 'Sunflower':
        honey_made = 10
    elif flower == 'Daisy':
        honey_made = 12 + (12 * 0.1)
    elif flower == 'Lavender':
        honey_made = 12
    elif flower == 'Mint':
        honey_made = 10 + (10 * 0.1)
    honey_seasonal = number_of_flowers * honey_made
elif season == 'Summer':
    if flower == 'Sunflower':
        honey_made = 8
    elif flower == 'Daisy':
        honey_made = 8
    elif flower == 'Lavender':
        honey_made = 8
    elif flower == 'Mint':
        honey_made = 12
    total_honey = number_of_flowers * honey_made
    honey_seasonal = total_honey + (total_honey * 0.1)
elif season == 'Autumn':
    if flower == 'Sunflower':
        honey_made = 12
    elif flower == 'Daisy':
        honey_made = 6
    elif flower == 'Lavender':
        honey_made = 6
    elif flower == 'Mint':
        honey_made = 6
    total_honey = number_of_flowers * honey_made
    honey_seasonal = total_honey - (total_honey * 0.05)

print(f'Total honey harvested: {honey_seasonal:.2f}')
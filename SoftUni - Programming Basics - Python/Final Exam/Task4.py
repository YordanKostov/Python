from math import floor

population = int(input())
years = int(input())

for year in range(1, years + 1):
    population += floor(population / 10) * 2
    if year % 5 == 0:
        population -= floor(population / 50) * 5
    population -= floor(population / 20) * 2

print(f'Beehive population: {population}')
from math import floor

L = float(input())
W = float(input())
A = float(input())

total_space = (L * 100) * (W * 100)
wardrobe = (A * A) * 10000
bench = total_space / 10
free_space = total_space - bench - wardrobe
number_of_dancers = free_space / (40 + 7000)

print(f'{floor(number_of_dancers)}')
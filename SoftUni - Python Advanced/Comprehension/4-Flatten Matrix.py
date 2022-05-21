rows = int(input())
matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

flattened = [num for sublist in matrix for num in sublist]
print(flattened)
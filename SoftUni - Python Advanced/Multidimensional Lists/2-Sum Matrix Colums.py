rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for col in range(cols):
    sum_of_col = 0
    for row in range(rows):
        sum_of_col += matrix[row][col]
    print(sum_of_col)
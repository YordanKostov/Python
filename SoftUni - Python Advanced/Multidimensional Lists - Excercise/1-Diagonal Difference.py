rows = int(input())
matrix = []
sum_of_primary = 0
sum_of_secondary = 0
col = 0

for row in range(rows):
    column = [int(x) for x in input().split()]
    matrix.append(column)
    sum_of_primary += matrix[row][row]


for row in range(rows-1, -1, -1):
    sum_of_secondary += matrix[row][col]
    col += 1

print(abs(sum_of_primary - sum_of_secondary))

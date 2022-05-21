rows, cols = [int(x) for x in input().split()]
matrix = []
max = 0
sum = 0
for row in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)

for row in range(rows - 2):
    for col in range(cols - 2):
        for rower in range(row, row+3):
            for colur in range(col, col+3):
                sum += matrix[rower][colur]
        if max < sum:
            max = sum
        sum = 0

print(max)
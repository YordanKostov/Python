rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_of_matrix = 0
for row in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)
    sum_of_matrix += sum(numbers)

print(sum_of_matrix)
print(matrix)
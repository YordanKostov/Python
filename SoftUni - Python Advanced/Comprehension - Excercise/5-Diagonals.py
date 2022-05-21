rows = int(input())
matrix = []
sum_of_primary = 0
sum_of_secondary = 0
col = 0

for row in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

main_diagonal = [matrix[row][row] for row in range(rows)]

second_diagonal = [matrix[row][rows-1-row] for row in range(rows -1, -1, -1)]

second_diagonal.reverse()
print(f"First diagonal: {', '.join(map(str, main_diagonal))}. Sum: {sum(main_diagonal)}")
print(f"Second diagonal: {', '.join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}")
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(num) for num in input().split()])

change = input()
while change != 'END':
    command, row, col, value = change.split()
    if 0 <= int(row) < n and 0 <= int(col) < n:
        if command == "Add":
            matrix[int(row)][int(col)] += int(value)
        elif command == "Subtract":
            matrix[int(row)][int(col)] -= int(value)
    else:
        print("Invalid coordinates")
    change = input()

for row in matrix:
    row = map(str, row)
    print(" ".join(row))


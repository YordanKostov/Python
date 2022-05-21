matrix = []
rows = 8
queens = []
king = []
king_row = 0
king_col = 0

checks = []
for row in range(rows):
    matrix.append(input().split())

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "Q":
            queens.append([row, col])
        if matrix[row][col] == "K":
            king.append(row)
            king.append(col)
            king_row = row
            king_col = col

for row in range(1, rows):
    if matrix[row][row-1] == "Q":
        checks.append([row, row-1])
        if row > king_row:
            break

for row in range(rows-1, -1, -1):
    if matrix[row][row+1] == "Q":
        checks.append([row, row+1])
        

print(king_row)
print(king_col)
print(checks)
print(queens)
print(king)
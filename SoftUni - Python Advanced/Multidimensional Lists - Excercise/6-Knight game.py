n = int(input())
matrix = []
count = 0

kill_rows = [2, 2, -2, -2, 1, 1, -1, -1]
kill_cols = [1, -1, 1, -1, 2, -2, 2, -2]


def is_in_bounds(rows, cols):
    if 0 <= rows < n and 0 <= cols < n:
        return True
    return False


for _ in range(n):
    matrix.append(list(input()))


for row in range(n):
    for col in range(n):
        if matrix[row][col] == "K":
            for index in range(len(kill_rows)):
                potential_row = row + kill_rows[index]
                potential_col = col + kill_cols[index]
                if is_in_bounds(potential_row, potential_col):
                    if matrix[potential_row][potential_col] == 'K':
                        count += 1
                        matrix[potential_row][potential_col] = "0"

print(count)
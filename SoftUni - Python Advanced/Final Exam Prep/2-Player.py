initial_string = input()
rows = int(input())
matrix = []
current_row = 0
current_col = 0
word = []
punish = 0


def is_in_bounds(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


for row in range(rows):
    matrix.append(list(input()))

number_of_commands = int(input())

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "P":
            current_col = col
            current_row = row

for _ in range(number_of_commands):
    to_go = input()
#    matrix[current_row][current_col] = "-"
    if to_go == "up" and is_in_bounds(current_row - 1, current_col):
        matrix[current_row][current_col] = "-"
        current_row -= 1
        word.append(matrix[current_row][current_col])

    elif to_go == "down" and is_in_bounds(current_row + 1, current_col):
        matrix[current_row][current_col] = "-"
        current_row += 1
        word.append(matrix[current_row][current_col])

    elif to_go == "left" and is_in_bounds(current_row, current_col - 1):
        matrix[current_row][current_col] = "-"
        current_col -= 1
        word.append(matrix[current_row][current_col])

    elif to_go == "right" and is_in_bounds(current_row, current_col + 1):
        matrix[current_row][current_col] = "-"
        current_col += 1
        word.append(matrix[current_row][current_col])

    else:
        punish += 1

matrix[current_row][current_col] = "P"

if "-" in word:
    word.remove("-")
word = "".join(word)
initial_string += word
stringer = list(initial_string)

for index in range(punish):
    if len(stringer) > 0:
        stringer.pop()

print(f"{''.join(stringer)}")

for row in matrix:
    print("".join(row))

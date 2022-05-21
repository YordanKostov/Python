rows, cols = [int(x) for x in input().split()]
matrix = []
for row in range(rows):
    numbers = [x for x in input().split()]
    matrix.append(numbers)

command = input()

while command != 'END':
    command = command.split()
    if "swap" not in command:
        print('Invalid input')
    else:
        row = int(command[1])
        col = int(command[2])
        row1 = int(command[3])
        col1 = int(command[4])
        if row < rows or col < cols or row1 < rows or col1 < cols:
            temp = matrix[row][col]
            matrix[row][col] = matrix[row1][col1]
            matrix[row1][col1] = temp
            for element in matrix:
                print(" ".join(element))
        else:
            print("Invalid input")
    command = input()
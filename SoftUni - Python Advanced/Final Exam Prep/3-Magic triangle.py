def get_magic_triangle(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in range(row + 1):
            matrix[row].append(0)
    for row in range(n):
        for col in range(row + 1):
            matrix[row][0] = 1
            matrix[row][-1] = 1
            if col != 0 and col != row and row > 1:
                matrix[row][col] = matrix[row-1][col] + matrix[row-1][col-1]
    return matrix


get_magic_triangle(5)



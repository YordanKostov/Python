rows, cols = [int(x) for x in input().split()]
word = [x for x in input()]
matrix = []
word_index = 0

for row in range(rows):
    matrix.append([0 for el in range(cols)])

for row in range(rows):
    for col in range(cols):
        matrix[row][col] = word[word_index]
        word_index += 1
        if word_index == len(word):
            word_index = 0

for row in range(rows):
    if row % 2 != 0:
        matrix[row].reverse()
    print(f"{''.join(matrix[row])}")

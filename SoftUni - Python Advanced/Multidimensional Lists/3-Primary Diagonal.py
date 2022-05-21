rows = int(input())
matrix = []
sum_of_prime = 0

for row in range(rows):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)
    sum_of_prime += matrix[row][row]

print(sum_of_prime)
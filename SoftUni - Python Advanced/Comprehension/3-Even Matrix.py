rows = int(input())
numbers = [[int(x) for x in input().split() if int(x) % 2 == 0] for row in range(rows)]
print(numbers)
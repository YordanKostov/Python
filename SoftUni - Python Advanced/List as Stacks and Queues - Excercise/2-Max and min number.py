n = int(input())
numbers = []
for index in range(n):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        numbers.append(query[1])
    if query[0] == 2 and len(numbers) > 0:
        numbers.pop()
    if query[0] == 3:
        print(max(numbers))
    if query[0] == 4:
        print(min(numbers))

numbers_to_str = [str(x) for x in numbers]
print(", ".join(numbers_to_str))
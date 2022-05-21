numbers = input().split()
numbers = [int(x) for x in numbers]
remove_numbers = int(input())

for index in range(remove_numbers):
    numbers.remove(min(numbers))

print(numbers)
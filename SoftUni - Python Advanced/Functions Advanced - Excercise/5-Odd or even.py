def even_or_odd(command, numbers):

    if command == 'Odd':
        result = sum(num for num in numbers if num % 2 != 0) * len(numbers)
    else:
        result = sum(num for num in numbers if num % 2 == 0) * len(numbers)
    return result

command = input()
numbers = [int(num) for num in input().split()]

print(even_or_odd(command, numbers))
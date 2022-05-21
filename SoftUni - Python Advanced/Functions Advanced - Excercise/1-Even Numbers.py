def even_numbers(numbers):
    result = list(filter(lambda x: x % 2 == 0, numbers))
    return result


print(f"{even_numbers([int(x) for x in input().split()])}")
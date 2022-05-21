def min_max_sum(numbers):
    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")


min_max_sum([int(num) for num in input().split()])
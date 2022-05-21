numbers = input()
numbers_to_list = numbers.split(" ")
numbers_changed = []
for number in numbers_to_list:
    numbers_changed.append(int(number) * -1)
print(numbers_changed)
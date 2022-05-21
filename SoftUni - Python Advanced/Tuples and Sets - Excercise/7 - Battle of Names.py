number = int(input())
set_of_odd = set()
set_of_even = set()

for _ in range(number):
    name = input()
    value = 0
    for letter in name:
        value += ord(letter)
    if value % 2 == 0:
        set_of_even.add(value)
    else:
        set_of_odd.add(value)

sum_of_odd = sum(set_of_odd)
sum_of_even = sum(set_of_even)


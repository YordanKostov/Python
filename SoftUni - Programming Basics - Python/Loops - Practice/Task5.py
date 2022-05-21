number = int(input())

p2 = 0
p3 = 0
p4 = 0

for index in range(number):
    current_number = int(input())
    if current_number % 2 == 0:
        p2 += 1
    if current_number % 3 == 0:
        p3 += 1
    if current_number % 4 == 0:
        p4 += 1


print(f'{p2 / number * 100:.2f}%')
print(f'{p3 / number * 100:.2f}%')
print(f'{p4 / number * 100:.2f}%')
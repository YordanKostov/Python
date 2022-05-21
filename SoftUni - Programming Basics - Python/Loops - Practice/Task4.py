number = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for index in range(number):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number < 400:
        p2 += 1
    elif 400 <= current_number < 600:
        p3 += 1
    elif 600 <= current_number < 800:
        p4 += 1
    elif 800 <= current_number < 1000:
        p5 += 1

print(f'{p1 / number * 100:.2f}%')
print(f'{p2 / number * 100:.2f}%')
print(f'{p3 / number * 100:.2f}%')
print(f'{p4 / number * 100:.2f}%')
print(f'{p5 / number * 100:.2f}%')

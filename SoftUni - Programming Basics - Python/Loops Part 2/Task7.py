name = input()
total_grades = 0
index = 0

while index < 12:
    total_grades += float(input())
    index += 1

if total_grades / 12 >= 4:
    print(f'{name.title()} graduated. Average grade: {total_grades / 12:.2f}')
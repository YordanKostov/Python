from math import ceil

students = int(input())
seasons = int(input())

for season in range(1, seasons + 1):
    students = ceil(students * 0.9)
    students = ceil(students * 0.9)
    students = ceil(students * 0.8)
    if season % 3 == 0:
        students = ceil(students + (students * 0.15))
    else:
        students = ceil(students + (students * 0.05))

print(f"Students: {students}")
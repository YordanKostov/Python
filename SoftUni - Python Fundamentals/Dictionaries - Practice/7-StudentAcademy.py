n = int(input())
students = {}

for index in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student in students:
    if sum(students[student]) / len(students[student]) < 4.50:
        students[student] = 'None'

print(students)
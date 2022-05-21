from statistics import mean

students = int(input())
students_grades = {}

for index in range(students):
    info = input().split()
    name = info[0]
    grade = float(info[1])
    if name not in students_grades:
        students_grades[name] = [grade]
    else:
        students_grades[name].append(grade)

for key, value in students_grades.items():
    print(f"{key} -> {' '.join(map(str, value))} ({mean(value):.2f})")

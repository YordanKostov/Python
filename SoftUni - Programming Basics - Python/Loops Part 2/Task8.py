name = input()
total_grades = 0
index = 0
first_time = True

while index < 12:
    current_grade = float(input())
    if current_grade < 4:
        if first_time:
            first_time = False
        else:
            print(f"{name} has been excluded at {index} grade")
            break
    total_grades += current_grade
    index += 1

if total_grades / 12 >= 4 and index == 12:
    print(f'{name.title()} graduated. Average grade: {total_grades / 12:.2f}')
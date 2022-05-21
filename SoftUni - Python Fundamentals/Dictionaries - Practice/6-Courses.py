command = input()
courses = {}

while command != 'end':
    command = command.split(" : ")
    course = command[0]
    student = command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    command = input()

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f'-- {student}')
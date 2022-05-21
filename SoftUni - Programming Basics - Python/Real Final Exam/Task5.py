from math import floor

students = int(input())
tasks = int(input())
energy = int(input())
solved = 0
questions = 0

while True:
    solved += tasks
    energy += tasks * 3
    students -= tasks
    questions += students * 2
    energy -= 3 * (students * 2)
    if energy <= 0:
        print('The trainer is too tired!')
        print(f'Questions asked: {questions}')
        break
    elif students < 10:
        print("The students are too few!")
        print(f"Problems solved: {solved}")
        break
    students += floor(students / 10)
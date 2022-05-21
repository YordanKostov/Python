bad_marks = int(input())
index = 0
average_score = 0
number_of_problems = 0
last_problem = ' '

while index < bad_marks:
    subject = input()
    if subject == "Enough":
        average_score /= number_of_problems
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {number_of_problems}')
        print(f'Last problem: {last_problem}')
        break
    mark = int(input())
    if mark <= 4:
        index += 1
    number_of_problems += 1
    average_score += mark
    last_problem = subject

if index >= bad_marks:
    print(f'You need a break, {index} poor grades.')
task = int(input())
points = int(input())
course = input()
coefficient = 0

if course == 'Basics':
    if task == 1:
        coefficient = 8
    elif task == 2:
        coefficient = 9
    elif task == 3:
        coefficient = 9
    elif task == 4:
        coefficient = 10

    final = (points * coefficient) / 100
    if task == 1:
        final = final - (final * 0.2)
elif course == 'Fundamentals':
    if task == 1:
        coefficient = 11
    elif task == 2:
        coefficient = 11
    elif task == 3:
        coefficient = 12
    elif task == 4:
        coefficient = 13
    final = (points * coefficient) / 100
elif course == 'Advanced':
    if task == 1:
        coefficient = 14
    elif task == 2:
        coefficient = 14
    elif task == 3:
        coefficient = 15
    elif task == 4:
        coefficient = 16

    final = (points * coefficient) / 100
    final = final + (final * 0.2)

print(f"Total points: {final:.2f}")
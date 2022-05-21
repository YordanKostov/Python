while True:
    total_grade = 0
    name = input()
    final = 0
    cheater = False
    if name == "Midnight":
        break
    for grade in range(6):
        points = int(input())
        if points < 0:
            print(f'{name} was cheating!')
            cheater = True
            break
        total_grade += points
    final = int((total_grade / 600) * 100)
    final = final * 0.06
    if final < 5 and not cheater:
        if final < 3:
            print(f'{name} - 2.00')
        else:
            print(f'{name} - {final:.2f}')
    elif final >= 5 and not cheater:
        print("===================")
        print("|   CERTIFICATE   |")
        print(f"|    {final:.2f}/6.00    |")
        print("===================")
        print(f'Issued to {name}')

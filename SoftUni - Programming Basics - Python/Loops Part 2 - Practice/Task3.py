vacation = float(input())
money = float(input())
counter = 0
days = 0

while True:
    action = input()
    number = float(input())
    days += 1
    if action == 'spend':
        counter += 1
        money -= number
        if money < 0:
            money = 0
        if counter == 5:
            print(f"You can't save the money.")
            print(days)
            break
    elif action == 'save':
        money += number
    if money >= vacation:
        print(f"You saved the money for {days} days.")
        break

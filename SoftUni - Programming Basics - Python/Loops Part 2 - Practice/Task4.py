counter = 0
while True:
    steps = input()
    if steps == "Going home":
        counter += int(input())
        if counter < 10000:
            print(f"{10000 - counter} more steps to reach goal.")
            break
        else:
            print('Goal reached! Good job!')
            break
    else:
        counter += int(steps)
        if counter >= 10000:
            print('Goal reached! Good job!')
            break
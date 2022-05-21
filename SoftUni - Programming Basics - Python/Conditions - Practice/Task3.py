speed = float(input())

if speed <= 10:
    print('Slow')
elif speed > 10 and speed <= 50:
    print('Average')
elif speed > 50 and speed <= 150:
    print('Fast')
elif speed > 150 and speed <= 1000:
    print('Ultra fast')
else:
    print('Extremely fast')

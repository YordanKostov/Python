import math

first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time
minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes:.0f}:0{seconds}')
else:
    print(f'{minutes:.0f}:{seconds}')
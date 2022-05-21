import math
hour = int(input())
minutes = int(input())

everything_in_minutes = (hour * 60) + minutes
total_minutes = everything_in_minutes + 15

hour_convert = math.floor(total_minutes / 60)
minutes_convert = math.floor(total_minutes % 60)

if hour_convert > 23:
    hour_convert = 24 - hour_convert

if minutes_convert < 10:
    print(f'{hour_convert}:0{minutes_convert}')
else:
    print(f'{hour_convert}:{minutes_convert}')
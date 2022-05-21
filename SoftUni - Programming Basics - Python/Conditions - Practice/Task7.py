from math import floor

record = float(input())
meters = float(input())
time_per_meter = float(input())

total_time = time_per_meter * meters
total_time = total_time + ((meters/15) * 12.5)

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {floor(total_time - record):.2f} seconds slower.')
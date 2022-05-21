from math import floor

hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

hour_of_exam_in_minutes = hour_of_exam * 60 + minute_of_exam
hour_of_arrival_in_minutes = hour_of_arrival * 60 + minute_of_arrival

difference = hour_of_exam_in_minutes - hour_of_arrival_in_minutes

if difference < 0:
    print("Late")
    if abs(difference) < 60:
        print(f'{abs(difference)} minutes after the start')
    else:
        if 0 <= difference % 60 < 10:
            print(f'{floor(abs(difference / 60))}:0{abs(difference % 60)} hours after the start')
        else:
            print(f'{floor(abs(difference / 60))}:{abs(difference % 60)} hours after the start')
if difference >= 0:
    if difference <= 30:
        print("On time")
    elif difference > 30:
        print("Early")
        if abs(difference) < 60:
            print(f'{abs(difference)} minutes before the start')
        else:
            if 0 <= difference % 60 < 10:
                print(f'{floor(abs(difference / 60))}:0{abs(difference % 60)} hours before the start')
            else:
                print(f'{floor(abs(difference / 60))}:{abs(difference % 60)} hours before the start')

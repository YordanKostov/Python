from math import floor

year = input()
holidays = int(input())
weekends = int(input())

weekends_in_sofia = (48 - weekends) * 3/4
holidays_playing = holidays * 2/3

total_play_time = holidays_playing + weekends + weekends_in_sofia

if year == "leap":
    total_play_time = total_play_time + (total_play_time * 0.15)

print(f'{floor(total_play_time)}')





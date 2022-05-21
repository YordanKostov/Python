type_of_movie = input().title()
rows = int(input())
columns = int(input())
profit = 0
area = rows * columns

if type_of_movie == 'Premiere':
    profit = area * 12
elif type_of_movie == 'Normal':
    profit = area * 7.50
elif type_of_movie == 'Discount':
    profit = area * 5
else:
    print('Error')

print(f'{profit:.2f} leva')
honey = float(input())
total_honey = 0
while True:
    name = input()
    if name == 'Winter has come':
        if total_honey < honey:
            print(f'Hard Winter! Honey needed {honey - total_honey:.2f}.')
        else:
            print(f'Well done! Honey surplus {total_honey - honey:.2f}.')
        break
    elif total_honey >= honey:
        print(f'Well done! Honey surplus {total_honey - honey:.2f}.')
        break
    total_from_bee = 0
    for month in range(6):
        income = float(input())
        total_from_bee += income
    if total_from_bee < 0:
        print(f'{name} was banished for gluttony')
    total_honey += total_from_bee

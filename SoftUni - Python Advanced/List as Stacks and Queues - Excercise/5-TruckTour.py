pumps = int(input())
fuel = 0
kilometers = 0
best_start = 0
distance = 0
for index in range(pumps):
    info = [int(x) for x in input().split()]
    fuel = info[0]
    kilometers = info[1]
    if distance < abs(fuel - kilometers):
        distance = abs(fuel - kilometers)
        best_start = index

print(best_start)

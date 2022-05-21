numbers = [int(x) for x in input().split()]
capacity = int(input())
current_occupancy = 0
racks = 1

for index in range(len(numbers) - 1, -1, -1):
    current_occupancy += numbers[index]
    if current_occupancy > capacity:
        current_occupancy = numbers[index]
        racks += 1

print(racks)
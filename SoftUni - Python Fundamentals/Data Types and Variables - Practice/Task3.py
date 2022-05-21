from math import ceil, floor

people = int(input())
capacity = int(input())
most = floor(people / capacity)
no_space = people - (most * capacity)

if people < capacity:
    print('All the persons fit inside in the elevator. Only one course is needed.')
elif people % capacity == 0:
    print(f'{most} courses * {capacity} people')
else:
    print(f'{most} courses * {capacity} people')
    print(f'1 course * {no_space} people')

width_of_space = int(input())
length_of_space = int(input())
height_of_space = int(input())

free_space = width_of_space * length_of_space * height_of_space
current_space = 0

while current_space <= free_space:
    boxes = input()
    if boxes == "Done":
        print(f'{free_space - current_space} Cubic meters left.')
        break
    current_space += int(boxes)
    if current_space >= free_space:
        print(f'No more free space! You need {current_space - free_space} Cubic meters more.')
        break

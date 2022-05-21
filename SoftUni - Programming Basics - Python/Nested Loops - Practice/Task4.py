jury = int(input())
final_average = 0
counter = 0
while True:
    presentation = input()
    if presentation == "Finish":
        break
    counter += 1
    presentation_average = 0
    for index in range(jury):
        presentation_average += float(input())
    presentation_average /= jury
    print(f'{presentation} - {presentation_average:.2f}.')
    final_average += presentation_average

print(f"Student's final assessment is {final_average / counter:.2f}.")
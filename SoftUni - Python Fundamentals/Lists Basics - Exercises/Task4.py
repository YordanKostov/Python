intake = input()
beggars = int(input())
intake_to_list = intake.split(", ")

beggars_list = [0] * beggars

for index in range(len(intake_to_list)):
    element = int(intake_to_list[index])
    beggar_index = index % len(beggars_list)
    beggars_list[beggar_index] += element

print(beggars_list)
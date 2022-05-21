fire = input().split("#")
water = int(input())
total_fire = 0
effort = 0

print("Cells:")
for index in range(len(fire)):
    if total_fire < (water - 150):
        fire_element = fire[index].split(" = ")
        if fire_element[0] == "High" and 81 <= int(fire_element[1]) <= 125:
            print(f" - {fire_element[1]}")
            total_fire += int(fire_element[1])
            effort += int(fire_element[1]) / 4
        elif fire_element[0] == "Medium" and 51 <= int(fire_element[1]) <= 80:
            print(f" - {fire_element[1]}")
            total_fire += int(fire_element[1])
            effort += int(fire_element[1]) / 4
        elif fire_element[0] == "Low" and 1 <= int(fire_element[1]) <= 50:
            print(f" - {fire_element[1]}")
            total_fire += int(fire_element[1])
            effort += int(fire_element[1]) / 4
        else:
            continue
    else:
        break

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
efficiency1 = int(input())
efficiency2 = int(input())
efficiency3 = int(input())
people = int(input())

total = efficiency1 + efficiency2 + efficiency3
hours = 0

while people > 0:
    if hours % 4 == 0 and hours > 0:
        hours += 1
    else:
        hours += 1
        people -= total

print(f"Time needed: {hours}h.")
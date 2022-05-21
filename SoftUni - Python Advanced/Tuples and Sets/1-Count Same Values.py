values = (float(x) for x in input().split())
counted = {}

for value in values:
    if value not in counted:
        counted[value] = 1
    else:
        counted[value] += 1

for key, value in counted.items():
    print(f"{key} - {counted[key]} times")
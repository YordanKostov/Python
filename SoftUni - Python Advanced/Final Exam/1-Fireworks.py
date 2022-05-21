from collections import deque

firework_effect = [int(x) for x in input().split(", ")]
explosive_power = [int(x) for x in input().split(", ")]
count_palm = 0
count_willow = 0
count_crossette = 0
removed_negatives = False


while len(firework_effect) > 0 and len(explosive_power) > 0:
    for item in explosive_power:
        if item <= 0:
            explosive_power.remove(item)
            removed_negatives = True
    for item in firework_effect:
        if item <= 0:
            firework_effect.remove(item)
            removed_negatives = True
    if removed_negatives:
        removed_negatives = False
        continue
    value = firework_effect[0] + explosive_power[-1]
    if value % 3 == 0 and value % 5 != 0:
        count_palm += 1
        firework_effect.pop(0)
        explosive_power.pop()
    elif value % 5 == 0 and value % 3 != 0:
        count_willow += 1
        firework_effect.pop(0)
        explosive_power.pop()
    elif value % 5 == 0 and value % 3 == 0:
        count_crossette += 1
        firework_effect.pop(0)
        explosive_power.pop()
    else:
        firework_effect.append(firework_effect.pop(0) - 1)
    if count_crossette >= 3 and count_palm >= 3 and count_willow >= 3:
        break

if count_crossette >= 3 and count_palm >= 3 and count_willow >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if len(firework_effect) > 0:
    print(f"Firework Effects left: {', '.join(map(str, firework_effect))}")
if len(explosive_power) > 0:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {count_palm}")
print(f"Willow Fireworks: {count_willow}")
print(f"Crossette Fireworks: {count_crossette}")

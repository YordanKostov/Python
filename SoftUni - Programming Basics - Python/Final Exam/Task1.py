from math import floor

bees = int(input())
flowers = int(input())
total_honey = bees * flowers * 0.21

honey_combs = floor(total_honey/100)
left = total_honey - (honey_combs * 100)

print(f"{honey_combs} honeycombs filled.")
print(f'{left:.2f} grams of honey left.')
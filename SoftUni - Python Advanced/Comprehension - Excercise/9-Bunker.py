categories = {category: [] for category in input().split(", ")}
n = int(input())
total_quality = 0
total_quantity = 0

for _ in range(n):
    category, item, quantity_quality = input().split(" - ")
    quantity, quality = quantity_quality.split(";")
    total_quantity += int(quantity.split(":")[1])
    total_quality += int(quality.split(":")[1])
    categories[category].append(item)

print(f"Count of items: {total_quantity}")
print(f"Average quality: {total_quality/len(categories):.2f}")
print(*[f"{key} -> {', '.join(value)}" for key, value in categories.items()], sep="\n")
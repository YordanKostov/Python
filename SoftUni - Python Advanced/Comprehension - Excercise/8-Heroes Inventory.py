names = input().split(", ")
data = input()
heroes = {}
while data != "End":
    name, item, cost = data.split("-")

    if not heroes.get(name):
        heroes[name] = {}

    if not heroes[name].get(item):
        heroes[name].update({item: int(cost)})
    data = input()

print(*[f"{name} -> Items: {len(items)}, Cost: {sum(items.values())}"for name, items in heroes.items()], sep="\n")


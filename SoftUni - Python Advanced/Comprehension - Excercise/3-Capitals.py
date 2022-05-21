countries = input().split(", ")
capitals = input().split(", ")

combo = dict(zip(countries, capitals))

for key, value in combo.items():
    print(f"{key} -> {value}")
text = [x for x in input().split()]
rever = []

for index in range(len(text) - 1, -1, -1):
    rever.append(text[index])

print(" ".join(rever))
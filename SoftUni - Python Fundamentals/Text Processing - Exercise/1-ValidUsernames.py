import re

names = input().split(", ")
valid = []

for name in names:
    if 3 <= len(name) <= 16:
        if re.match("^[A-Za-z0-9_-]*$", name):
            valid.append(name)

for name in valid:
    print(name)
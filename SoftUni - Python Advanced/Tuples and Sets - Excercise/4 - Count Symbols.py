text = input()
counter = {}
for letter in text:
    if letter not in counter:
        counter[letter] = 1
    else:
        counter[letter] += 1

for (key, value) in sorted(counter.items()):
    print(f'{key}: {value} time/s')
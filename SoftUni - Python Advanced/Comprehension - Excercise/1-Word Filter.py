text = input().split()
filtered = [x for x in text if len(x) % 2 == 0]
for word in filtered:
    print(word)
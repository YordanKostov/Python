text = list(input())
reverse = []

while len(text) > 0:
    letter = text.pop()
    reverse.append(letter)

print(''.join(reverse))
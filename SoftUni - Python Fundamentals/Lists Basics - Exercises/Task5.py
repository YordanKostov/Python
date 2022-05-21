cards = input().split()
times = int(input())
middle = int(len(cards) / 2)

for time in range(times):
    first = [cards[index] for index in range(middle)]
    second = [cards[index] for index in range(middle, len(cards))]
    cards = []
    for index in range(middle):
        cards.append(first[index])
        cards.append(second[index])

print(cards)


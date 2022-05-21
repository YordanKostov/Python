import itertools


def swapping(word, index):
    if index >= len(word):
        print(" ".join(word))
        return
    swapping(word, index + 1)
    for i in range(index + 1, len(word)):
        word[index], word[i] = word[i], word[index]
        swapping(word, index + 1)
        word[index], word[i] = word[i], word[index]


word = list(input())
swapping(word, 0)
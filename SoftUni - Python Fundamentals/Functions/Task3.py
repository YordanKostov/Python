words = input()
times = int(input())


def multiplier(word, time):
    for index in range(time):
        print(f"{word}", end="")

multiplier(words, times)

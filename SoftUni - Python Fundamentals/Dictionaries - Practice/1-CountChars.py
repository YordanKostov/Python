text = input()
number_of_letters = {}

for letter in text:
    if letter != " ":
        if letter not in number_of_letters:
            number_of_letters[letter] = 1
        else:
            number_of_letters[letter] += 1

for letter in number_of_letters:
    print(f'{letter} -> {number_of_letters[letter]}')

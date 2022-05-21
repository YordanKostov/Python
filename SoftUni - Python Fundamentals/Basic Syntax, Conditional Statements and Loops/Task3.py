word = input()
word_in_reverse = ''

for letter in range(len(word) - 1, -1, -1):
    word_in_reverse += word[letter]

print(word_in_reverse)
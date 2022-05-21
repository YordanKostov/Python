words = input().split()
search_word = input()
count = 0
polindrome = []

for word in words:
    if search_word == word:
        count += 1
    polindrom = ''
    for letter in range(len(word) - 1, -1, -1):
        polindrom += word[letter]
    if polindrome == word:
        polindrome.append(word)

print(polindrome)
print(f"Found palindrome {count} times")
import re
text = input().lower()
word = input()
matches = re.findall(word, text)
print(len(matches))



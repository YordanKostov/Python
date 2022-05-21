import re

text = input()
pattern = r"\b[a-z0-9.-_]+@[a-z.]+\b"
matches = re.findall(pattern, text)
for match in matches:
    print(match)
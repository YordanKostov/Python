import re
everything = ""
while True:
    text = input()
    if len(text) > 0:
        everything += text
    else:
        break

pattern = r"\d+"
matches = re.findall(pattern, everything)

print(*matches)
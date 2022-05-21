import re

text = input()
pattern = r"\b(_)([A-Za-z\d]+)"
matches = re.finditer(pattern, text)
results = [match[2] for match in matches]

print(','.join(results))

for _ in range(times):
    text = input()
    if re.match(pattern, text):
        matches = re.findall(pattern, text)
        if matches[0] is not None:
            print(f"{matches[1]: } ")
        else:
            print(f"{matches[4]: }")
    else:
        print("Valid message not found!")
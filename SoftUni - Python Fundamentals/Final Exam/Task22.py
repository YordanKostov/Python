import re

pattern_one = r"[*](?P<start>[A-Z][a-z][a-z]+)[*]: \[(?P<first>[A-Z]|[a-z])\]\|\[(?P<second>[A-Z]|[a-z])\]\|\[(?P<third>[A-Z]|[a-z])\]\|$"
pattern_two = r"[@](?P<start>[A-Z][a-z][a-z]+)[@]: \[(?P<first>[A-Z]|[a-z])\]\|\[(?P<second>[A-Z]|[a-z])\]\|\[(?P<third>[A-Z]|[a-z])\]\|$"
times = int(input())

for _ in range(times):
    text = input()
    if re.search(pattern_two, text):
        match = re.search(pattern_two, text)
        obj = match.groupdict()
        print(f"{obj['start']}: {ord(obj['first'])} {ord(obj['second'])} {ord(obj['third'])}")
    elif re.search(pattern_one, text):
        match = re.search(pattern_one, text)
        obj = match.groupdict()
        print(f"{obj['start']}: {ord(obj['first'])} {ord(obj['second'])} {ord(obj['third'])}")
    else:
        print("Valid message not found!")
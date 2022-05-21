number = int(input())
s1 = set()
s2 = set()
longest = []

for _ in range(number):
    ranges = input().split("-")
    first_range = ranges[0].split(",")
    second_range = ranges[1].split(",")
    first_start = int(first_range[0])
    first_end = int(first_range[1])
    second_start = int(second_range[0])
    second_end = int(second_range[1])
    for index in range(first_start, first_end + 1):
        s1.add(index)
    for index in range(second_start, second_end + 1):
        s2.add(index)
    current = s1.intersection(s2)
    if len(current) > len(longest):
        longest = list(current)
    s1.clear()
    s2.clear()

print(f"Longest intersection is {longest} with length {len(longest)}")

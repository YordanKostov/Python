words = input().split()
first = words[0]
second = words[1]
total_sum = 0

if len(first) > len(second):
    temp = first
    first = second
    second = temp

for index in range(len(first)):
    total_sum += ord(first[index]) * ord(second[index])
if len(first) != len(second):
    for index in range(len(first), len(second)):
        total_sum += ord(second[index])

print(total_sum)
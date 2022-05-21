names = [x for x in input().split()]
jumps = int(input())

while len(names) > 1:
    count = jumps
    while count > 1:
        temp = names[0]
        names.pop(0)
        names.append(temp)
        count -= 1
    names.pop(0)

print(f'Last is {names[0]}')
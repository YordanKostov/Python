factor = int(input())
count = int(input())
new_list = []
for index in range(factor, count * factor + 1, factor):
    new_list.append(index)

print(new_list)
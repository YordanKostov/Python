gifts = input().split()

command = ''
while True:
    command = input()
    command_list = command.split(' ')
    if command == "No Money":
        break
    elif command.__contains__('OutOfStock'):
        for index in range(len(gifts)):
            if gifts[index] == command_list[1]:
                gifts[index] = 'None'
    elif command.__contains__('Required'):
        if int(command_list[2]) < len(gifts):
            gifts[int(command_list[2])] = command_list[1]
    elif command.__contains__('JustInCase'):
        gifts.pop()
        gifts.append(command_list[1])

for i in range(len(gifts)):
    if gifts[i] == 'None':
        continue
    else:
        print(gifts[i], end=' ')

width = int(input())
length = int(input())

pieces = width * length

while True:
    cut = input()
    if cut == 'STOP':
        print(f"{pieces} pieces are left.")
        break
    pieces -= int(cut)
    if pieces <= 0:
        print(f'No more cake left! You need {abs(pieces)} pieces more.')
        break
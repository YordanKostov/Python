bees = int(input())
health = int(input())
attack = int(input())

while True:
    bees -= attack
    if bees < 100:
        if bees < 0:
            print('The bear stole the honey! Bees left 0.')
        else:
            print(f'The bear stole the honey! Bees left {bees}.')
        break
    health -= bees * 5
    if health <= 0:
        print(f'Beehive won! Bees left {bees}.')
        break
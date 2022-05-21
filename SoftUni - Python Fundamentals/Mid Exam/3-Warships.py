status_pirate = [int(x) for x in input().split('>')]
status_warship = [int(x) for x in input().split('>')]
max_health = int(input())
command = input().split()
over = False
total = 0

while command[0] != 'Retire':
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                over = True
                break
    elif command[0] == 'Defend':
        start = int(command[1])
        end = int(command[2])
        damage = int(command[3])
        if 0 <= start < len(status_pirate) or 0 <= end < len(status_pirate):
            for index in range(start, end + 1):
                status_pirate[index] -= damage
                if status_pirate[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    over = True
                    break
    elif command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate):
            status_pirate[index] += health
            if status_pirate[index] > max_health:
                status_pirate[index] = max_health
    elif command[0] == 'Status':
        needs_repairing = max_health * 0.2
        for section in status_pirate:
            if section < needs_repairing:
                total += 1
        print(f"{total} sections need repair.")

    command = input().split()

if not over:
    pirates = sum(status_pirate)
    warship = sum(status_warship)
    print(f'Pirate ship status: {pirates}')
    print(f'Warship status: {warship}')

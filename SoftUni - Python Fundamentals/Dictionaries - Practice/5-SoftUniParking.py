n = int(input())
registered_cars = {}

for index in range(n):
    command = input().split()
    if command[0] == 'register':
        if command[1] not in registered_cars:
            registered_cars[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[2]}")
    elif command[0] == 'unregister':
        if command[1] not in registered_cars:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            del registered_cars[command[1]]

for value in registered_cars:
    print(f"{value} => {registered_cars[value]}")
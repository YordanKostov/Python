n = int(input())
bomb_coordinates = int(input())
matrix = []
bombs = []
for _ in range(bomb_coordinates):
    bombs.append(list(input()))

print(bombs)
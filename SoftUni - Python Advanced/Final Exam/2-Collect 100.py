from math import floor

n = int(input())
matrix = []
player_row = 0
player_col = 0
coins = 0
moves = []


def in_bound(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True


for rows in range(n):
    matrix.append(input().split())

for rows in range(n):
    for cols in range(n):
        if matrix[rows][cols] == 'P':
            player_row = rows
            player_col = cols
            break

while coins < 100:
    command = input()
    if command == "up":
        player_row -= 1
        if not in_bound(player_row, player_col):
            print(f"Game over! You've collected {floor(coins / 2)} coins.")
            break
        if matrix[player_row][player_col] != "X" and in_bound(player_row, player_col):
            coins += int(matrix[player_row][player_col])
            moves.append([player_row, player_col])
        else:
            print(f"Game over! You've collected {floor(coins/2)} coins.")
            break
    if command == "down":
        player_row += 1
        if not in_bound(player_row, player_col):
            print(f"Game over! You've collected {floor(coins / 2)} coins.")
            break
        if matrix[player_row][player_col] != "X":
            coins += int(matrix[player_row][player_col])
            moves.append([player_row, player_col])
        else:
            print(f"Game over! You've collected {floor(coins/2)} coins.")
            break
    if command == "right":
        player_col += 1
        if not in_bound(player_row, player_col):
            print(f"Game over! You've collected {floor(coins / 2)} coins.")
            break
        if matrix[player_row][player_col] != "X" and in_bound(player_row, player_col):
            coins += int(matrix[player_row][player_col])
            moves.append([player_row, player_col])
        else:
            print(f"Game over! You've collected {floor(coins/2)} coins.")
            break
    if command == "left":
        player_col -= 1
        if not in_bound(player_row, player_col):
            print(f"Game over! You've collected {floor(coins / 2)} coins.")
            break
        if matrix[player_row][player_col] != "X" and in_bound(player_row, player_col):
            coins += int(matrix[player_row][player_col])
            moves.append([player_row, player_col])
        else:
            print(f"Game over! You've collected {floor(coins/2)} coins.")
            break

if coins > 100:
    print(f"You won! You've collected {coins} coins.")
print('Your path: ')
for move in moves:
    print(move)
cards = input()
my_list = cards.split(' ')
team_a = 11
team_b = 11

for player in my_list:
    if player.__contains__("A"):
        team_a -= 1
    elif player.__contains__("B"):
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break

print(f'Team A - {team_a}; Team B - {team_b}')
if team_a < 7 or team_b < 7:
    print('Game was terminated')
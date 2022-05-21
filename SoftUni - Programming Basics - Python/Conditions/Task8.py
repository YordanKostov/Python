price_of_trip = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

winnings = puzzles * 2.60 + talking_dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2
total_number = puzzles + talking_dolls + teddy_bears + minions + trucks

if total_number >= 50:
    winnings = winnings - (winnings * 0.25)

rent = winnings * 0.1
winnings = winnings - rent
money_left = abs(winnings - price_of_trip)

if winnings >= price_of_trip:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')

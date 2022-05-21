intellect = int(input())
power = int(input())
gender = input()
bee = ''

if intellect >= 80 and power >= 80 and gender == 'female':
    bee = 'Queen Bee'
elif intellect >= 80:
    bee = 'Repairing Bee'
elif intellect >= 60:
    bee = 'Cleaning Bee'
elif power >= 80 and gender == 'male':
    bee = "Drone Bee"
elif power >= 60:
    bee = 'Guard Bee'
else:
    bee = 'Worker Bee'

print(bee)
guest = input()
s = set()
while guest != 'PARTY':
    s.add(guest)
    guest = input()

guest = input()
while guest != 'END':
    s.remove(guest)
    guest = input()

s = sorted(s)
print(len(s))
print("\n".join(s))
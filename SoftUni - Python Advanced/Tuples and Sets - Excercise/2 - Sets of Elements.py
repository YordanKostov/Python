length = input().split()
s1 = set(input() for _ in range(int(length[0])))
s2 = set(input() for _ in range(int(length[1])))

print("\n".join(s1 & s2))
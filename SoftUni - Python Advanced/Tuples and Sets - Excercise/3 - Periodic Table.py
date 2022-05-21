number = int(input())
s = set()
for _ in range(number):
    s.update(x for x in input().split())

print("\n".join(s))
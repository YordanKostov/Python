from collections import deque

males = [int(num) for num in input().split() if -100 <= int(num) <= 100]
females = deque([int(num) for num in input().split() if -100 <= int(num) <= 100])
matches = 0

while len(females) > 0 and len(males) > 0:
    if females[0] <= 0:
        females.popleft()
        continue
    elif males[-1] <= 0:
        males.pop()
        continue
    elif females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    elif males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    if females[0] != males[-1]:
        males[-1] -= 2
        females.popleft()
    else:
        females.popleft()
        males.pop()
        matches += 1
females = list(map(str, females))

print(f"Matches: {matches}")
if len(males) > 0:
    males = list(map(str, males))
    print(f"Males left: {', '.join(males.__reversed__())}")
else:
    print(f"Males left: none")
if len(females) > 0:
    print(f"Females left: {', '.join(females)}")
else:
    print("Females left: none")
expres = str(input())
opening_bracket = []
values = []

for index in range(len(expres)):
    if expres[index] == '(':
        opening_bracket.append(index)
    elif expres[index] == ')':
        seq = ''
        for num in range(opening_bracket.pop(), index + 1):
            seq += expres[num]
        values.append(seq)

for value in values:
    print(value)
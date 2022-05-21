parentheses = input()
opened = ["{", "[", "("]
closed = ["}", "]", ")"]
balanced = True
stack = []

for parant in parentheses:
    if parant in opened:
        stack.append(parant)
    elif parant in closed:
        pos = closed.index(parant)
        if ((len(stack) > 0) and
                (opened[pos] == stack[len(stack) - 1])):
            stack.pop()
        else:
            balanced = False

if len(stack) == 0:
    balanced = True
else:
    balanced = False

if balanced:
    print("YES")
else:
    print("NO")

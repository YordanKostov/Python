def operate(command, *args):
    args = [int(x) for x in args]
    if command == "+":
        return sum(args)
    elif command == "-":
        subtract = 0
        for number in args:
            subtract -= number
        return subtract
    elif command == "*":
        multiply = 1
        for number in args:
            multiply *= number
        return multiply
    elif command == "/":
        divide = 0
        for index in range(len(args)):
            if index == 0:
                divide += args[index]
            else:
                divide /= args[index]
        return f"{divide:.2f}"


print(operate("/", 1, 2, 3))

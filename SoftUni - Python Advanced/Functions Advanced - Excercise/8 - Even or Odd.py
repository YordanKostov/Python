def even_odd(*args):
    command = args[-1]
    if command == 'odd':
        result = filter(lambda x: x % 2 != 0, args[0:-1])
    else:
        result = filter(lambda x: x % 2 == 0, args[0:-1])
    return list(result)


print(even_odd(1, 2, 3, 4, 5, 6, "odd"))

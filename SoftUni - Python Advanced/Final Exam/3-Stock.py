def stock_availability(boxes, command, *args):
    if command == "delivery":
        for arg in args:
            boxes.append(arg)
    if command == "sell":
        if len(args) > 0 and contains_only_integers(args):
            for _ in range(int(args[0])):
                if len(boxes) > 0:
                    boxes.pop(0)
        elif len(args) == 0:
            boxes.pop(0)
        elif len(args) > 0 and contains_only_strings(args):
            for arg in args:
                while arg in boxes:
                    boxes.remove(arg)
    return boxes


def contains_only_integers(tup):
    for item in tup:
        if not isinstance(item, int):
            return False
    return True


def contains_only_strings(tup):
    for item in tup:
        if not isinstance(item, str):
            return False
    return True


print(stock_availability(["chocolate", "chocolate", "banana", "banana", "chocolate"], "sell", "chocolate", "banana"))

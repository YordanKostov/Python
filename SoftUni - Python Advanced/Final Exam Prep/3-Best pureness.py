def best_list_pureness(numbers, rotations):
    best_rotation = 0
    max_pureness = 0
    for rot in range(rotations + 1):
        pureness = 0
        for index in range(len(numbers)):
            pureness += (index * numbers[index])
        if pureness > max_pureness:
            max_pureness = pureness
            best_rotation = rot
        numbers.insert(0, numbers.pop(len(numbers) - 1))

    return f"Best pureness {max_pureness} after {best_rotation} rotations"


print(best_list_pureness([7, 9, 2, 5, 3, 4], 3))

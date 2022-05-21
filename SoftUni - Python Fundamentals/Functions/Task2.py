num1 = int(input())
num2 = int(input())
num3 = int(input())


def sum_numbers(number1, number2):
    return number1 + number2


def subtract(number, number3):
    return number - number3


def add_and_subtract(number1, number2, number3):
    return subtract(sum_numbers(number1, number2), number3)


print(add_and_subtract(num1, num2, num3))

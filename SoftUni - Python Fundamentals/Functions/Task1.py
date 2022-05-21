def smallest_number(number1, number2, number3):
    if number1 <= number2 and number1 <= number3:
        return number1
    elif number2 <= number3 and number2 <= number1:
        return number2
    else:
        return number3


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_number(num1, num2, num3))

N1 = int(input())
N2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = N1 + N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "-":
    result = N1 - N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "*":
    result = N1 * N2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{N1} {operator} {N2} = {result} - {even_or_odd}")
elif operator == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} {operator} {N2} = {result:.2f}")
elif operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} {operator} {N2} = {result}")  (input())
n2 = int(input())
operator = input()
odd_even = ''

if abs(n1 - n2) % 2 == 0:
    odd_even = 'even'
else:
    odd_even = 'odd'

if operator == '-':
    if abs(n1 - n2) % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    print(f'{n1} - {n2} = {abs(n1 - n2)} - {odd_even}')
elif operator == '+':
    if abs(n1 + n2) % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    print(f'{n1} + {n2} = {abs(n1 + n2)} - {odd_even}')
elif operator == '*':
    if abs(n1 * n2) % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    print(f'{n1} * {n2} = {abs(n1 * n2)} - {odd_even}')
elif operator == '%':
    if n1 == 0:
        print(f'Cannot divide {n2} by zero')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        print(f'{n1} % {n2} = {abs(n1 % n2):.2f}')
elif operator == '/':
    if n1 == 0:
        print(f'Cannot divide {n2} by zero')
    elif n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        print(f'{n1} / {n2} = {abs(n1 / n2):.2f}')

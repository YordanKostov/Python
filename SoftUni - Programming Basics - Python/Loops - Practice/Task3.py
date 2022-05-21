import sys

number = int(input())
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

for index in range(1, number + 1):
    current_number = float(input())
    if index % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number

if odd_max == -sys.maxsize:
    odd_max = str('No')
    odd_min = str('No')
if even_max == -sys.maxsize:
    even_max = str('No')
    even_min = str('No')

print(f'OddSum={odd_sum:.2f},')
if odd_min != 'No':
    print(f'OddMin={odd_min:.2f},')
else:
    print(f"OddMin={odd_min},")
if odd_max != 'No':
    print(f'OddMax={odd_max:.2f},')
else:
    print(f"OddMax={odd_max},")
print(f'EvenSum={even_sum:.2f},')
if even_min != 'No':
    print(f'EvenMin={even_min:.2f},')
else:
    print(f"EvenMin={even_min},")
if even_max != 'No':
    print(f'EvenMax={even_max:.2f}')
else:
    print(f"EvenMax={even_max}")

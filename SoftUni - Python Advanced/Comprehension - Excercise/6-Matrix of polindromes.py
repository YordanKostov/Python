rows, cols = [int(x) for x in input().split()]
poli = [[f"{chr(num)}{chr(nested_num)}{chr(num)}"for nested_num in range(num, num+cols)]for num in range(97, 97+rows)]

print(*[" ".join(el) for el in poli], sep="\n")
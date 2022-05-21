number_of_tables = int(input())
length_of_tables = float(input())
width_of_tables = float(input())

area_of_rectangle = number_of_tables * (length_of_tables + 2 * 0.30) * (width_of_tables + 2 * 0.30)
area_of_square = number_of_tables * (length_of_tables /2 ) * (length_of_tables / 2)

price_in_dollars = area_of_rectangle * 7 + area_of_square * 9
price_in_lev = price_in_dollars * 1.85

print(f'{price_in_dollars:.2f} USD')
print(f'{price_in_lev:.2f} BGN')
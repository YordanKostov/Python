number_of_dogs = int(input())
other_animals = int(input())
price_for_dogs = number_of_dogs * 2.50
price_for_others = other_animals * 4
final_price = price_for_dogs + price_for_others

print(f'{final_price:.2f} lv.')
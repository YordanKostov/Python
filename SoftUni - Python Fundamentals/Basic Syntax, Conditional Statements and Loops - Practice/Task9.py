budget = float(input())
price_flour = float(input())

price_eggs = price_flour * 0.75
price_milk = price_flour + (price_flour * 0.25)
count_colored = 0
count_cozonacs = 0
cost_ingredients = price_flour + price_eggs + (price_milk / 4)

while budget > cost_ingredients:
    budget -= cost_ingredients
    count_cozonacs += 1
    count_colored += 3
    if count_cozonacs % 3 == 0:
        count_colored -= count_cozonacs - 2

print(f"You made {count_cozonacs} cozonacs! Now you have {count_colored} eggs and {budget:.2f}BGN left.")

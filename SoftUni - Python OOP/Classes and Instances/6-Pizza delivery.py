class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients and self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * ingredient_price

    def format_output(self):
        return ", ".join([f"{key}: {value}" for key, value in self.ingredients.items()])

    def make_order(self):
        self.ordered = True
        res = f"You've ordered pizza {self.name} prepared with {self.format_output()} and the price will be {self.price}lv."
        return res


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

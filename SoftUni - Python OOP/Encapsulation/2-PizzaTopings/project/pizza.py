class Pizza:
    __name = str
    __toppings = dict
    __toppings_capacity = int

    def __init__(self, name, dough, toppings_capacity):
        self.__toppings_capacity = toppings_capacity
        self.__name = name
        self.__dough = dough
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    @property
    def toppings(self):
        return self.__toppings

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @name.setter
    def name(self, name):
        self.__name = name

    @dough.setter
    def dough(self, dough):
        self.__dough = dough

    @toppings.setter
    def toppings(self, toppings):
        self.__toppings = toppings

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping):
        if self.__toppings_capacity > len(self.__toppings):
            if topping.topping_type not in self.__toppings:
                self.__toppings[topping.topping_type] = 0
            self.__toppings[topping.topping_type] += topping.weight

        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        weight_of_ingredients = self.__dough.weight + sum(self.__toppings.values())
        return weight_of_ingredients

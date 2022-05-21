class Topping:
    __topping_type = str
    __weight = float

    def __init__(self, toppings_type, weight):
        self.__topping_type = toppings_type
        self.__weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @property
    def weight(self):
        return self.__weight

    @topping_type.setter
    def topping_type(self, topping_type):
        self.__topping_type = topping_type

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

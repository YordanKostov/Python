class Dough:
    __flour_type = str
    __baking_technique = str
    __weight = float

    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

    @flour_type.setter
    def flour_type(self, flour_type):
        self.__flour_type = flour_type

    @baking_technique.setter
    def baking_technique(self, baking_technique):
        self.__baking_technique = baking_technique

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

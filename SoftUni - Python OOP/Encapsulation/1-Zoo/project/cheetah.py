class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs(self):
        return 600

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
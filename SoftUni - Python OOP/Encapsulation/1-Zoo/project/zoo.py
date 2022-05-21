class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            return f"{animal.name} the {type(animal)} added to the zoo"
        elif price > self.__budget and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker)} hired successfully"
        else:
            return "Not enough space for worker"

    def pay_workers(self):
        salaries = sum([w.salary() for w in self.workers])
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def tend_animals(self):
        tend = sum([a.get_needs() for a in self.animals])
        if tend <= self.__budget:
            self.__budget -= tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        res += f"----- {len(lions)} Lions\n"
        for lion in lions:
            res += lion.__repr__()
        res += f"----- {len(tigers)} Tigers\n"
        for tiger in tigers:
            res += tiger.__repr__()
        res += f"----- {len(cheetahs)} Cheetahs\n"
        for cheetah in cheetahs:
            res += cheetah.__repr__()
        return res

    def worker_status(self):
        keepers = [a for a in self.animals if a.__class__.__name__ == "Keeper"]
        caretakers = [a for a in self.animals if a.__class__.__name__ == "Caretaker"]
        vets = [a for a in self.animals if a.__class__.__name__ == "Vet"]
        res = f"You have {len(self.workers)} workers"
        res += f"----- {len(keepers)} Keepers\n"
        for keeper in keepers:
            res += keeper.__repr__()
        res += f"----- {len(caretakers)} Caretakers\n"
        for caretaker in caretakers:
            res += caretaker.__repr__()
        res += f"----- {len(vets)} Vets\n"
        for vet in vets:
            res += vet.__repr__()
        return res

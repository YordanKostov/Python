class Inventory:
    def __init__(self, capacity):
        self.startcapacity = capacity
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            print('not enough room in inventory')

    def get_capacity(self):
        return self.startcapacity

    def __repr__(self):
        return f"Items: {self.items}.\nCapacity left: {self.__capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)

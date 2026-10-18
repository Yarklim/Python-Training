class User:
    def __init__(self, name, age, status='offline'):
        self.name = name
        self.age = age
        self.status = status

    def change_status(self):
        if self.status == 'offline':
            self.status = 'online'
        else:
            self.status = 'offline'


user1 = User('Alex', 28)

print(user1.__dict__)  # {'name': 'Alex', 'age': 28, 'status': 'offline'}

user1.change_status()

print(user1.__dict__)  # {'name': 'Alex', 'age': 28, 'status': 'online'}


# ------------------------------------------------------
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_total(self):
        if not self.items:
            return 0

        return sum(item.price for item in self.items)

    def show_items(self):
        if not self.items:
            print('Cart is empty')
            return

        for item in self.items:
            print(f'- {item.name}: ${item.price}')


cart1 = Cart('Alex')
cart1.add_item(Item('IPhone', 1500))
cart1.add_item(Item('MacBook Pro', 3500))

cart1.show_items()
print(f'Total: ${cart1.get_total()}')


# ------------------------------------------

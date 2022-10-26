

class ShoppingCart:

    def __init__(self):
        self.items = []
        # self.value = 0

    def add_item(self, name, price, qty):
        self.items.append((name, price, qty))
        # self.value = self.value + (price * qty) # option 1

    def remove_item(self, name):
        ...

    # option 2
    @property
    def value(self):
        return sum([ item[1] * item[2] for item in self.items ])


cart = ShoppingCart()
cart.add_item("eggs", 7.99, 1)
cart.add_item("oranges", 3.99, 3)

print(cart.value)
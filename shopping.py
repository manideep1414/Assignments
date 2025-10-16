class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def __str__(self):
        return f"{self.name}: ₹{self.price} × {self.qty} = ₹{self.price * self.qty}"

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for i in self.items:
            if i.name == item.name:
                i.qty += item.qty
                return
        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return
        print(f"Item '{name}' not found in cart.")
            
    def get_total(self):
        return sum(i.price * i.qty for i in self.items)

    def __str__(self):
        if not self.items:
            return "Cart is empty."
        return "\n".join(str(i) for i in self.items) + f"\nTotal: ₹{self.get_total()}"

cart = Cart()
cart.add_item(Item("Pen", 10, 3))
cart.add_item(Item("Notebook", 50, 2))
print(cart)
print("--------------------------------")
cart.add_item(Item("Pen", 10, 2))
print(cart)
print("--------------------------------")
cart.remove_item("Notebook")
print(cart)

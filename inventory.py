class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: ₹{self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = []  # list to store Product objects

    def add(self, product):
        self.products.append(product)

    def total(self):
        return sum(p.price * p.quantity for p in self.products)

    def display(self):
        if not self.products:
            print("No products in inventory.")
            return
        for p in self.products:
            print(p)  # uses Product.__str__ method
        print(f"Total Inventory Value: ₹{self.total()}")

p1 = Product("Pen", 10, 50)
p2 = Product("Book", 50, 20)
p3 = Product("Bag", 1000, 2)

inv = Inventory()
inv.add(p1)
inv.add(p2)
inv.add(p3)

inv.display()

print("-----------------")
p4 = Product("Laptop",25000,2)
inv.add(p4)
inv.display()
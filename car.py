class Car:
    def display(self):
        print(f"Brand: {self.brand}\n   Model: {self.model}")


c1 = Car()
c2 = Car()
c3 = Car()

c1.brand = "Maruthi Suzuki"
c1.model = "Brezza"
c2.brand= "Toyota"
c2.model= "Fortuner"
c3.brand= "Mahindra"
c3.model= "XUV700"

c1.display()
c2.display()
c3.display()
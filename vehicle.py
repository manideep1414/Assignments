class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def vehicle_info(self):
        return f"Vehicle: {self.make} {self.model} ({self.year})"

    def __str__(self):
        return self.vehicle_info()


class Car(Vehicle):
    def __init__(self, make, model, year, gear_type):
        super().__init__(make, model, year)
        self.gear_type = gear_type

    def vehicle_info(self):
        return f"Car: {self.make} {self.model} ({self.year}), Gear Type: {self.gear_type}"


class Bike(Vehicle):
    def __init__(self, make, model, year, engine_cc):
        super().__init__(make, model, year)
        self.engine_cc = engine_cc

    def vehicle_info(self):
        return f"Bike: {self.make} {self.model} ({self.year}), Engine: {self.engine_cc}cc"

v1 = Vehicle("Tata", "Nexon", 2023)
c1 = Car("Hyundai", "Creta", 2022, "MT")
b1 = Bike("Yamaha", "R15", 2021, 155)
c2 = Car("Toyota","Fortuner",2015,"AT")

print(v1)
print(c1)
print(b1)
print(c2)
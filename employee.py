class Employee:
    company_name = "Cloud Orbit"

    def __init__(self, name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def hike(self, percent):
        new_salary = self.salary + (percent / 100) * self.salary
        print(f"Salary before hike: ₹{self.salary:.2f}")
        self.salary = new_salary
        print(f"Salary after hike: ₹{self.salary:.2f}")
         

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₹{self.salary}")
        print(f"Company: {Employee.company_name}")

e1 = Employee("A", "Manager",100000)
e2 = Employee("B", "HR", 50000)
e3 = Employee("C", "Intern", 15000)

e1.display()
print("-----------")
e2.display()
print("-----------")
e3.display()
print("-----------")
e1.hike(10)
e1.display()
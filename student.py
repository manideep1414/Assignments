class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        if 0 <= mark <= 100:
            self.marks[subject] = mark
        else:
            print(f"❌ Invalid mark for {self.name}: {mark}")

    def display_info(self):
        print(f"\nStudent Name: {self.name}")
        if not self.marks:
            print("❌ No marks added yet.")
            return
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        total = sum(self.marks.values())
        average = total / len(self.marks)
        print(f"Total: {total}")
        print(f"Average: {average:.2f}")


students = []

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")

students.extend([s1, s2, s3])

s1.add_mark("Math", 85)
s1.add_mark("Physics", 90)
s2.add_mark("Math", 78)
s3.add_mark("English", 88)
s3.add_mark("Biology", 92)

for student in students:
    student.display_info()

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add(self, title):
        self.books.append(Book(title))

    def borrow(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print(f"Borrowed '{title}'") 
                return
        print(f"'{title}' not available")

    def return_book(self, title):
        for b in self.books:
            if b.title == title and not b.available:
                b.available = True
                print(f"Returned '{title}'") 
                return
        print(f"Already returned '{title}'")

    def available_books(self):
        for b in self.books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.title} ({status})")

lib = Library()
lib.add("AIML")
lib.add("Python")
lib.available_books()

print("------------")
lib.borrow("AIML")
lib.borrow("Python")
lib.available_books()

print("------------")
lib.return_book("AIML")
lib.available_books()

lib.return_book("AIML")
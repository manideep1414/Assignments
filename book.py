class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print(f"Title={self.title}",f"Author={self.author}",f"Price={self.price}")
        
    def discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amount
        print(f"✅ Discount of {percent}% applied. New Price: ₹{self.price:.2f}")
    
            
          
b1=Book("Wings of Fire","Dr.APJ Abdul Kalam",200)
b2=Book("The Pschology of Money","Morgan Housel",300)
b3=Book("The Diary of a Young Girl","Anne Frank",150)

b1.display()
b2.display()   
b3.display()

b3.discount(10)
b3.display()               
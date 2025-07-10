"""class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product : {self.name}, Price: ${self.price:.2f}")

product1 = Product("Laptop", 999.99)
product2 = Product("Smartphone", 499.49)

product1.display()
product2.display()"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product : {self.name}, Price: {self.price:.2f}/-")

name1 = input("first product: ")
price1 = float(input("price: "))

name2 = input("second product: ")
price2 = float(input("price: "))

product1 = Product(name1, price1)
product2 = Product(name2, price2)

product1.display()
product2.display()


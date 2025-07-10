from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using credit card.")
class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


'''a = CreditCard()
a.pay(100)

b = DebitCardPayment()
b.pay(200)

c = PayPalPayment()
c.pay(150)'''

print("Select Payment Method:")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = input("Enter choice (1/2/3): ")
amount = float(input("Enter amount to pay: "))

if choice == "1":
    payment = CreditCard()
elif choice == "2":
    payment = DebitCard()
elif choice == "3":
    payment = UPI()
else:
    print("Invalid choice!")
    exit()






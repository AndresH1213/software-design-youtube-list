"""
If you have objects in a program you should be able to
replace those objects with instances of their subtypes
or subclasses without altering the correctness of the program
"""
from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    # security_code if different so we remove it from the abstract method
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self,order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self,order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address
    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = DebitPaymentProcessor("212313")
processor.pay(order)

processor2 = PaypalPaymentProcessor("email@testing.com");
processor2.pay(order)


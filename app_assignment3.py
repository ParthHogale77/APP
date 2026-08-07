from abc import ABC, abstractmethod


# Stratergy Interface
class PaymentStratergy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Stratergy 1
class Creditcardpayment(PaymentStratergy):
    def pay(self, amount):
        print("payment of ${amount} processed using Credit card")


# Concrete Stratergy 2
class Deditcardpayment(PaymentStratergy):
    def pay(self, amount):
        print("payment of ${amount} processed using Dedit card")


# Concrete Stratergy 3
class Upipayment(PaymentStratergy):
    def pay(self, amount):
        print("payment of ${amount} processed using UPI")


# Context class

class PaymentProcessor:
    def __init__(self, stratergy=None):
        self.stratergy = stratergy

    def set_stratergy(self, stratergy):
        self.stratergy = stratergy


def process_payment(self, amount):
    if self.stratergy is None:
        print("select a payment Mode")
    else:
        self.stratergy.pay(amount)


# Driver Code
processor = PaymentProcessor()

while True:
    print("---------Payment processing System--------------")
    print("1.Credit Card")
    print("2.Dedit Card")
    print("3.UPI Payment")
    print("Exit")

    choice = int(input("Enter your choice"))
    amount = float(input("enter the amount"))
    if choice == 1:
        processor.set_stratergy(Creditcardpayment)


    elif choice == 2:
        processor.set_stratergy(Deditcardpayment)


    elif choice == 3:
        processor.set_stratergy(Upipayment)


    elif choice == 4:
        print("thanks you for using payment system")
    else:
        print("invalid choice")
        continue

    processor.process_payment(amount)

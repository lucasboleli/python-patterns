from .payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"paid with credit card {amount}")
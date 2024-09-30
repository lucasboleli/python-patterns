from .payment import Payment

class PaypalPayment(Payment):
    def pay(self, amount: float):
        print("paid with paypal "+amount)
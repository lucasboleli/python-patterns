from .payment import Payment
class GooglePayment(Payment):
    def pay(self, amount: float):
        print("paid with google " + str(amount))
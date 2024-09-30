from payment_methods.payment import Payment
class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print("paid with credit card "+amount)
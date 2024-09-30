from payment_factory import PaymentFactory

factory = PaymentFactory()
payment = factory.create("GooglePayment")
payment.pay(1)
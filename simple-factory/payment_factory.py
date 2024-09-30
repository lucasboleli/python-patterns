from inspect import getmembers, isabstract, isclass
import payment_methods


class PaymentFactory(object):
    payment_implementations={}

    def __init__(self):
        self.load_payment_methods()

    def load_payment_methods(self):
        implementations = getmembers(payment_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_implementations[name] = _type
    
    def create(self, payment_type:str):
        if payment_type in self.payment_implementations:
            return self.payment_implementations[payment_type]()
        else:
            raise ValueError(payment_type + " invalid type")
from abc import ABC, abstractmethod


# Adaptee / existing component
class PaymentGateway:
    def charge_cents(self, cents):
        print(f"charging {cents} cents")


# Target interface
class PaymentProvider(ABC):
    @abstractmethod
    def pay(self, amount_chf):
        pass


# Adapter
class PaymentAdapter(PaymentProvider):
    def __init__(self, gateway):
        self.gateway = gateway

    def pay(self, amount_chf):
        cents = int(amount_chf * 100)
        self.gateway.charge_cents(cents)


# Client
class CheckoutService:
    def __init__(self, payment_provider):
        self.payment_provider = payment_provider

    def place_order(self, amount_chf):
        self.payment_provider.pay(amount_chf)
        print("order confirmed")


def main():
    gateway = PaymentGateway()
    adapter = PaymentAdapter(gateway)
    checkout = CheckoutService(adapter)
    checkout.place_order(19.50)


if __name__ == "__main__":
    main()
from abc import ABC, abstractmethod


# Interface / contract
class TaxableItem(ABC):
    def __init__(self, net_price):
        self.net_price = net_price

    @abstractmethod
    def calculate_vat(self):
        pass


# Concrete implementation
class RegularProduct(TaxableItem):
    VAT_RATE = 0.081

    def calculate_vat(self):
        return round(self.net_price * self.VAT_RATE, 2)


# Concrete implementation
class ReducedProduct(TaxableItem):
    VAT_RATE = 0.026

    def calculate_vat(self):
        return round(self.net_price * self.VAT_RATE, 2)


# Concrete implementation
class TaxFreeProduct(TaxableItem):
    def calculate_vat(self):
        return 0.0


# Client
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total_vat(self):
        total = 0.0

        for item in self.items:
            total = total + item.calculate_vat()

        return round(total, 2)


def main():
    cart = ShoppingCart()
    cart.add(RegularProduct(10.0))
    cart.add(ReducedProduct(10.0))
    cart.add(TaxFreeProduct(10.0))
    print(cart.total_vat())


if __name__ == "__main__":
    main()
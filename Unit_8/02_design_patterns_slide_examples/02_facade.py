
# Subsystem
class InventoryService:
    def reserve(self, sku):
        print(f"reserve {sku}")


# Subsystem
class PaymentService:
    def charge(self, customer):
        print(f"charge {customer}")


# Subsystem
class DeliveryService:
    def schedule(self, customer, sku):
        print(f"deliver {sku} to {customer}")


# Facade
class OrderFacade:
    def __init__(self):
        self.inventory = InventoryService()
        self.payments = PaymentService()
        self.delivery = DeliveryService()

    def place_order(self, customer, sku):
        self.inventory.reserve(sku)
        self.payments.charge(customer)
        self.delivery.schedule(customer, sku)


# Client
class WebShopClient:
    def __init__(self, facade):
        self.facade = facade

    def checkout(self):
        self.facade.place_order("Alice", "PIZZA-MARGHERITA")


# Client
class SupportDeskClient:
    def __init__(self, facade):
        self.facade = facade

    def reorder(self):
        self.facade.place_order("Bob", "PIZZA-MARGHERITA")


def main():
    facade = OrderFacade()
    WebShopClient(facade).checkout()
    SupportDeskClient(facade).reorder()


if __name__ == "__main__":
    main()
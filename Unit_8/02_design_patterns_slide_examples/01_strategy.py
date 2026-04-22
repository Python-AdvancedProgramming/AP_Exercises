from abc import ABC, abstractmethod


# Strategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def discount(self, subtotal):
        pass


# Concrete strategy 1
class NoDiscount(DiscountStrategy):
    def discount(self, subtotal):
        return 0.0


# Concrete strategy 2
class PercentageDiscount(DiscountStrategy):
    def discount(self, subtotal):
        if subtotal > 50.0:
            return round(subtotal * 0.10, 2)
        return 0.0


# Concrete strategy 3
class FlatDiscount(DiscountStrategy):
    def discount(self, subtotal):
        if subtotal > 50.0:
            return 5.0
        return 0.0


# Client
class PricingService:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def totals_from_lines(self, line_totals):
        subtotal = round(sum(line_totals), 2)
        discount = self.strategy.discount(subtotal)
        total = round(subtotal - discount, 2)
        return subtotal, discount, total


def main():
    lines = [18.0, 22.0, 19.0]
    pricing = PricingService(NoDiscount())
    print("regular", pricing.totals_from_lines(lines))
    pricing.set_strategy(PercentageDiscount())
    print("percentage", pricing.totals_from_lines(lines))
    pricing.set_strategy(FlatDiscount())
    print("flat", pricing.totals_from_lines(lines))


if __name__ == "__main__":
    main()
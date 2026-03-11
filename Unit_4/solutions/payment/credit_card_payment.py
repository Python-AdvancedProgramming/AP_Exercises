from payment_method import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def __init__(self, amount: float, card_number: str) -> None:
        super().__init__(amount)
        self.card_number = card_number

    @property
    def card_number(self) -> str:
        return self._card_number

    @card_number.setter
    def card_number(self, value: str) -> None:
        if not value:
            raise ValueError("card_number can not be empty")
        self._card_number = str(value)

    def process_payment(self) -> str:
        return f"Processing credit card payment of CHF {self.amount:g}"

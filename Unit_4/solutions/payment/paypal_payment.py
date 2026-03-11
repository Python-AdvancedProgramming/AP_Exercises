from payment_method import PaymentMethod


class PayPalPayment(PaymentMethod):
    def __init__(self, amount: float, email: str) -> None:
        super().__init__(amount)
        self.email = email

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not value:
            raise ValueError("email can not be empty")
        self._email = str(value)

    def process_payment(self) -> str:
        return f"Processing PayPal payment of CHF {self.amount:g}"

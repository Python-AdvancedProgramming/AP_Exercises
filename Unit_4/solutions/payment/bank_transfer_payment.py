from payment_method import PaymentMethod


class BankTransferPayment(PaymentMethod):
    def __init__(self, amount: float, iban: str) -> None:
        super().__init__(amount)
        self.iban = iban

    @property
    def iban(self) -> str:
        return self._iban

    @iban.setter
    def iban(self, value: str) -> None:
        if not value:
            raise ValueError("iban can not be empty")
        self._iban = str(value)

    def process_payment(self) -> str:
        return f"Processing bank transfer of CHF {self.amount:g}"

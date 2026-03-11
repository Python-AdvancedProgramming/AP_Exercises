# OOP Exercise: Payment Processing

In this exercise you will design and implement a small object-oriented payment processing system.  
Different payment methods share common behavior but implement their payment logic differently.

The `solutions/payment` package in the repository contains a working reference implementation; your task is to build your own version from scratch following the requirements below.

> **Note**: Do not copy the solution files directly—this exercise is meant to be solved independently. Once you have finished your implementation, compare it with the provided `solutions/payment` package to see alternate design choices.

## Learning goals

1. Practice designing class hierarchies using **inheritance**.
2. Implement **method overriding** in subclasses.
3. Apply **polymorphism** by calling the same method on different object types.
4. Use **abstract base classes (ABC)** to define required interfaces.
5. Observe how inheritance structures affect program design.

---

## Requirements

You should create the following classes in a new module or package (e.g. `payment.py`):

### `PaymentMethod`
- Implement this class as an **abstract base class**.
- Attributes:
  - `amount` (float) – the payment amount.
- Methods:
  - `process_payment()` – abstract method that must be implemented by subclasses.

The purpose of this class is to define the common interface for all payment types.

---

### `CreditCardPayment`
Subclass of `PaymentMethod`.

- Additional attributes:
  - `card_number` (string)
- Implement `process_payment()` to return a message similar to: ```Processing credit card payment of CHF {self.amount} with {self.card_number}```

---

### `PayPalPayment`
Subclass of `PaymentMethod`.

- Additional attributes:
  - `email` (string)
- Implement `process_payment()` to return a message similar to: ```Processing PayPal payment of CHF {self.amount} with {self.email}```

---

### `BankTransferPayment`
Subclass of `PaymentMethod`.

- Additional attributes:
  - `iban` (string)
- Implement `process_payment()` to return a message similar to: 
```Processing bank transfer of CHF {self.amount} with {self.iban}```

---

## Using polymorphism

Create several payment objects and store them in a list:

```python
payments = [
    CreditCardPayment(50, "1234-5678-9012-3456"),
    PayPalPayment(25, "user@email.com"),
    BankTransferPayment(100, "CH9300762011623852957")
]
```

Iterate over the list and process all payments:
```python
for payment in payments:
    payment.process_payment()
```

## Reflection questions:
* Why is an abstract base class useful in this system?
* What advantage does polymorphism provide here?
* In which situations could multiple inheritance become problematic?

## Optional extensions
### Validation

Add validation rules for some attributes.

Examples:
* Credit card numbers must contain 16 digits.
* IBAN values must start with "CH".

Raise appropriate exceptions when invalid values are provided.

### Logging behavior
Create a class LoggedPayment that logs a message before processing a payment.

Example:
```
Logging payment...
Processing credit card payment of CHF 50
```
Consider how this behavior could be integrated using inheritance.

### Multiple inheritance challenge

Create a class SecureCreditCardPayment that inherits from both:

CreditCardPayment

LoggedPayment

Observe which process_payment() implementation is used and how method resolution order (MRO) affects the behavior.

Override the method if necessary.
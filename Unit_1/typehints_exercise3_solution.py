# -------------------------
# Exercise 3 (short) — Solution
# -------------------------
def apply_discount(price: float, discount: int | float | None) -> float:
    """
    Applies a discount to a price.

    discount:
      - int: percentage (10 means 10%)
      - float: decimal (0.1 means 10%)
      - None: no discount
    """
    if discount is None:
        return price

    if isinstance(discount, int):
        factor = discount / 100.0
    else:  # discount is float here
        factor = discount

    return price * (1 - factor)


if __name__ == "__main__":
    print(apply_discount(100, 4))
    print(apply_discount(100, None))
    print(apply_discount(100, 0.25))

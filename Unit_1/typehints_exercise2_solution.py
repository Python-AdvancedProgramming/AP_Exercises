# -------------------------
# Exercise 2 — Solution
# -------------------------

from typing import Iterable


def search_customers(customers: Iterable[str], keyword: str | None) -> list[str]:
    """
    Returns customers whose name contains keyword (case-insensitive).
    If keyword is None, returns all customers as a list.
    """
    customer_list = list(customers)

    if keyword is None:
        return customer_list

    k = keyword.lower()
    return [c for c in customer_list if k in c.lower()]


if __name__ == "__main__":
    customers = ("Becker", "Nadal", "Federer")
    keyword = "Fed"
    print(search_customers(customers, keyword))

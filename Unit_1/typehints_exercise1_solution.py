# -------------------------
# Exercise 1 — Solution
# -------------------------
def invoice_total(net_amount: float, vat_rate: float | None = None) -> float:
    """
    Returns the invoice total for a net amount.
    If vat_rate is None, no VAT is applied.
    """
    if vat_rate is None:
        return net_amount
    return net_amount * (1 + vat_rate)

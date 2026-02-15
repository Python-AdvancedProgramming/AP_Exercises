def invoice_total(net_amount, vat_rate=None):
    """
    net_amount: net price
    vat_rate: VAT rate like 0.077 (optional). If None, no VAT is added.
    """
    if vat_rate is None:
        return net_amount
    return net_amount * (1 + vat_rate)

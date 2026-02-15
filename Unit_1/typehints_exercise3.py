def apply_discount(price, discount):
    """
    price: original price
    discount:
        - int (percentage, e.g. 10 means 10%)
        - float (decimal, e.g. 0.1 means 10%)
        - None (no discount)
    """
    if discount is None:
        return price
 
    # TODO: handle int vs float correctly
 

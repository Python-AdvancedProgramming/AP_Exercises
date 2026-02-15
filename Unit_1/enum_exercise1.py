def display_cart(items: list[tuple[str, float]]) -> None:
    """
    Display cart items with numbers and total.
    
    Example output:
    1. Laptop - CHF999.99
    2. Mouse - CHF29.99
    Total: CHF1029.98
    """
    # Your code here using enumerate()


# Test with:
cart = [("Laptop", 999.99), ("Mouse", 29.99), ("Keyboard", 79.99)]
display_cart(cart)

def search_customers(customers, keyword):
    """
    Returns customers whose name contains keyword (case-insensitive).
    """
    keyword = keyword.lower()
    result = []
    for c in customers:
        if keyword in c.lower():
            result.append(c)
    return result
 
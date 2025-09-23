def calcDiscount(price, discount):
    if not isinstance(price, (int, float)):
        return 0
    if not isinstance(discount, (int, float)):
        return 0
    return round(price * (1 - discount / 100), 2)
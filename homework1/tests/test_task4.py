import pytest

def calcDiscount(price, discount):
    if not isinstance(price, (int, float)):
        return 0
    if not isinstance(discount, (int, float)):
        return 0
    return round(price * (1 - discount / 100), 2)

def testInt():
    assert calcDiscount(100,10) == 90

def testFloat():
    assert calcDiscount(100.0,10.0) == 90.0

def testMixed():
    assert calcDiscount(130,10.5) == 116.35
    assert calcDiscount(100.67,10) == 90.6


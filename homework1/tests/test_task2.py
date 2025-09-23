import pytest

intExample = 1 + 1

floatExample = 2.3 + 2.5

stringExample = "Hello World"

booleanExample = False

def testInt():
    assert type(intExample) == int

def testFloat():
    assert type(floatExample) == float

def testString():
    assert type(stringExample) == str

def testBoolean():
    assert type(booleanExample) == bool
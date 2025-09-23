import numpy as np
import pytest

def multArray(a1, a2):
    a = np.array(a1)
    b = np.array(a2)
    return a * b

def multByScalar(a1, scalar):
    a = np.array(a1)
    return a * scalar

array1 = [1,2,3]
array2 = [4,5,6]
scalar = 2

def testMultbyArray():
    result = multArray(array1, array2)
    expected = np.array([4, 10, 18])
    assert np.array_equal(result, expected)

def testMultbyScalar():
    result = multByScalar(array1, scalar)
    expected = np.array([2, 4, 6])
    assert np.array_equal(result, expected)

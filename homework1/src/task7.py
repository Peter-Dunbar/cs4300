import numpy as np

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

print("multiplied arrays:", multArray(array1, array2))
print("multiplied by Scalar:", multByScalar(array1, scalar))
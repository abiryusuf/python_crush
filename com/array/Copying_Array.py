# importing the module
from numpy import *
import numpy as np

# creating the first array
arr1 = array([2, 3, 6, 1, 4])
arr2 = arr1
print(arr2)
# shallow copy: it will copy the element but memory location will be different.
# If I change or update a value in arr1, it will copy the same in arr2 but in deep copy won't
arr2 = arr1.view()

# Deep copy: it will copy the element with different value and memory location
# arr2 = arr1.copy()
arr1[1] = 7
# (arr1)
print(arr2)

# it shows same value and same location ID
print(id(arr1))
# print(id(arr2))

arr3 = array([79, 45, 34, 12])
print(arr3)

arr4 = arr3
print(arr4)

arr4 = arr3.view()
arr4[0] = 3
print(arr4)
print(id(arr4))
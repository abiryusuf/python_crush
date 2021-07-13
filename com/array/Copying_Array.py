# importing the module
from numpy import *
import numpy as np

# creating the first array
arr1 = array([2, 3, 6, 1, 4])

# shallow copy: it will copy the element but memory location will be different.
arr2 = arr1.view()

# Deep copy: it will store the array with different array and memory location
arr2 = arr1.copy()
arr1[1] = 7
print(arr1)
print(arr2)

# it shows same value and same location ID
print(id(arr1))
print(id(arr2))

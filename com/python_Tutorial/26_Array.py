"""
Array is a collection of variable, array and list same but array contains only
same data type where list contains different data type
"""

import array as arr
from array import *

vals = array('i', [3, 5, 7, -2, 8])

for i, value in enumerate(vals):
    print("Key {} and value {}".format(i, value))

for i in range(len(vals)):
    print(i)
vals.reverse()
print(vals[0])

vals.append(10)
vals.remove(10)
print(vals)

newArr = array(vals.typecode, (a*a for a in vals))
print(newArr)
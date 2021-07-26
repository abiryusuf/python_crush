"""
Array is a collection of variable, array and list same but array contains only
same data type where list contains different data type
"""

import array as arr
from array import *

# vals = array('i', [3, 5, 7, -2, 8])
#
# for i, value in enumerate(vals):
#     print("Key {} and value {}".format(i, value))
#
# for i in range(len(vals)):
#     print(i)
# vals.reverse()
# print(vals[0])
#
# vals.append(10)
# vals.remove(10)
# print(vals)
#
# newArr = array(vals.typecode, (a*a for a in vals))
# print(newArr)


# Search the array

arr = array("i", [])
#
# length = int(input("Enter the length of the array  "))
#
# for i in range(length):
#     x = int(input("Enter the next value: "))
#     arr.append(x)
# print(arr)
#
# # find the index from the array
# val = int(input("Enter the value "))
#
# count = 0
#
# for e in arr:
#     if e == val:
#         print(count)
#         break
#     count += 1


arr_1 = []

size = int(input("Enter the length of array  "))

for i in range(size):
    x = int(input("Enter the next value "))
    arr_1.append(x)
print(arr_1)

target = int(input("Inter the target value "))
res = 0
for i in arr_1:
    if i == target:
        print(res)
        break
    res += 1
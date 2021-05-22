
"""
Main purpose the binary search is "don't need to execute the whole list to find the
target value, so it is save time
we can divided low and high and find the mid and make a condition with low and high

I can eliminate half the values in the list when the target value is not found at the
middle position
"""
pos = -1
def binarySearch(value, target):
    low = 0
    high = len(value) - 1

    while low < high:
        mid = (low + high) // 2
        if value[mid] == target:
            globals()["pos"] = mid
            return True
        if value[mid] < target:
            low = mid
        else:
            high = mid
    return False
item = [3, 5, 6, 7, 10, 46, 50]
target = 5

# if binarySearch(item, target):
#     print("Found at", item)
# else:
#     print("not found")

x = binarySearch(item, target)
if x == -1:
    print("Not found")
else:
    print("Found", pos + 1)

def recBinarySearch(target, value, first, last):
    if first > last:
        return False
    else:
        mid = (first + last) // 2
        if value[mid] == target:
            return True
        elif target < value[mid]:
            return recBinarySearch(target, value, first, mid - 1)
        else:
            return recBinarySearch(target, value, mid + 1, last)
    return False

# value = [3, 5, 6, 7, 10, 46, 50]
# target = 6
# first = 3
# last = 50
# y = recBinarySearch(target, value, first, last)
# if y == -1:
#     print("Not Found")
# else:
#     print("found")

y = 2 ** 8
print(y)

def exp(x, n):
    y = 1
    for i in range(n):
        y *= x
    return y
print(exp(8, 2))




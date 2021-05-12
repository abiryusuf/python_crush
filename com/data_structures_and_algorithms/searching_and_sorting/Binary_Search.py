
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





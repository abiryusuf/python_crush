
"""
sequential search the item from list and loop will execute until find the target
if not found it will return -1

Linear search: finding the phone number by searching in phone
"""
# Finding the a specific item
def linear_search(value, target1):
    length = len(value)
    for i in range(0, length):
        if value[i] == target1:
            return i
    return -1
arr = [4, 5, 6, 7, 9]
target = 5

x = linear_search(arr, target)
if x == -1:
    print("Item is not found")
else:
    print("Item is found and index number is {}".format(x))

# Searching a sorted sequence
print(sorted(arr))

def sortedLinearSearch(values, item):
    values = sorted(values)

    length = len(values)

    for i in range(0, length):
        if values[i] == item:
            return True
        elif values[i] > item:
            return False
    return False
value = [3, 5, 6, 7, 8]
item = 7
y = sortedLinearSearch(value, item)
print(y)


# Finding the smallest Value
def findSmallest(theValues):
    length = len(theValues)
    smallest = theValues[0]
    for i in range(1, length):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest
num = [3, 5, 6, 8, 2]
print(findSmallest(num))



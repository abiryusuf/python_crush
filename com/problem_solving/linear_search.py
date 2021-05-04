# find the index number from array list
# e.g arr = [2, 3, 5, 45, 23] in index = 2, item = 5

def linear_search(arr, n, item):  # arr = list, n = size, item = number from list
    for i in range(0, n):
        if arr[i] == item:
            return i
    return -1
arr1 = [2, 3, 4, 5, 10]
n = len(arr1)
item = 9
x = linear_search(arr1, n, item)
if(x == -1):
    print("item not found")
else:
    print("item is found")





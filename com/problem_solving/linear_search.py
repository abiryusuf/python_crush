# find the index number from array list
# e.g arr = [2, 3, 5, 45, 23] in index = 2, item = 5
# Runtime complexity: 0(N), it will execute N number based on the loop
# Space Complexity: 0(1), Don't take extra memory to store the data

def linear_search(arr, size, item):  # arr = list, n = size, item = number from list
    for i in range(0, size):
        if arr[i] == item:
            return i
    return -1
arr1 = [2, 3, 4, 5, 10]
size = len(arr1)
item = 9
x = linear_search(arr1, size, item)
if(x == -1):
    print("Item is not found")
else:
    print("Item is found")





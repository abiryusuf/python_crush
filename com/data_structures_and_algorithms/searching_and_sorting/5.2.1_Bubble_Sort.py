"""
Bubble Sort: Rearranges the value by iterating over the list multiple times, causing
larger values to bubble to the top or end of the list.

Main reasons is find the large value from end of the list
Bubble sort needs two loops
"""
arr = [2, 5, 1, 3, 11, 90]
length = len(arr)

# for i in range(length):
#     print(i + 1)


# x = arr[+1]
# print(x)

def bubbleSort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
       # print(arr[i])
bubbleSort(arr)

for i in range(length):
    print("%d" % arr[i])
# x = arr[+1]
# print(x)
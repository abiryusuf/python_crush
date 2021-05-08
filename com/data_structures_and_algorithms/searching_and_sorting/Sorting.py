"""
Sorting is the process of arranging or ordering a collection of items such
that each item and its successor satisfy a prescribed relationship
e.g [2, 5, 6, 3, 1] output [1, 2, 3, 5, 6 ]
"""


# Bubble sort: follow the order from biggest number
# e . g [ 2, 4, 1, 9, 8] put the biggest number in the last


# Selection sort
# follow the order from smallest number

arr = [3, 8, 5, 9, 6]
def selectionSort(num):
    length = len(num)
    for i in range(length - 1):
        smallIndex = i
        for j in range(i + 1, length):
            if num[j] < num[smallIndex]:
                smallIndex = j
        if smallIndex != i:
            temp = num[i]
        num[i] = num[smallIndex]
        num[smallIndex] = temp


selectionSort(arr)
print(arr)


print(selectionSort(arr))







arr = [1,3,4,5]

x = len(arr) - 1
y = len(arr)
print(x, y)

def mergeSortedList(ListA, ListB):
    a = 0
    b = 0
    newList = list()

    while a < len(ListA) and b < len(ListA):
        if ListA[a] < ListB[b]:
            newList.append(ListA[a])
            a += 1
        else:
            newList.append(ListB[b])
            b += 1
    # Add new item
    while a < len(ListA):
        newList.append(ListA[a])
        a += 1
    while b < len(ListB):
        newList.append(ListB[b])
        b += 1
    return newList
print(mergeSortedList([1, 2, 4, 7], [4, 5, 6, 8]))

arr1 = [1, 3, 5, 7]
arr2 = [4, 6, 3, 7]
def common_elements(listA, listB):
    x = 0
    y = 0
    newList = list()

    while x < len(listA) and y < len(listB):
        if listA[x] == listB[y]:
            newList.append(listA[x] and newList.append(listB[y]))
            x += 1
            y += 1
        elif listA[x] < listB[y]:
            x += 1
        else:
            y += 1
    return newList
print(common_elements(arr1, arr2))
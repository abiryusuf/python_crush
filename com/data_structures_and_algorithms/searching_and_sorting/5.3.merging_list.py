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